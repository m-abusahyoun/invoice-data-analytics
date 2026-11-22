# Invoice Data Analytics
**Mahmoud Abusahyoun | Data Analytics final project, HTU**

Three related notebooks cover descriptive, predictive and prescriptive analytics. All three are executed with saved outputs; no local rerun is needed to review the results.

| Notebook | Contents |
|---|---|
| `descriptive.ipynb` | Full-dataset statistics, distributions and comparisons |
| `predictive.ipynb` | Daily smoothing, feature selection, linear/tree regression, RNN and LSTM |
| `prescriptive.ipynb` | Linear programming and a genetic algorithm for branch allocation |

## Data included
The supplied `invoices - updated.xlsx` contains **532,057 rows and 12 columns**. The author identified it as public/synthetic Kaggle data and authorized publication. The exact Kaggle listing and license were not supplied and are not invented here.

- `data/invoices_model_data.csv.gz` retains **every row** and the eight columns required by the notebooks. Four identifying columns are excluded from this analytical view.
- `data/workbook_parts/` preserves every byte of the complete original workbook, including all twelve columns. It is split only because the original workbook exceeds the browser's single-file upload limit.
- Run `python restore_workbook.py` from this folder to reconstruct `invoices - updated.xlsx`. The script verifies each part and the complete workbook with SHA-256 before saving it. Python's standard library is sufficient.
- The notebooks read the compressed analytical CSV directly; restoration of the Excel workbook is optional for running the analysis. No external download is required.

## Run
Use Python 3.12, install `requirements.txt`, and open the notebooks with this repository as the working directory. TensorFlow runs on CPU. `artifacts/` includes the selected regressor, trained RNN/LSTM and fitted sequence preprocessing. `results/` includes statistics, validation comparisons, held-out metrics, training histories, split details and the execution log.

## Rerun results
| Model | Evaluation partition | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Tree_Forward | random_test | 295.04 | 414.91 | 0.9794 |
| Training_mean | random_test | 1068.14 | 2893.71 | -0.0000 |
| RNN | chronological_test | 1076.17 | 3098.07 | -0.0008 |
| LSTM | chronological_test | 1083.47 | 3097.16 | -0.0002 |
| Fitting_mean | chronological_test | 1084.32 | 3097.14 | -0.0002 |

Random and chronological test partitions differ, so those model families should not be ranked directly against one another. Linear/tree experiments select features using fitting data and choose a method on validation data before final testing. The neural experiments use 70%/10%/20% chronological row boundaries and ten preceding invoice feature rows; the fitting partition alone determines encoders and feature/target scaling. They use at most 30 epochs with validation early stopping. Weak sequence results are retained and compared with a mean baseline.

## Interpretation and limits
`days_overdue` may only be available after issuance, so the regression is retrospective unless the operational timing of features is established. Ordered invoice records belong to different invoices; the sequence experiments do not establish customer-level or entity-level forecasting ability. Smoothing curves are descriptive, not held-out forecasts. The currency is not established by the workbook. Historical coursework previously inspected test outputs, so these reruns are not independent external validation.

The descriptive plots now match pie labels to their count order, describe right skew correctly, and aggregate category bars. Only a seeded scatter-plot display sample is used; statistical summaries and model partitions retain all rows. The original neural target-indexing problem is corrected.

## Prescriptive assumptions
The allocation model retains the original equality `A + I + 1.10Q = 5000`: it allocates **5,000 processing operations including rework**, not 5,000 distinct invoices. Its costs and capacities are stipulated assumptions, not estimates learned from the invoice workbook. The exact LP minimum is 2,340.00 JOD; the seeded genetic algorithm's recorded result and gap are in `results/prescriptive_results.json`.

## Original coursework
The three exact original notebooks are preserved in the separate complete project backup. They retain their original code and outputs; the current repository contains the corrected rerun edition.
