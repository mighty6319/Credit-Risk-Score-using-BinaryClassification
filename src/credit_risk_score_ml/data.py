import pandas as pd

def original_dataset():
    df=pd.read_csv("../data/raw/german-credit_risk_dataset.csv")
    return df

