# Invoice Data Analytics
**Mahmoud Abusahyoun | Data Analytics final project, HTU**

Three related notebooks demonstrate descriptive, predictive and prescriptive analytics for an invoice-processing scenario.

| Notebook | Content | Reproducibility |
|---|---|---|
| `descriptive.ipynb` | Frequency, central tendency, dispersion and charts | Archived original outputs; source workbook missing |
| `predictive.ipynb` | Moving averages, smoothing, regression, feature selection, RNN/LSTM | Archived original outputs; source workbook missing |
| `prescriptive.ipynb` | Branch allocation with SciPy linear programming and PyGAD | Corrected and rerun; self-contained |

## Missing source data
The first two notebooks require `invoices - updated.xlsx`, which was absent from the supplied files and was not recovered by a filename search. Their saved outputs contain summaries, not a complete recoverable workbook. No replacement or fabricated invoice dataset has been used. These two notebooks preserve original code and outputs with a prominent archive notice and have not been rerun or validated.

The predictive notebook includes exploratory limitations: encoding before splitting, repeated method comparisons on a shared test set, and ANN validation preprocessing fitted to a larger training set. Feature availability at prediction time and time ordering also require review against the workbook. Its original metrics should not be represented as corrected or production-ready.

## Prescriptive model
Allocate a workload of 5,000 **processing operations including rework** across Amman, Irbid and Aqaba, minimizing assumed costs while respecting capacities and an accuracy-related allocation constraint. This preserves the original equality `A + I + 1.10Q = 5000`. If the business requirement is 5,000 distinct invoices, the equality must instead be reformulated; this notebook makes no claim to solve that different scenario.

The linear program obtains a minimum cost of **2,340.00 JOD**. The seeded genetic algorithm obtains **2,340.90 JOD**, a **0.90 JOD** optimality gap. Assumptions are specified directly in code; the missing workbook is not needed for this notebook. Upper-bound sampling was corrected so PyGAD can reach the allowed capacities.

Use Python 3.12, install `requirements.txt`, then open `prescriptive.ipynb` from this folder. Results and an execution log are included in `results/`. The original descriptive/predictive notebooks require the workbook in the working directory before they can be run; their code is retained unchanged.
