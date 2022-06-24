# Experiments Overview

## BSD68
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_slurm](./experiments/BSD68_reproducibility_slurm)            |   26.76   |   27.00   | 26.86 | 27.00 | uniform_withCP |
|[BSD68_reproducibility_slurm-run1](./experiments/BSD68_reproducibility_slurm-run1)  |   26.24   |   26.99   | 26.57 | 26.99 | uniform_withCP | 
|[BSD68_sbp_slurm](./experiments/BSD68_sbp_slurm)                                    | __27.07__ | __27.29__ | __27.19__ | __27.30__ | uniform_withCP |
|[BSD68_sbp_uniform_withoutCP_slurm](./experiments/BSD68_sbp_uniform_withoutCP_slurm)|   26.66   |   27.21   | 26.91 | 27.22 | uniform_withoutCP |
|[BSD68_uniform_withoutCP_slurm](./experiments/BSD68_uniform_withoutCP_slurm)        |   26.47   |   26.74   | 26.62 | 26.74 | uniform_withoutCP |


## Convallaria
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_n2v_baseline_slurm](./experiments/Convallaria_n2v_baseline_slurm)                    | 35.40 | 35.55 | 35.43 | 35.57 | uniform_withoutCP |
|[Convallaria_n2v_sbp_slurm](./experiments/Convallaria_n2v_sbp_slurm)                              | 36.15 | 36.15 | 36.17 | 36.17 | uniform_withoutCP |
|[Convallaria_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_n2v_sbp_uniform_withCP_slurm)| __36.19__ | __36.27__ | __36.21__ | __36.29__ | uniform_withCP |
|[Convallaria_n2v_uniform_withCP_slurm](./experiments/Convallaria_n2v_uniform_withCP_slurm)        | 35.86 | 35.85 | 35.89 | 35.88 | uniform_withCP |


## Flywing
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Flywing_g70_n2v_baseline_slurm](./experiments/Flywing_g70_n2v_baseline_slurm)                    | 24.96 | 24.98 | 24.99 | 25.02 | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_slurm](./experiments/Flywing_g70_n2v_sbp_slurm)                              | __25.43__ | __25.44__ | __25.47__ | __25.47__ | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_sbp_uniform_withCP_slurm)| 25.38 | __25.44__ | 25.41 | __25.47__ | uniform_withCP |
|[Flywing_g70_n2v_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_uniform_withCP_slurm)        | 25.20 | 25.22 | 25.25 | 25.26 | uniform_withCP |


## Mouse_g20
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_g20_n2v_baseline_slurm](./experiments/Mouse_g20_n2v_baseline_slurm)                    | 33.88 | 33.90 | 33.90 | 33.90 | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_slurm](./experiments/Mouse_g20_n2v_sbp_slurm)                              | 34.44 | 34.63 | 34.52 | 34.64 | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_sbp_uniform_withCP_slurm)| __34.65__ | __34.66__ | __34.66__ | __34.68__ | uniform_withCP |
|[Mouse_g20_n2v_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_uniform_withCP_slurm)        | 34.03 | 34.04 | 34.04 | 34.05 | uniform_withCP |


## Mouse_sp12
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp12_n2v_baseline_slurm](./experiments/Mouse_sp12_n2v_baseline_slurm)                    | 22.96 | 22.95 | 32.66 | 33.42 | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_slurm](./experiments/Mouse_sp12_n2v_sbp_slurm)                              | __23.11__ | 22.95 | __34.47__ | __34.66__ | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_sbp_uniform_withCP_slurm)| 23.10 | __23.03__ | 34.37 | 34.35 | uniform_withCP |
|[Mouse_sp12_n2v_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_uniform_withCP_slurm)        | 20.11 | 20.43 | 23.82 | 24.04 | uniform_withCP |


## Mouse_sp3
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp3_n2v_baseline_slurm](./experiments/Mouse_sp3_n2v_baseline_slurm)                    | 30.31 | 30.42 | 34.65 | 34.75 | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_slurm](./experiments/Mouse_sp3_n2v_sbp_slurm)                              | 30.78 | __30.77__ | 35.24 | __35.91__ | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_sbp_uniform_withCP_slurm)| __31.06__ | 30.76 | __35.76__ | 35.83 | uniform_withCP |
|[Mouse_sp3_n2v_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_uniform_withCP_slurm)        | 19.43 | 19.42 | 21.44 | 21.43 | uniform_withCP |

## Mouse_sp6
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp6_n2v_baseline_slurm](./experiments/Mouse_sp6_n2v_baseline_slurm)                    | 27.27 | 27.25 | 34.38 | 34.42 | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_slurm](./experiments/Mouse_sp6_n2v_sbp_slurm)                              | 27.43 | 27.34 | __35.46__ | __35.58__ | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_sbp_uniform_withCP_slurm)| __27.51__ | __27.46__ | 35.20 | 35.24 | uniform_withCP |
|[Mouse_sp6_n2v_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_uniform_withCP_slurm)        | 18.20 | 18.20 | 20.68 | 20.73 | uniform_withCP |
