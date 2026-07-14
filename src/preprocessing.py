import pandas as pd

def dataset_info(df):
    print("\n============ First 5 row ============")
    print(df.head())



    print("\n============ Last 5 row ============")
    print(df.tail())


    print("\n============ Dataset Info ============")
    print(df.info())


    print("\n============ Dataset shape ============")
    print(df.shape)


    print("\n============ Columns ============")
    print(df.columns)


    print("\n============ Data Type ============")
    print(df.dtypes)


    print("\n============ Statistical Summary ============")
    print(df.describe())


def check_missing_values(df):
    print("\n============ Check Missing Values ============")
    print(df.isnull().sum())


def check_duplicates(df):
    print("\n============ Check Duplicate Records ============")
    print(df.duplicated().sum())

def remove_duplicates(df):
    print("\n============ Remove Duplicates ============")
    df=df.drop_duplicates()
    return df

def save_clean_data(df):
    df.to_csv("data/emoloyee_cleaned.csv",index=False)
    print("\n Cleaned dataset saved successfully.")