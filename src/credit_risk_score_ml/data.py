import pandas as pd

def original_dataset():
    df=pd.read_csv("../data/raw/german-credit-data-set-with-credit-risk.csv")
    return df

