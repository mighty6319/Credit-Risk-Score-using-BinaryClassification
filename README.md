# Data

This folder stores the credit-risk dataset through its preparation stages.

| Folder | Contents |
|---|---|
| `raw/` | Original German credit CSV. Keep this source file unchanged. |
| `in-between/` | Dataset copy with `Credit Risk` mapped to binary labels (`1` → `0` for good, `2` → `1` for poor/bad) and the row-index column removed. |
| `processed/` | Preprocessed train/test features and labels: `X_train_processed.csv`, `X_test_processed.csv`, `y_train.csv`, and `y_test.csv`. |

**Data flow:** `raw` → `in-between` → `processed`