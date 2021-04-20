import pandas

df = pandas.read_csv('hrdata_modified.csv')

newEmployee = ['Colin Vinson','2011-01-17',82000.00,25,'11-111-1111']

df.loc[len(df.index)+1] = newEmployee

df.to_csv('hrdata_modified.csv', index=False)