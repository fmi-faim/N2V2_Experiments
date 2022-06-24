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
|[Convallaria_n2v_zeiss_mean_bp_sk](experiments/Convallaria_n2v_zeiss_mean_bp_sk)    | 20.853632 |       19.941455 |       23.890234 |       23.700333 ||
|[Convallaria_n2v_zeiss_median](experiments/Convallaria_n2v_zeiss_median)            | 27.442528 |       27.872378 |       28.409888 |       28.890761 ||
|[Convallaria_n2v_zeiss_median_bp_sk](experiments/Convallaria_n2v_zeiss_median_bp_sk)| 21.040318 |       20.250296 |       24.445709 |       24.140433 ||
|[Flywing_g70_n2v_zeiss_mean](experiments/Flywing_g70_n2v_zeiss_mean)                |  9.964426 |        9.307624 |       17.739788 |       17.652367 ||
|[Flywing_g70_n2v_zeiss_mean_bp_sk](experiments/Flywing_g70_n2v_zeiss_mean_bp_sk)    | 10.926513 |       10.922209 |       17.973673 |       17.973473 ||
|[Flywing_g70_n2v_zeiss_median](experiments/Flywing_g70_n2v_zeiss_median)            | 15.843161 |       15.865043 |       19.422810 |       19.435305 ||
|[Flywing_g70_n2v_zeiss_median_bp_sk](experiments/Flywing_g70_n2v_zeiss_median_bp_sk)| 11.006944 |       11.016245 |       17.989104 |       17.986946 ||
|[Mouse_g20_n2v_zeiss_mean](experiments/Mouse_g20_n2v_zeiss_mean)                    | 20.209486 |       20.184326 |       22.476917 |       22.489772 ||
|[Mouse_g20_n2v_zeiss_mean_bp_sk](experiments/Mouse_g20_n2v_zeiss_mean_bp_sk)        | 20.155270 |       20.137941 |       22.591400 |       22.610804 ||
|[Mouse_g20_n2v_zeiss_median](experiments/Mouse_g20_n2v_zeiss_median)                | 28.586573 |       28.730031 |       29.087357 |       29.163176 ||
|[Mouse_g20_n2v_zeiss_median_bp_sk](experiments/Mouse_g20_n2v_zeiss_median_bp_sk)    | 20.447580 |       20.424719 |       22.789787 |       22.781220 ||
|[Mouse_sp12_n2v_zeiss_mean](experiments/Mouse_sp12_n2v_zeiss_mean)                  |  5.173321 |        5.267361 |       17.246261 |       17.239888 ||
|[Mouse_sp12_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk)      | 11.457333 |       11.461465 |       17.927168 |       17.941535 ||
|[Mouse_sp12_n2v_zeiss_median](experiments/Mouse_sp12_n2v_zeiss_median)              | 12.026396 |       12.195303 |       17.875640 |       17.893340 ||
|[Mouse_sp12_n2v_zeiss_median_bp_sk](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk)  | 10.770723 |       10.685784 |       17.654749 |       17.651881 ||
|[Mouse_sp3_n2v_zeiss_mean](experiments/Mouse_sp3_n2v_zeiss_mean)                    |  6.409958 |        6.371194 |       17.184030 |       17.184748 ||
|[Mouse_sp3_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp3_n2v_zeiss_mean_bp_sk)        | 16.927828 |       16.932631 |       20.356923 |       20.336592 ||
|[Mouse_sp3_n2v_zeiss_median](experiments/Mouse_sp3_n2v_zeiss_median)                | 17.675763 |       17.654012 |       20.401906 |       20.391773 ||
|[Mouse_sp3_n2v_zeiss_median_bp_sk](experiments/Mouse_sp3_n2v_zeiss_median_bp_sk)    | 16.657223 |       16.642204 |       20.141004 |       20.133595 ||
|[Mouse_sp6_n2v_zeiss_mean](experiments/Mouse_sp6_n2v_zeiss_mean)                    |  8.163826 |        8.158258 |       17.649973 |       17.634283 ||
|[Mouse_sp6_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp6_n2v_zeiss_mean_bp_sk)        | 14.263220 |       14.257066 |       18.995556 |       18.986233 ||
|[Mouse_sp6_n2v_zeiss_median](experiments/Mouse_sp6_n2v_zeiss_median)                | 14.315774 |       14.317810 |       18.751745 |       18.755969 ||
|[Mouse_sp6_n2v_zeiss_median_bp_sk](experiments/Mouse_sp6_n2v_zeiss_median_bp_sk)    | 13.770606 |       13.810281 |       18.707837 |       18.745050 ||
