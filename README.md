# 💳 Credit Risk Score

<p align="center">
  <strong>Exploring binary classification models for German credit-risk data</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-In%20Progress-blue" alt="Project in progress">
  <img src="https://img.shields.io/badge/Task-Binary%20Classification-purple" alt="Binary classification">
  <img src="https://img.shields.io/badge/Dataset-German%20Credit-green" alt="German credit dataset">
</p>

## 📌 About the Project

This research project explores whether information about a loan applicant can help classify their recorded credit risk as **good** or **poor/bad**.

The project uses the German Credit dataset to study applicant features, prepare the data, and compare binary classifiers. It is an educational research project; it is not a validated system for making real lending decisions.

## 🎯 Research Goals

- Explore patterns between applicant features and the credit-risk label.
- Prepare the dataset for machine-learning experiments.
- Compare multiple binary classifiers using consistent evaluation.
- Review model errors and explain limitations.

## 📊 Dataset

The dataset is from [Kaggle’s German Credit dataset](https://www.kaggle.com/datasets/benjaminmcgregor/german-credit-data-set-with-credit-risk/data).

It includes applicant information such as age, sex, job, housing, savings, checking-account status, credit amount, loan duration, and loan purpose.

### Target Labels

The target column is `Credit Risk`. The project maps its original labels as follows:

| Original label | Meaning | Binary label |
|---:|---|---:|
| `1` | Good credit risk | `0` |
| `2` | Poor/bad credit risk | `1` |

## 🔎 Current EDA Snapshot

The saved notebook results currently report **954 rows**:

- **665 good-risk cases (`0`)** — about 69.7%.
- **289 poor/bad-risk cases (`1`)** — about 30.3%.
- `Saving accounts` has 175 missing values.
- `Checking account` has 378 missing values.

The notebooks show differences in credit-risk proportions across some applicant categories. The mean credit amount is also higher for class `1` in the saved results. These are preliminary patterns in this dataset; they do not prove cause and effect. Re-run the notebooks before treating the numbers as final.

## ⚙️ Project Workflow

```text
Raw data → Label preparation → Feature preprocessing → Model experiments → Error analysis
```

1. **Data quality** — inspect shape, columns, data types, missing values, duplicates, and target classes.
2. **EDA** — review class balance, feature distributions, and patterns between features and credit risk.
3. **Preprocessing** — prepare missing values, categorical features, and numeric features.
4. **Model experiments** — compare classifiers on the prepared data.
5. **Error analysis** — review predictions, confusion matrices, and evaluation measures.

## 🤖 Model Experiments

The repository currently includes a **K-Nearest Neighbors (KNN)** experiment. Its saved test results at the default classification threshold show:

| Measure | Current KNN result |
|---|---:|
| Accuracy | 69.6% |
| ROC-AUC | 0.642 |
| Recall for poor/bad-risk class (`1`) | 9.0% |

The low recall means this experiment misses many poor/bad-risk cases at the default threshold. This is a preliminary result, not a final model selection. Further classifier comparisons and validation are still needed.

Planned comparisons include Logistic Regression, Decision Tree, Random Forest, and XGBoost.

## 🗂️ Repository Structure

```text
data/
├── raw/          Original dataset
├── in-between/   Dataset with binary target labels and row index removed
└── processed/    Prepared train/test features and labels

docs/             Project and dataset documentation
notebooks/
├── 01_data_quality.ipynb
├── 02_eda.ipynb
├── 03_preprocessing.ipynb
└── models/
    └── 02_knn.ipynb

reports/figures/  Generated charts
src/              Reusable project functions
tests/            Project checks
requirements.txt  Python dependencies
```

## 🚀 Getting Started

Install the packages used by the current notebooks:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

Then open the notebooks in Jupyter or Visual Studio Code and run them in workflow order:

1. `01_data_quality.ipynb`
2. `02_eda.ipynb`
3. `03_preprocessing.ipynb`
4. `models/02_knn.ipynb`

Some notebook paths are still being standardized for use on other computers. In particular, check that the model notebook reads the prepared files from this repository rather than from a personal drive path.

## ⚠️ Limitations and Responsible Use

- Results apply to this dataset and may not generalize to other people, lenders, or time periods.
- Missing data and unequal class proportions can affect model results.
- A model prediction should not be the only basis for approving or rejecting a real loan.
- This project is for research and learning, not for production lending decisions.