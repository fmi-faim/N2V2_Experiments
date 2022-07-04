# Experiments Overview

## BSD68
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_slurm](./experiments/BSD68_reproducibility_slurm)            |   26.84   |   26.97   | 26.88 | 26.97 | uniform_withCP |
|[BSD68_reproducibility_slurm-run1](./experiments/BSD68_reproducibility_slurm-run1)  |   26.95   |   26.99   | 26.99 | 27.00 | uniform_withCP | 
|[BSD68_reproducibility_slurm_mean_bp_sk](./experiments/BSD68_reproducibility_slurm_mean_bp_sk) | __26.83__ | __27.59__ | __27.34__ | __27.61__ | mean |
|[BSD68_sbp_slurm](./experiments/BSD68_sbp_slurm)                                    | 27.09 | 27.30 | 27.16 | 27.31 | uniform_withCP |
|[BSD68_sbp_uniform_withoutCP_slurm](./experiments/BSD68_sbp_uniform_withoutCP_slurm)|   26.76   |   27.24   | 26.90 | 27.25 | uniform_withoutCP |
|[BSD68_uniform_withoutCP_slurm](./experiments/BSD68_uniform_withoutCP_slurm)        |   25.33   |   26.64   | 25.39 | 26.64 | uniform_withoutCP |


## Convallaria
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_n2v_baseline_slurm](./experiments/Convallaria_n2v_baseline_slurm)                    | 35.56 | 35.56 | 35.58 | 35.58 | uniform_withoutCP |
|[Convallaria_n2v_sbp_slurm](./experiments/Convallaria_n2v_sbp_slurm)                              | __36.21__ | __36.29__ | __36.25__ | __36.31__ | uniform_withoutCP |
|[Convallaria_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_n2v_sbp_uniform_withCP_slurm)| 36.18 | 36.24 | 36.20 | 36.26 | uniform_withCP |
|[Convallaria_n2v_uniform_withCP_slurm](./experiments/Convallaria_n2v_uniform_withCP_slurm)        | 35.85 | 35.87 | 35.86 | 35.89 | uniform_withCP |


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
