import pandas

df = pandas.read_csv('hrdata_modified.csv')

newEmployee = ['Ryan Curtis','2012-01-14',81000.00,15]

df.loc[len(df.index)+1] = newEmployee

df.to_csv('hrdata_modified.csv', index=False)