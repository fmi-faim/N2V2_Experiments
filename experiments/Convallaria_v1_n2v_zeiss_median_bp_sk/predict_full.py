import json
import argparse
from os.path import join

from n2v.models import N2VConfig, N2V
import numpy as np

import matplotlib.pyplot as plt
from tqdm import tqdm


def predict_X(X, model):
    preds = []
    for n, img in tqdm(enumerate(X), total=X.shape[0]):
        pred = model.predict(img.astype(np.float32), "YXC", tta=False)
        if False:
            plt.figure(figsize=(16, 8))
            plt.subplot(1, 2, 1), plt.title("img"), plt.imshow(img, cmap=plt.get_cmap("magma"))
            plt.subplot(1, 2, 2), plt.title("pred"), plt.imshow(pred, cmap=plt.get_cmap("magma"))
            plt.show()
        preds.append(pred)
    return np.stack(preds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Run config file.")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = json.load(f)
    X = np.load(config["full_data"])["full"][..., np.newaxis]

    n2v_conf = N2VConfig(X[:1], **config["n2v_config"])
    base_dir = join(config["expdir"], "models")
    model = N2V(n2v_conf, config["name"], basedir=base_dir)

    model.load_weights("weights_best.h5")
    predictions_best = predict_X(X, model)

    model.load_weights("weights_last.h5")
    predictions_last = predict_X(X, model)

    np.savez(
        "predictions_full.npz",
        predictions_best=predictions_best,
        predictions_last=predictions_last,
    )
