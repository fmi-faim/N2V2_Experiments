# Experiments Overview

## Baselines

| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_slurm](./experiments/BSD68_reproducibility_slurm)| 26.76 | 27.00 | 26.86 | 27.00 | uniform_withCP |
|[BSD68_reproducibility_slurm-run1](./experiments/BSD68_reproducibility_slurm-run1)|  |  |  |  | uniform_withCP | uniform_withoutCP |
|[Convallaria_n2v_baseline_slurm](./experiments/Convallaria_n2v_baseline_slurm)| 35.40 | 35.55 | 35.43 | 35.57 | uniform_withoutCP |
|[Flywing_g70_n2v_baseline_slurm](./experiments/Flywing_g70_n2v_baseline_slurm)| 24.96 | 24.98 | 24.99 | 25.02 | uniform_withoutCP |
|[Mouse_g20_n2v_baseline_slurm](./experiments/Mouse_g20_n2v_baseline_slurm)| 33.88 | 33.90 | 33.90 | 33.90 | uniform_withoutCP |
|[Mouse_sp12_n2v_baseline_slurm](./experiments/Mouse_sp12_n2v_baseline_slurm)| 22.96 | 22.95 | 32.66 | 33.42 | uniform_withoutCP |
|[Mouse_sp3_n2v_baseline_slurm](./experiments/Mouse_sp3_n2v_baseline_slurm)| 30.31 | 30.42 | 34.65 | 34.75 | uniform_withoutCP |
|[Mouse_sp6_n2v_baseline_slurm](./experiments/Mouse_sp6_n2v_baseline_slurm)| 27.27 | 27.25 | 34.38 | 34.42 | uniform_withoutCP |

