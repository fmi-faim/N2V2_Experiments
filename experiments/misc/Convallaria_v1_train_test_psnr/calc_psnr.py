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

def compute_best_psnrs(input_data, gt_data, fun):
    psnrs = []
    for n, (img, gt) in enumerate(zip(input_data, gt_data)):
        psnrs.append(fun(gt, img, gt.max() - gt.min()))

    return np.array(psnrs)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Run config file.")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)

    X = load_data(config["train_data"], key="x_train")
    gt = load_data(config["train_data"].replace("train.npz", "train_gt.npz"), key="gt_train")
    psnrs = compute_best_psnrs(X, gt, fun=best_PSNR)
    print("train best_psnr", np.mean(psnrs))

    X = load_data(config["test_input"], key="x_test")
    gt = load_data(config["test_gt"], key="gt_test")
    psnrs = compute_best_psnrs(X, gt, fun=best_PSNR)
    print("test best_PSNR", np.mean(psnrs))
