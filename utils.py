import pandas as pd

def loadData(df): 
    return pd.read_csv('raw_data/bird_migration_data.csv')