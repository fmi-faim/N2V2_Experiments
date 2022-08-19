# Experiments Overview

## BSD68
__Note:__ Shown PSNR values are computed with a fixed intensity range of 255.0.
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[BSD68_reproducibility_slurm](./experiments/BSD68_reproducibility_slurm/results_255_avg.csv)            |   27.57   |   27.69   | 27.61 | 27.70 | uniform_withCP |
|[BSD68_reproducibility_slurm-run1](./experiments/BSD68_reproducibility_slurm-run1/results_255_avg.csv)  |   27.67   |   27.72   | 27.71 | 27.72 | uniform_withCP |
|[BSD68_reproducibility_zeiss_baseline](experiments/BSD68_reproducibility_zeiss_baseline/results_255_avg.csv) |   27.39   |   27.67   | 27.44 | 27.67 | uniform_withCP | 
|[BSD68_reproducibility_slurm_mean_bp_sk](./experiments/BSD68_reproducibility_slurm_mean_bp_sk/results_255_avg.csv) | 27.56 | __28.32__ | __28.06__ | __28.34__ | mean |
|[BSD68_reproducibility_zeiss_mean_bp_sk](experiments/BSD68_reproducibility_zeiss_mean_bp_sk/results_255_avg.csv) |   27.72   |   28.29   | 27.88 | 28.31 | mean |
|[BSD68_sbp_slurm](./experiments/BSD68_sbp_slurm/results_255_avg.csv)                                    | __27.82__ | 28.03 | 27.89 | 28.04 | uniform_withCP |
|[BSD68_sbp_uniform_withoutCP_slurm](./experiments/BSD68_sbp_uniform_withoutCP_slurm/results_255_avg.csv)|   27.49   |   27.96   | 27.63 | 27.97 | uniform_withoutCP |
|[BSD68_uniform_withoutCP_slurm](./experiments/BSD68_uniform_withoutCP_slurm/results_255_avg.csv)        |   26.06   |   27.37   | 26.11 | 27.37 | uniform_withoutCP |
|[BSD68_bp_uwCP_slurm](./experiments/BSD68_bp_uwCP_slurm/results_255_avg.csv)                            |   27.43   |   27.69   | 27.51 | 27.69 | uniform_withCP |
|[BSD68_sk_uwCP_slurm](./experiments/BSD68_sk_uwCP_slurm/results_255_avg.csv)                            |   26.19   |   27.88   | 26.37 | 27.88 | uniform_withCP |
|[BSD68_reproducibility_zeiss_mean](experiments/BSD68_reproducibility_zeiss_mean/results_255_avg.csv) |   27.72   |  28.22   | 27.91 | 28.25 | mean |
|[BSD68_reproducibility_zeiss_median](experiments/BSD68_reproducibility_zeiss_median/results_255_avg.csv) |   27.40   |   27.49   | 27.45 | 27.49 | median |
|[BSD68_reproducibility_zeiss_median_bp_sk](experiments/BSD68_reproducibility_zeiss_median_bp_sk/results_255_avg.csv) |   27.69   |   28.31   | 27.80 | 28.32 | median |


## Convallaria
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_n2v_baseline_slurm](./experiments/Convallaria_n2v_baseline_slurm)                    |   35.56   |   35.56   |   35.58   |   35.58   | uniform_withoutCP |
|[Convallaria_n2v_zeiss_baseline](experiments/Convallaria_n2v_zeiss_baseline)                      |   35.73   |   35.73   |   35.75   |   35.76   | uniform_withoutCP |
|[Convallaria_n2v_sbp_slurm](./experiments/Convallaria_n2v_sbp_slurm)                              |   36.21   | __36.29__ |   36.25   |   36.31   | uniform_withoutCP |
|[Convallaria_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_n2v_sbp_uniform_withCP_slurm)|   36.18   |   36.24   |   36.20   |   36.26   | uniform_withCP |
|[Convallaria_n2v_uniform_withCP_slurm](./experiments/Convallaria_n2v_uniform_withCP_slurm)        |   35.85   |   35.87   |   35.86   |   35.89   | uniform_withCP |
|[Convallaria_n2v_zeiss_mean](experiments/Convallaria_n2v_zeiss_mean)                              |   35.57   |   35.57   |   36.00   |   35.90   | mean |
|[Convallaria_n2v_zeiss_median](experiments/Convallaria_n2v_zeiss_median)                          |   36.10   |   36.23   | __36.42__ | __36.39__ | median |
|[Convallaria_n2v_zeiss_mean_bp_sk](experiments/Convallaria_n2v_zeiss_mean_bp_sk)                  |   36.05   |   36.15   |   36.20   |   36.27   | mean |
|[Convallaria_n2v_zeiss_median_bp_sk](experiments/Convallaria_n2v_zeiss_median_bp_sk)              | __36.30__ |   36.25   |   36.34   |   36.36   | median |


