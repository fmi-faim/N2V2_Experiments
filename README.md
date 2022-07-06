# Experiments Overview

## BSD68
__Note:__ Shown PSNR values are computed with a fixed intensity range of 255.0.
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_slurm](./experiments/BSD68_reproducibility_slurm/results_255_avg.csv)            |   27.57   |   27.69   | 27.61 | 27.70 | uniform_withCP |
|[BSD68_reproducibility_slurm-run1](./experiments/BSD68_reproducibility_slurm-run1/results_255_avg.csv)  |   27.67   |   27.72   | 27.71 | 27.72 | uniform_withCP | 
|[BSD68_reproducibility_slurm_mean_bp_sk](./experiments/BSD68_reproducibility_slurm_mean_bp_sk/results_255_avg.csv) | 27.56 | __28.32__ | __28.06__ | __28.34__ | mean |
|[BSD68_sbp_slurm](./experiments/BSD68_sbp_slurm/results_255_avg.csv)                                    | __27.82__ | 28.03 | 27.89 | 28.04 | uniform_withCP |
|[BSD68_sbp_uniform_withoutCP_slurm](./experiments/BSD68_sbp_uniform_withoutCP_slurm/results_255_avg.csv)|   27.49   |   27.96   | 27.63 | 27.97 | uniform_withoutCP |
|[BSD68_uniform_withoutCP_slurm](./experiments/BSD68_uniform_withoutCP_slurm/results_255_avg.csv)        |   26.06   |   27.37   | 26.11 | 27.37 | uniform_withoutCP |


## Convallaria
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_n2v_baseline_slurm](./experiments/Convallaria_n2v_baseline_slurm)                    | 35.56 | 35.56 | 35.58 | 35.58 | uniform_withoutCP |
|[Convallaria_n2v_sbp_slurm](./experiments/Convallaria_n2v_sbp_slurm)                              | __36.21__ | __36.29__ | __36.25__ | __36.31__ | uniform_withoutCP |
|[Convallaria_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_n2v_sbp_uniform_withCP_slurm)| 36.18 | 36.24 | 36.20 | 36.26 | uniform_withCP |
|[Convallaria_n2v_uniform_withCP_slurm](./experiments/Convallaria_n2v_uniform_withCP_slurm)        | 35.85 | 35.87 | 35.86 | 35.89 | uniform_withCP |


## Convallaria_v1
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_v1_n2v_baseline_slurm](./experiments/Convallaria_v1_n2v_baseline_slurm)                    | 31.09 | 31.22 | 31.27 | 31.24 | uniform_withoutCP |
|[Convallaria_v1_n2v_sbp_slurm](./experiments/Convallaria_v1_n2v_sbp_slurm)                              | 29.00 | __31.47__ | 30.38 | __31.51__ | uniform_withoutCP |
|[Convallaria_v1_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_v1_n2v_sbp_uniform_withCP_slurm)| 27.36 | 31.43 | 29.66 | 31.45 | uniform_withCP |
|[Convallaria_v1_n2v_uniform_withCP_slurm](./experiments/Convallaria_v1_n2v_uniform_withCP_slurm)        | __31.56__ | 31.41 | __31.85__ | 31.43 | uniform_withCP |
|[Convallaria_v1_slurm_mean_bp_sk](./experiments/Convallaria_v1_slurm_mean_bp_sk)                        | 29.64 | 31.42 | 30.38 | 31.48 | mean |
|[Convallaria_v1_slurm_median_bp_sk](./experiments/Convallaria_v1_slurm_median_bp_sk)                    | 29.10 | 31.40 | 30.18 | 31.44 | median |


## Flywing
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Flywing_g70_n2v_baseline_slurm](./experiments/Flywing_g70_n2v_baseline_slurm)                    | 25.04 | 25.00 | 25.07 | 25.04 | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_identity_slurm](./experiments/Flywing_g70_n2v_sbp_identity_slurm)            | 11.23 | 11.23 | 17.68 | 17.68 | identity |
|[Flywing_g70_n2v_sbp_slurm](./experiments/Flywing_g70_n2v_sbp_slurm)                              | __25.44__ | __25.45__ | __25.47__ | __25.49__ | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_sbp_uniform_withCP_slurm)| 25.38 | 25.38 | 25.41 | 25.42 | uniform_withCP |
|[Flywing_g70_n2v_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_uniform_withCP_slurm)        | 25.16 | 25.17 | 25.19 | 25.20 | uniform_withCP |


## Mouse_g20
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_g20_n2v_baseline_slurm](./experiments/Mouse_g20_n2v_baseline_slurm)                    | 33.91 | 33.93 | 33.93 | 33.94 | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_slurm](./experiments/Mouse_g20_n2v_sbp_slurm)                              | 34.52 | 34.57 | 34.55 | 34.59 | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_sbp_uniform_withCP_slurm)| __34.64__ | __34.63__ | __34.64__ | __34.65__ | uniform_withCP |
|[Mouse_g20_n2v_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_uniform_withCP_slurm)        | 34.03 | 34.11 | 34.06 | 34.12 | uniform_withCP |


## Mouse_sp12
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp12_n2v_baseline_slurm](./experiments/Mouse_sp12_n2v_baseline_slurm)                    | 22.91 | 22.96 | 33.45 | 33.49 | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_slurm](./experiments/Mouse_sp12_n2v_sbp_slurm)                              | __22.99__ | __23.07__ | __34.36__ | __34.52__ | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_sbp_uniform_withCP_slurm)| 22.90 | 22.99 | 34.10 | 34.19 | uniform_withCP |
|[Mouse_sp12_n2v_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_uniform_withCP_slurm)        | 18.02 | 17.99 | 21.00 | 20.99 | uniform_withCP |


## Mouse_sp3
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp3_n2v_baseline_slurm](./experiments/Mouse_sp3_n2v_baseline_slurm)                    | 30.33 | 30.60 | 34.94 | 35.17 | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_slurm](./experiments/Mouse_sp3_n2v_sbp_slurm)                              | 30.51 | 30.66 | 35.63 | __35.91__ | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_sbp_uniform_withCP_slurm)| __30.61__ | __30.71__ | __35.64__ | 35.74 | uniform_withCP |
|[Mouse_sp3_n2v_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_uniform_withCP_slurm)        | 19.83 | 19.23 | 21.79 | 21.32 | uniform_withCP |

## Mouse_sp6
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp6_n2v_baseline_slurm](./experiments/Mouse_sp6_n2v_baseline_slurm)                    | 26.95 | 27.27 | 34.05 | 34.24 | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_slurm](./experiments/Mouse_sp6_n2v_sbp_slurm)                              | __27.48__ | __27.50__ | __35.43__ | __35.47__ | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_sbp_uniform_withCP_slurm)| 27.32 | 27.48 | 34.96 | 35.32 | uniform_withCP |
|[Mouse_sp6_n2v_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_uniform_withCP_slurm)        | 18.16 | 18.13 | 20.76 | 20.69 | uniform_withCP |
