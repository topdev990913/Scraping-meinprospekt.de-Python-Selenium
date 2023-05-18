import pandas as pd
df = pd.read_csv('Result13.csv')
# If you know the name of the column skip this
first_column = df.columns[0]
# Delete first
df = df.drop([first_column], axis=1)
df.to_csv('Result.csv', index=False)