## Convallaria_v1
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------| 
|[Convallaria_v1_n2v_baseline_slurm](./experiments/Convallaria_v1_n2v_baseline_slurm)                               |   31.09   |   31.22   |   31.27   |   31.24   | uniform_withoutCP |
|[Convallaria_v1_n2v_sbp_slurm](./experiments/Convallaria_v1_n2v_sbp_slurm)                                         |   29.00   | __31.47__ |   30.38   | __31.51__ | uniform_withoutCP |
|[Convallaria_v1_n2v_sbp_uniform_withCP_slurm](./experiments/Convallaria_v1_n2v_sbp_uniform_withCP_slurm)           |   27.36   |   31.43   |   29.66   |   31.45   | uniform_withCP |
|[Convallaria_v1_n2v_uniform_withCP_slurm](./experiments/Convallaria_v1_n2v_uniform_withCP_slurm)                   | __31.56__ |   31.41   | __31.85__ |   31.43   | uniform_withCP |
|[Convallaria_v1_slurm_mean_bp_sk](./experiments/Convallaria_v1_slurm_mean_bp_sk)                                   |   29.64   |   31.42   |   30.38   |   31.48   | mean |
|[Convallaria_v1_slurm_median_bp_sk](./experiments/Convallaria_v1_slurm_median_bp_sk)                               |   29.10   |   31.40   |   30.18   |   31.44   | median |
|[Convallaria_v1_n2v_zeiss_testontrain_baseline](experiments/Convallaria_v1_n2v_zeiss_testontrain_baseline)         |   30.22   |   30.50   |   30.39   |   30.52   | uniform_withoutCP |
|[Convallaria_v1_n2v_zeiss_testontrain_mean](experiments/Convallaria_v1_n2v_zeiss_testontrain_mean)                 |   30.52   |   31.18   |   31.16   |   31.37   | mean |
|[Convallaria_v1_n2v_zeiss_testontrain_mean_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testontrain_mean_bp_sk)     |   28.35   |   31.01   |   28.97   |   31.09   | mean |
|[Convallaria_v1_n2v_zeiss_testontrain_median](experiments/Convallaria_v1_n2v_zeiss_testontrain_median)             |   30.91   |   31.08   |   31.16   |   31.35   | median |
|[Convallaria_v1_n2v_zeiss_testontrain_median_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testontrain_median_bp_sk) |   30.44   |   31.01   |   30.73   |   31.06   | median |
|[Convallaria_v1_n2v_zeiss_testonval_baseline](experiments/Convallaria_v1_n2v_zeiss_testonval_baseline)             |   30.57   |   30.72   |   30.65   |   30.74   | uniform_withoutCP|
|[Convallaria_v1_n2v_zeiss_testonval_mean](experiments/Convallaria_v1_n2v_zeiss_testonval_mean)                     |   30.71   |   31.35   |   31.37   |   31.49   | mean |
|[Convallaria_v1_n2v_zeiss_testonval_mean_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testonval_mean_bp_sk)         |   28.90   |   31.16   |   29.52   |   31.22   | mean |
|[Convallaria_v1_n2v_zeiss_testonval_median](experiments/Convallaria_v1_n2v_zeiss_testonval_median)                 |   31.18   |   31.24   |   31.27   |   31.48   | median |
|[Convallaria_v1_n2v_zeiss_testonval_median_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testonval_median_bp_sk)     |   30.75   |   31.15   |   31.02   |   31.19   | median |



