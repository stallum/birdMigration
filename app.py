import pandas as pd

dataset = pd.read_csv('raw_data/bird_migration_data.csv')
print(dataset)

sumaryStats = dataset.describe()