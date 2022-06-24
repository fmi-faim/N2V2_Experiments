# Experiments Overview

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
|[Convallaria_n2v_zeiss_mean](experiments/Convallaria_n2v_zeiss_mean)                | 22.258734 |       22.282437 |       25.522387 |       25.435619 ||
|[Convallaria_n2v_zeiss_median](experiments/Convallaria_n2v_zeiss_median)            | 27.442528 |       27.872378 |       28.409888 |       28.890761 ||
|[Flywing_g70_n2v_zeiss_mean](experiments/Flywing_g70_n2v_zeiss_mean)                |  9.964426 |        9.307624 |       17.739788 |       17.652367 ||
|[Flywing_g70_n2v_zeiss_median](experiments/Flywing_g70_n2v_zeiss_median)            | 15.843161 |       15.865043 |       19.422810 |       19.435305 ||
|[Mouse_g20_n2v_zeiss_mean](experiments/Mouse_g20_n2v_zeiss_mean)                    | 20.209486 |       20.184326 |       22.476917 |       22.489772 ||
|[Mouse_g20_n2v_zeiss_median](experiments/Mouse_g20_n2v_zeiss_median)                | 28.586573 |       28.730031 |       29.087357 |       29.163176 ||
|[Mouse_sp12_n2v_zeiss_mean](experiments/Mouse_sp12_n2v_zeiss_mean)                  |  5.173321 |        5.267361 |       17.246261 |       17.239888 ||
|[Mouse_sp12_n2v_zeiss_median](experiments/Mouse_sp12_n2v_zeiss_median)              | 12.026396 |       12.195303 |       17.875640 |       17.893340 ||
|[Mouse_sp3_n2v_zeiss_mean](experiments/Mouse_sp3_n2v_zeiss_mean)                    |  6.409958 |        6.371194 |       17.184030 |       17.184748 ||
|[Mouse_sp3_n2v_zeiss_median](experiments/Mouse_sp3_n2v_zeiss_median)                | 17.675763 |       17.654012 |       20.401906 |       20.391773 ||
|[Mouse_sp6_n2v_zeiss_mean](experiments/Mouse_sp6_n2v_zeiss_mean)                    |  8.163826 |        8.158258 |       17.649973 |       17.634283 ||
|[Mouse_sp6_n2v_zeiss_median](experiments/Mouse_sp6_n2v_zeiss_median)                | 14.315774 |       14.317810 |       18.751745 |       18.755969 ||
|[Convallaria_n2v_zeiss_mean_bp_sk](experiments/Convallaria_n2v_zeiss_mean_bp_sk)    | 28.128531 |       29.489551 |       28.858988 |       29.578911 ||
|[Convallaria_n2v_zeiss_median_bp_sk](experiments/Convallaria_n2v_zeiss_median_bp_sk)| 28.320208 |       29.608477 |       28.657491 |       29.750094 ||
|[Flywing_g70_n2v_zeiss_mean_bp_sk](experiments/Flywing_g70_n2v_zeiss_mean_bp_sk)    | 25.361035 |       25.370307 |       25.427740 |       25.427188 ||
|[Flywing_g70_n2v_zeiss_median_bp_sk](experiments/Flywing_g70_n2v_zeiss_median_bp_sk)| 25.379543 |       25.484090 |       25.428994 |       25.545069 ||
|[Mouse_g20_n2v_zeiss_mean_bp_sk](experiments/Mouse_g20_n2v_zeiss_mean_bp_sk)        | 34.499746 |       34.509595 |       34.630219 |       34.688050 ||
|[Mouse_g20_n2v_zeiss_median_bp_sk](experiments/Mouse_g20_n2v_zeiss_median_bp_sk)    | 34.627272 |       34.502412 |       34.734864 |       34.722973 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk)      | 23.350323 |       23.256364 |       33.447390 |       33.706267 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk)  | 22.518748 |       22.939720 |       34.476900 |       34.482922 ||
|[Mouse_sp3_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp3_n2v_zeiss_mean_bp_sk)        | 30.590071 |       30.760299 |       35.618571 |       35.448269 ||
|[Mouse_sp3_n2v_zeiss_median_bp_sk](experiments/Mouse_sp3_n2v_zeiss_median_bp_sk)    | 30.902534 |       30.720023 |       35.763712 |       35.823552 ||
|[Mouse_sp6_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp6_n2v_zeiss_mean_bp_sk)        | 27.266872 |       27.649582 |       34.917322 |       34.953092 ||
|[Mouse_sp6_n2v_zeiss_median_bp_sk](experiments/Mouse_sp6_n2v_zeiss_median_bp_sk)    | 27.237407 |       27.434635 |       35.267758 |       35.489634 ||
