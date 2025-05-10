import pandas as pd

dataset = pd.read_csv('raw_data/bird_migration_data.csv')
print(dataset)

sumaryStats = dataset.describe()

speciesCount = dataset['Species'].value_counts()

sucessRate_by_Species = (
    dataset.groupby('Species')['Migration_Success'].value_counts(normalize=True).unstack().fillna(0) * 100
)

interruptionReasons = dataset['Interrupted_Reason'].value_counts()

tagWeight_by_success = dataset.groupby("Migration_Success")["Tag_Weight_g"].mean()