## Flywing
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Flywing_g70_n2v_baseline_slurm](./experiments/Flywing_g70_n2v_baseline_slurm)                    |   25.04   |   25.00   |   25.07   |   25.04   | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_identity_slurm](./experiments/Flywing_g70_n2v_sbp_identity_slurm)            |   11.23   |   11.23   |   17.68   |   17.68   | identity |
|[Flywing_g70_n2v_sbp_slurm](./experiments/Flywing_g70_n2v_sbp_slurm)                              |   25.44   |   25.45   |   25.47   |   25.49   | uniform_withoutCP |
|[Flywing_g70_n2v_sbp_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_sbp_uniform_withCP_slurm)|   25.38   |   25.38   |   25.41   |   25.42   | uniform_withCP |
|[Flywing_g70_n2v_uniform_withCP_slurm](./experiments/Flywing_g70_n2v_uniform_withCP_slurm)        |   25.16   |   25.17   |   25.19   |   25.20   | uniform_withCP |
|[Flywing_g70_n2v_bp_uwCP_slurm](./experiments/Flywing_g70_n2v_bp_uwCP_slurm)                      |   25.09   |   25.27   |   25.14   |   25.30   | uniform_withCP |
|[Flywing_g70_n2v_sk_uwCP_slurm](./experiments/Flywing_g70_n2v_sk_uwCP_slurm)                      |   25.41   |   25.45   |   25.46   |   25.49   | uniform_withCP |
|[Flywing_g70_n2v_zeiss_baseline](experiments/Flywing_g70_n2v_zeiss_baseline)                      |   25.13   |   25.21   |   25.16   |   25.24   | uniform_withoutCP |
|[Flywing_g70_n2v_zeiss_mean](experiments/Flywing_g70_n2v_zeiss_mean)                              |   25.44   |   25.45   |   25.50   |   25.54   | mean |
|[Flywing_g70_n2v_zeiss_mean_bp_sk](experiments/Flywing_g70_n2v_zeiss_mean_bp_sk)                  |   25.40   |   25.44   |   25.46   |   25.48   | mean |
|[Flywing_g70_n2v_zeiss_median](experiments/Flywing_g70_n2v_zeiss_median)                          | __25.49__ | __25.50__ | __25.57__ | __25.57__ | meadian |
|[Flywing_g70_n2v_zeiss_median_bp_sk](experiments/Flywing_g70_n2v_zeiss_median_bp_sk)              |   25.41   |   25.41   |   25.46   |   25.46   | median |


## Mouse_g20
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_g20_n2v_baseline_slurm](./experiments/Mouse_g20_n2v_baseline_slurm)                    |   33.91   |   33.93   |   33.93   |   33.94   | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_slurm](./experiments/Mouse_g20_n2v_sbp_slurm)                              |   34.52   |   34.57   |   34.55   |   34.59   | uniform_withoutCP |
|[Mouse_g20_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_sbp_uniform_withCP_slurm)| __34.64__ |   34.63   | __34.64__ |   34.65   | uniform_withCP |
|[Mouse_g20_n2v_uniform_withCP_slurm](./experiments/Mouse_g20_n2v_uniform_withCP_slurm)        |   34.03   |   34.11   |   34.06   |   34.12   | uniform_withCP |
|[Mouse_g20_n2v_bp_uwCP_slurm](./experiments/Mouse_g20_n2v_bp_uwCP_slurm)                      |   34.18   |   34.16   |   34.20   |   34.17   | uniform_withCP |
|[Mouse_g20_n2v_sk_uwCP_slurm](./experiments/Mouse_g20_n2v_sk_uwCP_slurm)                      |   34.57   |   34.61   |   34.59   |   34.63   | uniform_withCP |
|[Mouse_g20_n2v_zeiss_baseline](experiments/Mouse_g20_n2v_zeiss_baseline)                      |   34.17   |   34.18   |   34.17   |   34.20   | uniform_withoutCP |
|[Mouse_g20_n2v_zeiss_mean](experiments/Mouse_g20_n2v_zeiss_mean)                              |   33.92   |   34.39   |   34.41   |   34.49   | mean |
|[Mouse_g20_n2v_zeiss_mean_bp_sk](experiments/Mouse_g20_n2v_zeiss_mean_bp_sk)                  |   34.32   |   34.49   |   34.50   |   34.61   | mean |
|[Mouse_g20_n2v_zeiss_median](experiments/Mouse_g20_n2v_zeiss_median)                          |   34.27   |   34.26   |   34.41   |   34.41   | median |
|[Mouse_g20_n2v_zeiss_median_bp_sk](experiments/Mouse_g20_n2v_zeiss_median_bp_sk)              |   34.20   | __34.64__ |   34.41   | __34.74__ | median |