## Results `mean_median_uniformWOcp_v1_noshift_v2.patch`
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_zeiss_baseline](experiments/BSD68_reproducibility_zeiss_baseline)           | 26.664 |          26.944 |          26.715 |          26.946 ||
|[BSD68_reproducibility_zeiss_mean](experiments/BSD68_reproducibility_zeiss_mean)                   | 26.990 |          27.491 |          27.179 |          27.520 ||
|[BSD68_reproducibility_zeiss_mean_bp_sk](experiments/BSD68_reproducibility_zeiss_mean_bp_sk)       | 26.990 |          27.561 |          27.155 |          27.580 ||
|[BSD68_reproducibility_zeiss_median](experiments/BSD68_reproducibility_zeiss_median)               | 26.670 |          26.760 |          26.717 |          26.766 ||
|[BSD68_reproducibility_zeiss_median_bp_sk](experiments/BSD68_reproducibility_zeiss_median_bp_sk)   | 26.961 |          27.584 |          27.075 |          27.595 ||
|[Convallaria_n2v_zeiss_baseline](experiments/Convallaria_n2v_zeiss_baseline)                       | 35.734 |          35.729 |          35.750 |          35.758 ||
|[Convallaria_n2v_zeiss_mean](experiments/Convallaria_n2v_zeiss_mean)                               | 35.570 |          35.572 |          35.997 |          35.900 ||
|[Convallaria_n2v_zeiss_mean_bp_sk](experiments/Convallaria_n2v_zeiss_mean_bp_sk)                   | 36.045 |          36.150 |          36.198 |          36.271 ||
|[Convallaria_n2v_zeiss_median](experiments/Convallaria_n2v_zeiss_median)                           | 36.100 |          36.228 |          36.416 |          36.391 ||
|[Convallaria_n2v_zeiss_median_bp_sk](experiments/Convallaria_n2v_zeiss_median_bp_sk)               | 36.304 |          36.252 |          36.337 |          36.362 ||
|[Flywing_g70_n2v_zeiss_baseline](experiments/Flywing_g70_n2v_zeiss_baseline)                       | 25.125 |          25.213 |          25.156 |          25.242 ||
|[Flywing_g70_n2v_zeiss_mean](experiments/Flywing_g70_n2v_zeiss_mean)                               | 25.435 |          25.453 |          25.499 |          25.536 ||
|[Flywing_g70_n2v_zeiss_mean_bp_sk](experiments/Flywing_g70_n2v_zeiss_mean_bp_sk)                   | 25.402 |          25.439 |          25.460 |          25.478 ||
|[Flywing_g70_n2v_zeiss_median](experiments/Flywing_g70_n2v_zeiss_median)                           | 25.490 |          25.500 |          25.568 |          25.569 ||
|[Flywing_g70_n2v_zeiss_median_bp_sk](experiments/Flywing_g70_n2v_zeiss_median_bp_sk)               | 25.406 |          25.408 |          25.458 |          25.458 ||
|[Mouse_g20_n2v_zeiss_baseline](experiments/Mouse_g20_n2v_zeiss_baseline)                           | 34.165 |          34.183 |          34.172 |          34.196 ||
|[Mouse_g20_n2v_zeiss_mean](experiments/Mouse_g20_n2v_zeiss_mean)                                   | 33.923 |          34.390 |          34.410 |          34.493 ||
|[Mouse_g20_n2v_zeiss_mean_bp_sk](experiments/Mouse_g20_n2v_zeiss_mean_bp_sk)                       | 34.316 |          34.487 |          34.498 |          34.607 ||
|[Mouse_g20_n2v_zeiss_median](experiments/Mouse_g20_n2v_zeiss_median)                               | 34.273 |          34.258 |          34.412 |          34.410 ||
|[Mouse_g20_n2v_zeiss_median_bp_sk](experiments/Mouse_g20_n2v_zeiss_median_bp_sk)                   | 34.202 |          34.637 |          34.414 |          34.736 ||
|[Mouse_sp12_n2v_zeiss_baseline](experiments/Mouse_sp12_n2v_zeiss_baseline)                         | 23.195 |          22.984 |          33.834 |          34.121 ||
|[Mouse_sp12_n2v_zeiss_baseline_shallow](experiments/Mouse_sp12_n2v_zeiss_baseline_shallow)         | 23.012 |          23.046 |          33.974 |          34.010 ||
|[Mouse_sp12_n2v_zeiss_mean](experiments/Mouse_sp12_n2v_zeiss_mean)                                 | 23.678 |          23.248 |          33.872 |          33.659 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk)                     | 22.522 |          23.184 |          32.911 |          34.167 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow)     | 23.168 |          23.217 |          33.908 |          33.903 ||
|[Mouse_sp12_n2v_zeiss_mean_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_shallow)                 | 23.296 |          23.213 |          33.124 |          33.259 ||
|[Mouse_sp12_n2v_zeiss_median](experiments/Mouse_sp12_n2v_zeiss_median)                             | 23.018 |          22.919 |          33.571 |          33.454 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk)                 | 23.465 |          22.997 |          34.389 |          34.540 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk_shallow) | 23.343 |          22.983 |          33.824 |          33.882 ||
|[Mouse_sp12_n2v_zeiss_median_shallow](experiments/Mouse_sp12_n2v_zeiss_median_shallow)             | 22.880 |          22.880 |          32.986 |          32.981 ||
|[Mouse_sp3_n2v_zeiss_baseline](experiments/Mouse_sp3_n2v_zeiss_baseline)                           | 30.441 |          30.630 |          35.383 |          35.444 ||
|[Mouse_sp3_n2v_zeiss_mean](experiments/Mouse_sp3_n2v_zeiss_mean)                                   | 30.745 |          30.663 |          35.270 |          35.290 ||
|[Mouse_sp3_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp3_n2v_zeiss_mean_bp_sk)                       | 31.117 |          30.808 |          34.997 |          35.506 ||
|[Mouse_sp3_n2v_zeiss_median](experiments/Mouse_sp3_n2v_zeiss_median)                               | 30.473 |          30.394 |          35.254 |          35.228 ||
|[Mouse_sp3_n2v_zeiss_median_bp_sk](experiments/Mouse_sp3_n2v_zeiss_median_bp_sk)                   | 29.681 |          30.746 |          35.069 |          35.809 ||
|[Mouse_sp6_n2v_zeiss_baseline](experiments/Mouse_sp6_n2v_zeiss_baseline)                           | 27.538 |          27.411 |          34.809 |          34.890 ||
|[Mouse_sp6_n2v_zeiss_mean](experiments/Mouse_sp6_n2v_zeiss_mean)                                   | 27.454 |          27.498 |          34.633 |          34.710 ||
|[Mouse_sp6_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp6_n2v_zeiss_mean_bp_sk)                       | 27.896 |          27.582 |          34.893 |          35.009 ||
|[Mouse_sp6_n2v_zeiss_median](experiments/Mouse_sp6_n2v_zeiss_median)                               | 26.814 |          27.355 |          34.858 |          35.066 ||
|[Mouse_sp6_n2v_zeiss_median_bp_sk](experiments/Mouse_sp6_n2v_zeiss_median_bp_sk)                   | 27.348 |          27.529 |          35.476 |          35.496 ||
|[Convallaria_v1_n2v_zeiss_baseline](experiments/Convallaria_v1_n2v_zeiss_baseline)                 | 30.764 |          31.235 |          31.094 |          31.266 ||
|[Convallaria_v1_n2v_zeiss_mean](experiments/Convallaria_v1_n2v_zeiss_mean)                         | 30.772 |          31.681 |          31.375 |          31.838 ||
|[Convallaria_v1_n2v_zeiss_mean_bp_sk](experiments/Convallaria_v1_n2v_zeiss_mean_bp_sk)             | 28.096 |          31.286 |          28.449 |          31.357 ||
|[Convallaria_v1_n2v_zeiss_median](experiments/Convallaria_v1_n2v_zeiss_median)                     | 30.951 |          31.585 |          31.519 |          31.766 ||
|[Convallaria_v1_n2v_zeiss_median_bp_sk](experiments/Convallaria_v1_n2v_zeiss_median_bp_sk)         | 30.550 |          31.252 |          30.995 |          31.284 ||
