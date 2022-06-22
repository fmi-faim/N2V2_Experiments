import json
import argparse
from os.path import join, split, basename
import time
from glob import glob

from n2v.models import N2VConfig, N2V
import numpy as np
from n2v.utils.n2v_utils import manipulate_val_data
from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
from n2v.utils.evaluation_utils import best_PSNR

import subprocess

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
    
def compute_best_psnrs(input_data, gt_data):
    psnrs = []
    for img, gt in zip(test_input, test_gt):
        pred = model.predict(img.astype(np.float32), "YXC", tta=False)
        psnrs.append(best_PSNR(gt, img, gt.max() - gt.min()))
    
    return np.array(psnrs)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Run config file.")
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
    model = N2V(n2v_conf, config["name"], basedir=join(config["expdir"], "models"))
    model.prepare_for_training(metrics=())
    
    if use_wandb:
        model.callbacks.append(WandbCallback())
    
    history = model.train(X, X_val)
    
    model.load_weights("weights_best.h5")
    best_psnrs = compute_best_psnrs(test_input, test_gt)
    
    model.load_weights("weights_last.h5")
    last_psnrs = compute_best_psnrs(test_input, test_gt)
    
    with open(join(config["expdir"], "results.csv"), "w") as f:
        f.write("best_psnr, last_psnr\n")
        for best, last in zip(best_psnrs, last_psnrs):
            f.write(f"{best}, {last}\n")
            
    if use_wandb:
        wandb.log(
            {
                "best_avg_psnr": np.mean(best_psnrs),
                "last_avg_psnr": np.mean(last_psnrs)
            }
        )
    
    if use_wandb:
        run.finish(exit_code=0)
    

    
