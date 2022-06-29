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
|[Flywing_g70_n2v_zeiss_baseline](experiments/Flywing_g70_n2v_zeiss_baseline)           | 25.078 |          25.131 |          25.105 |          25.160 ||
|[Mouse_g20_n2v_zeiss_baseline](experiments/Mouse_g20_n2v_zeiss_baseline)               | 34.021 |          34.051 |          34.030 |          34.060 ||
|[Mouse_sp12_n2v_zeiss_baseline](experiments/Mouse_sp12_n2v_zeiss_baseline)             | 22.749 |          22.868 |          32.741 |          32.812 ||
|[Mouse_sp3_n2v_zeiss_baseline](experiments/Mouse_sp3_n2v_zeiss_baseline)               | 30.161 |          30.525 |          34.859 |          34.924 ||
|[Mouse_sp6_n2v_zeiss_baseline](experiments/Mouse_sp6_n2v_zeiss_baseline)               | 27.292 |          27.225 |          34.067 |          34.040 ||
|[Convallaria_n2v_zeiss_baseline](experiments/Convallaria_n2v_zeiss_baseline)           | 35.700 |          35.666 |          35.738 |          35.688 ||

# No shift and `unet_residuals=false`
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Convallaria_n2v_zeiss_baseline](experiments/Convallaria_n2v_zeiss_baseline)           | 34.831 |          34.813 |          34.851 |          34.852 ||
|[Convallaria_n2v_zeiss_mean](experiments/Convallaria_n2v_zeiss_mean)                   | 35.287 |          35.270 |          35.311 |          35.332 ||
|[Convallaria_n2v_zeiss_mean_bp_sk](experiments/Convallaria_n2v_zeiss_mean_bp_sk)       | 34.589 |          34.597 |          34.638 |          34.660 ||
|[Convallaria_n2v_zeiss_median](experiments/Convallaria_n2v_zeiss_median)               | 35.460 |          35.489 |          35.498 |          35.519 ||
|[Convallaria_n2v_zeiss_median_bp_sk](experiments/Convallaria_n2v_zeiss_median_bp_sk)   | 34.547 |          34.554 |          34.591 |          34.591 ||
|[Flywing_g70_n2v_zeiss_baseline](experiments/Flywing_g70_n2v_zeiss_baseline)           | 25.043 |          25.077 |          25.074 |          25.105 ||
|[Flywing_g70_n2v_zeiss_mean](experiments/Flywing_g70_n2v_zeiss_mean)                   | 25.359 |          25.359 |          25.413 |          25.413 ||
|[Flywing_g70_n2v_zeiss_mean_bp_sk](experiments/Flywing_g70_n2v_zeiss_mean_bp_sk)       | 25.268 |          25.283 |          25.318 |          25.332 ||
|[Flywing_g70_n2v_zeiss_median](experiments/Flywing_g70_n2v_zeiss_median)               | 25.426 |          25.458 |          25.474 |          25.515 ||
|[Flywing_g70_n2v_zeiss_median_bp_sk](experiments/Flywing_g70_n2v_zeiss_median_bp_sk)   | 25.373 |          25.390 |          25.415 |          25.430 ||
|[Mouse_g20_n2v_zeiss_baseline](experiments/Mouse_g20_n2v_zeiss_baseline)               | 33.225 |          33.295 |          33.261 |          33.316 ||
|[Mouse_g20_n2v_zeiss_mean](experiments/Mouse_g20_n2v_zeiss_mean)                       | 33.560 |          33.582 |          33.646 |          33.670 ||
|[Mouse_g20_n2v_zeiss_mean_bp_sk](experiments/Mouse_g20_n2v_zeiss_mean_bp_sk)           | 32.821 |          32.997 |          33.031 |          33.056 ||
|[Mouse_g20_n2v_zeiss_median](experiments/Mouse_g20_n2v_zeiss_median)                   | 33.520 |          33.613 |          33.588 |          33.659 ||
|[Mouse_g20_n2v_zeiss_median_bp_sk](experiments/Mouse_g20_n2v_zeiss_median_bp_sk)       | 33.000 |          33.033 |          33.039 |          33.070 ||
|[Mouse_sp12_n2v_zeiss_baseline](experiments/Mouse_sp12_n2v_zeiss_baseline)             | 22.987 |          22.925 |          33.449 |          33.471 ||
|[Mouse_sp12_n2v_zeiss_mean](experiments/Mouse_sp12_n2v_zeiss_mean)                     | 23.215 |          23.078 |          32.697 |          32.866 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk)         | 22.984 |          22.961 |          32.083 |          32.360 ||
|[Mouse_sp12_n2v_zeiss_median](experiments/Mouse_sp12_n2v_zeiss_median)                 | 23.167 |          22.852 |          32.750 |          33.073 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk)     | 22.685 |          22.658 |          31.722 |          32.066 ||
|[Mouse_sp3_n2v_zeiss_baseline](experiments/Mouse_sp3_n2v_zeiss_baseline)               | 29.840 |          30.171 |          34.371 |          34.470 ||
|[Mouse_sp3_n2v_zeiss_mean](experiments/Mouse_sp3_n2v_zeiss_mean)                       | 29.458 |          29.912 |          33.795 |          33.792 ||
|[Mouse_sp3_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp3_n2v_zeiss_mean_bp_sk)           | 29.957 |          29.884 |          33.313 |          33.485 ||
|[Mouse_sp3_n2v_zeiss_median](experiments/Mouse_sp3_n2v_zeiss_median)                   | 30.198 |          30.221 |          34.691 |          34.742 ||
|[Mouse_sp3_n2v_zeiss_median_bp_sk](experiments/Mouse_sp3_n2v_zeiss_median_bp_sk)       | 29.855 |          29.752 |          33.493 |          33.504 ||
|[Mouse_sp6_n2v_zeiss_baseline](experiments/Mouse_sp6_n2v_zeiss_baseline)               | 26.804 |          27.104 |          33.663 |          34.079 ||
|[Mouse_sp6_n2v_zeiss_mean](experiments/Mouse_sp6_n2v_zeiss_mean)                       | 26.612 |          27.408 |          33.652 |          34.041 ||
|[Mouse_sp6_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp6_n2v_zeiss_mean_bp_sk)           | 26.998 |          27.063 |          32.860 |          33.098 ||
|[Mouse_sp6_n2v_zeiss_median](experiments/Mouse_sp6_n2v_zeiss_median)                   | 27.310 |          27.066 |          33.379 |          33.882 ||
|[Mouse_sp6_n2v_zeiss_median_bp_sk](experiments/Mouse_sp6_n2v_zeiss_median_bp_sk)       | 27.372 |          26.943 |          33.178 |          33.211 ||
|[Mouse_sp12_n2v_zeiss_baseline_shallow](experiments/Mouse_sp12_n2v_zeiss_baseline_shallow)         | 22.876 |          22.910 |          33.140 |          33.368 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow)     | 22.735 |          23.017 |          31.922 |          32.200 ||
|[Mouse_sp12_n2v_zeiss_mean_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_shallow)                 | 22.870 |          23.109 |          32.481 |          32.822 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk_shallow) | 21.112 |          20.896 |          23.801 |          23.761 ||
|[Mouse_sp12_n2v_zeiss_median_shallow](experiments/Mouse_sp12_n2v_zeiss_median_shallow)             | 22.877 |          22.804 |          32.944 |          33.036 ||
