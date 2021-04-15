import csv

with open('hrdata_modified.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)

#print(data)

employee = input("Enter employee name: ")

if (employee in [j for i in data for j in i]) == True:
    print("Employee found!")
else:
    print("Employee not found!")
