import pandas

df = pandas.read_csv('hrdata_modified.csv')

newEmployee = ['Eric Edward','2014-06-23',71000.00,5]

df.loc[len(df.index)+1] = newEmployee

df.to_csv('hrdata_modified.csv', index=False)