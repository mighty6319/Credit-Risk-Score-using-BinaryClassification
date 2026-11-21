# Problem Definition

## Project

**Project name:** Credit Risk Score

## Problem statement

This project studies whether applicant information in the German credit dataset can be used to classify a loan applicant's recorded credit risk as **good** or **poor/bad**. The task is a binary classification problem using the dataset's `Credit Risk` column as the target.

## Target and label mapping

For the planned binary use, the dataset labels will be mapped as follows:

| Dataset value | Meaning used in this project | Binary label |
| --- | --- | ---: |
| `1` | Good credit risk | `0` |
| `2` | Poor/bad credit risk | `1` |

This mapping is based on the project owner's description and should be checked against the dataset source documentation before final reporting.

## Intended audience and use

The intended audience is a person reviewing an applicant's loan status or risk. In this research project, the model is used to study how the available applicant features relate to the recorded credit-risk class. The project will compare multiple binary classifiers and report their measured performance.

## Research aim

To examine how features such as age, sex, job, housing, savings, checking-account status, credit amount, loan duration, and purpose relate to the good/poor credit-risk label, and to compare different binary classification models on this dataset.

## Success criteria

The project will be considered complete when it has:

- Documented the dataset columns and target labels.
- Checked and described data quality and class balance.
- Compared multiple binary classifiers using a documented evaluation approach.
- Selected a best-performing model for this dataset based on the chosen evaluation measures.
- Examined important prediction errors and stated limitations.
- Recorded the experiment settings and results so the comparison can be understood and repeated.

The specific evaluation measures and model-selection rule will be chosen and documented before comparing final model results. No performance threshold or selected model has been set yet.

## Scope and limitations

- This project analyzes the supplied German credit dataset; conclusions may not apply to other populations, lenders, or time periods.
- The project studies patterns and predictive performance. It does not show that any feature causes a credit outcome.
- Dataset quality, class balance, missing values, and possible bias can affect results and must be reviewed.
- A model prediction should not be treated as the sole basis for approving or rejecting a loan.
- This is a research and learning project, not a validated lending system.