## Mouse_sp12
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp12_n2v_baseline_slurm](./experiments/Mouse_sp12_n2v_baseline_slurm)                       |   22.91   |   22.96   |   33.45   |   33.49   | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_slurm](./experiments/Mouse_sp12_n2v_sbp_slurm)                                 |   22.99   |   23.07   |   34.36   |   34.52   | uniform_withoutCP |
|[Mouse_sp12_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_sbp_uniform_withCP_slurm)   |   22.90   |   22.99   |   34.10   |   34.19   | uniform_withCP |
|[Mouse_sp12_n2v_uniform_withCP_slurm](./experiments/Mouse_sp12_n2v_uniform_withCP_slurm)           |   18.02   |   17.99   |   21.00   |   20.99   | uniform_withCP |
|[Mouse_sp12_n2v_zeiss_baseline](experiments/Mouse_sp12_n2v_zeiss_baseline)                         |   23.20   |   22.98   |   33.83   |   34.12   | uniform_withoutCP |
|[Mouse_sp12_n2v_zeiss_baseline_shallow](experiments/Mouse_sp12_n2v_zeiss_baseline_shallow)         |   23.01   |   23.05   |   33.97   |   34.01   | uniform_withoutCP |
|[Mouse_sp12_n2v_zeiss_mean](experiments/Mouse_sp12_n2v_zeiss_mean)                                 | __23.68__ | __23.25__ |   33.87   |   33.66   | mean |
|[Mouse_sp12_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk)                     |   22.52   |   23.18   |   32.91   |   34.17   | mean |
|[Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_bp_sk_shallow)     |   23.17   |   23.22   |   33.91   |   33.90   | mean |
|[Mouse_sp12_n2v_zeiss_mean_shallow](experiments/Mouse_sp12_n2v_zeiss_mean_shallow)                 |   23.30   |   23.21   |   33.12   |   33.26   | mean |
|[Mouse_sp12_n2v_zeiss_median](experiments/Mouse_sp12_n2v_zeiss_median)                             |   23.02   |   22.92   |   33.57   |   33.45   | median |
|[Mouse_sp12_n2v_zeiss_median_bp_sk](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk)                 |   23.47   |   23.00   | __34.39__ | __34.54__ | median |
|[Mouse_sp12_n2v_zeiss_median_bp_sk_shallow](experiments/Mouse_sp12_n2v_zeiss_median_bp_sk_shallow) |   23.34   |   22.98   |   33.82   |   33.88   | median |
|[Mouse_sp12_n2v_zeiss_median_shallow](experiments/Mouse_sp12_n2v_zeiss_median_shallow)             |   22.88   |   22.88   |   32.99   |   32.98   | median |


## Mouse_sp3
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp3_n2v_baseline_slurm](./experiments/Mouse_sp3_n2v_baseline_slurm)                    |   30.33   |   30.60   |   34.94   |   35.17   | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_slurm](./experiments/Mouse_sp3_n2v_sbp_slurm)                              |   30.51   |   30.66   |   35.63   | __35.91__ | uniform_withoutCP |
|[Mouse_sp3_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_sbp_uniform_withCP_slurm)|   30.61   |   30.71   | __35.64__ |   35.74   | uniform_withCP |
|[Mouse_sp3_n2v_uniform_withCP_slurm](./experiments/Mouse_sp3_n2v_uniform_withCP_slurm)        |   19.83   |   19.23   |   21.79   |   21.32   | uniform_withCP |
|[Mouse_sp3_n2v_zeiss_baseline](experiments/Mouse_sp3_n2v_zeiss_baseline)                      |   30.44   |   30.63   |   35.38   |   35.44   | uniform_withoutCP |
|[Mouse_sp3_n2v_zeiss_mean](experiments/Mouse_sp3_n2v_zeiss_mean)                              |   30.75   |   30.66   |   35.27   |   35.29   | mean |
|[Mouse_sp3_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp3_n2v_zeiss_mean_bp_sk)                  | __31.12__ | __30.81__ |   35.00   |   35.51   | mean |
|[Mouse_sp3_n2v_zeiss_median](experiments/Mouse_sp3_n2v_zeiss_median)                          |   30.47   |   30.39   |   35.25   |   35.23   | median |
|[Mouse_sp3_n2v_zeiss_median_bp_sk](experiments/Mouse_sp3_n2v_zeiss_median_bp_sk)              |   29.68   |   30.75   |   35.07   |   35.81   | median |


