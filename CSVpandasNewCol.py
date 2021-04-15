import pandas

df = pandas.read_csv('hrdata_modified.csv')

df["ID#"] = "00-000-0000"

df.to_csv('hrdata_modified.csv', index=False)