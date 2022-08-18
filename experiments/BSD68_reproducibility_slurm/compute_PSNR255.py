import json
import argparse
from os.path import join, split, basename
import time
from glob import glob

from n2v.models import N2VConfig, N2V
import numpy as np
from n2v.utils.n2v_utils import manipulate_val_data
from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
from n2v.utils.evaluation_utils import best_PSNR, PSNR

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
    
def compute_best_psnrs(model, input_data, gt_data, fun):
    psnrs = []
    for img, gt in zip(input_data, gt_data):
        pred = model.predict(img.astype(np.float32), "YXC", tta=False)
        psnrs.append(fun(gt, pred, 255.0))
    
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
    
    test_input = load_data(config["test_input"], key="x_test")
    test_gt = load_data(config["test_gt"], key="gt_test")
    
    model = N2V(None, config["name"], basedir=join(config["expdir"], "models"))
    
    model.load_weights("weights_best.h5")
    bestPSNR_wbest = compute_best_psnrs(model, test_input, test_gt, fun=best_PSNR)
    PSNR_wbest = compute_best_psnrs(model, test_input, test_gt, fun=PSNR)
    
    model.load_weights("weights_last.h5")
    bestPSNR_wlast = compute_best_psnrs(model, test_input, test_gt, fun=best_PSNR)
    PSNR_wlast = compute_best_psnrs(model, test_input, test_gt, fun=PSNR)
    
    with open(join(config["expdir"], "results_255.csv"), "w") as f:
        f.write("bestPSNR_wbest, bestPSNR_wlast, PSNR_wbest, PSNR_wlast\n")
        for best_wbest, best_wlast, wbest, wlast in zip(bestPSNR_wbest, bestPSNR_wlast, PSNR_wbest, PSNR_wlast):
            f.write(f"{best_wbest}, {best_wlast}, {wbest}, {wlast}\n")
            
    
    with open(join(config["expdir"], "results_255_avg.csv"), "w") as f:
        f.write("PSNR_wbest, PSNR_wlast, bestPSNR_wbest, bestPSNR_wlast\n")
        f.write(f"{np.mean(PSNR_wbest)}, {np.mean(PSNR_wlast)}, {np.mean(bestPSNR_wbest)}, {np.mean(bestPSNR_wlast)}\n")
        

    
