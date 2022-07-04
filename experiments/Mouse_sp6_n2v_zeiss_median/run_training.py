import json
import argparse
from os.path import join, split, basename, exists
import os
import time
from glob import glob

from n2v.models import N2VConfig, N2V
import numpy as np
from n2v.utils.n2v_utils import manipulate_val_data
from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
from n2v.utils.evaluation_utils import best_PSNR, PSNR
from csbdeep.utils.utils import normalize_minmse

import subprocess

import matplotlib.pyplot as plt
from skimage.io import imsave


def load_data(path, key="x_train"):
    if basename(path) == "DCNN400_train_gaussian25.npy":
        return np.load(path)[..., np.newaxis]
    elif basename(path) == "DCNN400_validation_gaussian25.npy":
        return np.load(path)[..., np.newaxis]
    elif basename(path) == "bsd68_gaussian25.npy":
        data = np.load(path, allow_pickle=True)
        data = [d[..., np.newaxis] for d in data]
        return data
    elif basename(path) == "bsd68_groundtruth.npy":
        data = np.load(path, allow_pickle=True)
        data = [d[..., np.newaxis] for d in data]
        return data
    elif path.endswith(".npz"):
        return np.load(path)[key]
    else:
        raise NotImplementedError("File-format not supported.")

def save_img(n, img, gt, pred, out_dir):
    img_dir = join(config["expdir"], out_dir)
    if not exists(img_dir):
        os.makedirs(img_dir)

    if gt.max() > 255:
        img_pred = pred.squeeze().clip(0, 65536).astype(np.uint16)
        img_gt = gt.squeeze().clip(0, 65536).astype(np.uint16)
    else:
        img_pred = pred.squeeze().clip(0, 255).astype(np.uint8)
        img_gt = gt.squeeze().clip(0, 255).astype(np.uint8)
    imsave(join(config["expdir"], out_dir, f"pred_{n:03}.tif"), img_pred)
    imsave(join(config["expdir"], out_dir, f"gt_{n:03}.tif"), img_gt)

    plt.figure(figsize=(16, 8))
    plt.subplot(1, 3, 1)
    plt.title("gt")
    plt.imshow(gt)
    plt.subplot(1, 3, 2)
    plt.title("img")
    plt.imshow(img.astype(np.float32))
    plt.subplot(1, 3, 3)
    plt.title("pred")
    plt.imshow(pred)
    plt.savefig(join(config["expdir"], out_dir, f"{n:03}.jpg"))
    plt.close()

    img_n = normalize_minmse(img, gt)
    plt.figure(figsize=(16, 8))
    plt.subplot(1, 2, 1)
    plt.title("gt - img_n")
    plt.imshow(gt - img_n)
    plt.colorbar()
    plt.subplot(1, 2, 2)
    plt.title("square(gt - img_n)")
    plt.imshow(np.square(gt - img_n))
    plt.colorbar()
    plt.savefig(join(config["expdir"], out_dir, f"diff_{n:03}.jpg"))
    plt.close()

def compute_best_psnrs(model, input_data, gt_data, fun):
    psnrs = []
    for n, (img, gt) in enumerate(zip(input_data, gt_data)):
        pred = model.predict(img.astype(np.float32), "YXC", tta=False)
        psnrs.append(fun(gt, pred, gt.max() - gt.min()))
        if args.save_imgs:
            save_img(n, img, gt, pred, fun.__name__)

    return np.array(psnrs)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Run config file.")
    parser.add_argument('--save_imgs', action='store_true', default=False)
    parser.add_argument('--skip_train', action='store_true', default=False)
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)

    use_wandb = config["wandb"]["logging_on"]
    if use_wandb:
        import wandb
        from wandb.keras import WandbCallback

    if use_wandb:
        run = wandb.init(project=config["wandb"]["project"],
                         entity=config["wandb"]["entity"],
                         name=config["wandb"]["name"],
                         config=config)
    X = load_data(config["train_data"], key="x_train")
    X_val = load_data(config["val_data"], key="x_val")
    test_input = load_data(config["test_input"], key="x_test")
    test_gt = load_data(config["test_gt"], key="gt_test")

    assert len(X.shape) == 4
    assert len(X_val.shape) == 4
    assert len(test_input[0].shape) == 3
    assert len(test_gt[0].shape) == 3

    n2v_conf = N2VConfig(X, **config["n2v_config"])
    base_dir = join(config["expdir"], "models")
    model = N2V(n2v_conf, config["name"], basedir=base_dir)
    if not args.skip_train:
        model.prepare_for_training(metrics=())

        if use_wandb:
            model.callbacks.append(WandbCallback())

        history = model.train(X, X_val)
    else:
        print(f"skipping training, loading models from {base_dir}")

    model.load_weights("weights_best.h5")
    bestPSNR_wbest = compute_best_psnrs(model, test_input, test_gt, fun=best_PSNR)
    PSNR_wbest = compute_best_psnrs(model, test_input, test_gt, fun=PSNR)

    model.load_weights("weights_last.h5")
    bestPSNR_wlast = compute_best_psnrs(model, test_input, test_gt, fun=best_PSNR)
    PSNR_wlast = compute_best_psnrs(model, test_input, test_gt, fun=PSNR)

    with open(join(config["expdir"], "results.csv"), "w") as f:
        f.write("bestPSNR_wbest, bestPSNR_wlast, PSNR_wbest, PSNR_wlast\n")
        for best_wbest, best_wlast, wbest, wlast in zip(bestPSNR_wbest, bestPSNR_wlast, PSNR_wbest, PSNR_wlast):
            f.write(f"{best_wbest}, {best_wlast}, {wbest}, {wlast}\n")

    if use_wandb:
        wandb.log(
            {
                "bestPSNR_wbest": np.mean(bestPSNR_wbest),
                "bestPSNR_wlast": np.mean(bestPSNR_wlast),
                "PSNR_wbest": np.mean(PSNR_wbest),
                "PSNR_wlast": np.mean(PSNR_wlast)
            }
        )

    if use_wandb:
        run.finish(exit_code=0)