## Mouse_sp6
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Mouse_sp6_n2v_baseline_slurm](./experiments/Mouse_sp6_n2v_baseline_slurm)                    |   26.95   |   27.27   |   34.05   |   34.24   | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_slurm](./experiments/Mouse_sp6_n2v_sbp_slurm)                              |   27.48   |   27.50   |   35.43   |   35.47   | uniform_withoutCP |
|[Mouse_sp6_n2v_sbp_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_sbp_uniform_withCP_slurm)|   27.32   |   27.48   |   34.96   |   35.32   | uniform_withCP |
|[Mouse_sp6_n2v_uniform_withCP_slurm](./experiments/Mouse_sp6_n2v_uniform_withCP_slurm)        |   18.16   |   18.13   |   20.76   |   20.69   | uniform_withCP |
|[Mouse_sp6_n2v_zeiss_baseline](experiments/Mouse_sp6_n2v_zeiss_baseline)                      |   27.54   |   27.41   |   34.81   |   34.89   | uniform_withoutCP |
|[Mouse_sp6_n2v_zeiss_mean](experiments/Mouse_sp6_n2v_zeiss_mean)                              |   27.45   |   27.50   |   34.63   |   34.71   | mean |
|[Mouse_sp6_n2v_zeiss_mean_bp_sk](experiments/Mouse_sp6_n2v_zeiss_mean_bp_sk)                  | __27.90__ | __27.58__ |   34.89   |   35.01   | mean |
|[Mouse_sp6_n2v_zeiss_median](experiments/Mouse_sp6_n2v_zeiss_median)                          |   26.81   |   27.36   |   34.86   |   35.07   | median |
|[Mouse_sp6_n2v_zeiss_median_bp_sk](experiments/Mouse_sp6_n2v_zeiss_median_bp_sk)              |   27.35   |   27.53   | __35.48__ | __35.50__ | median |


## Results `Convallaria_v1_n2v_zeiss` test on `train`
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Convallaria_v1_n2v_zeiss_testontrain_baseline](experiments/Convallaria_v1_n2v_zeiss_testontrain_baseline)         |   30.22   |   30.50   |   30.39   |   30.52   | uniform_withoutCP |
|[Convallaria_v1_n2v_zeiss_testontrain_mean](experiments/Convallaria_v1_n2v_zeiss_testontrain_mean)                 |   30.52   | __31.18__ | __31.16__ | __31.37__ | mean |
|[Convallaria_v1_n2v_zeiss_testontrain_mean_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testontrain_mean_bp_sk)     |   28.35   |   31.01   |   28.97   |   31.09   | mean |
|[Convallaria_v1_n2v_zeiss_testontrain_median](experiments/Convallaria_v1_n2v_zeiss_testontrain_median)             | __30.91__ |   31.08   | __31.16__ | __31.35__ | median |
|[Convallaria_v1_n2v_zeiss_testontrain_median_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testontrain_median_bp_sk) |   30.44   |   31.01   |   30.73   |   31.06   | median |


## Results `Convallaria_v1_n2v_zeiss` test on `val`
| Name | PSNR_wbest | PSNR_wlast | bestPSNR_wbest | bestPSNR_wlast | Replacement |
|------|------------|------------|----------------|----------------|-------------|
|[Convallaria_v1_n2v_zeiss_testonval_baseline](experiments/Convallaria_v1_n2v_zeiss_testonval_baseline)             |   30.57   |   30.72   |   30.65   |   30.74   | uniform_withoutCP |
|[Convallaria_v1_n2v_zeiss_testonval_mean](experiments/Convallaria_v1_n2v_zeiss_testonval_mean)                     |   30.71   | __31.35__ | __31.37__ | __31.49__ | mean |
|[Convallaria_v1_n2v_zeiss_testonval_mean_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testonval_mean_bp_sk)         |   28.90   |   31.16   |   29.52   |   31.22   | mean |
|[Convallaria_v1_n2v_zeiss_testonval_median](experiments/Convallaria_v1_n2v_zeiss_testonval_median)                 | __31.18__ |   31.24   |   31.27   |   31.48   | median |
|[Convallaria_v1_n2v_zeiss_testonval_median_bp_sk](experiments/Convallaria_v1_n2v_zeiss_testonval_median_bp_sk)     |   30.75   |   31.15   |   31.02   |   31.19   | median |
