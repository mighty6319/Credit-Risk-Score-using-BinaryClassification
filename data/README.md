# Data Folder

The `data` folder has three folders:

## 1. raw

Contains the original dataset:

- `german-credit-data-set-with-credit-risk.csv`
  - 954 applicant records.
  - Includes age, sex, job, housing, savings, checking account, credit amount, duration, purpose, and credit risk.

## 2. in-between

Contains the mapped dataset:

- `german-credit_risk_in-between_dataset.csv`
  - 954 records.
  - Credit risk values are mapped to `0` for good and `1` for poor/bad risk.

## 3. processed

Contains the model-ready train and test datasets:

- `X_train_processed.csv`
  - 763 rows with 24 encoded and scaled feature columns.
- `X_test_processed.csv`
  - 191 rows with 24 encoded and scaled feature columns.
- `y_train.csv`
  - 763 target values for training.
- `y_test.csv`
  - 191 target values for testing.
