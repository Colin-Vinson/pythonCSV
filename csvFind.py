import csv

with open('hrdata_modified.csv') as f:
    reader = csv.reader(f)
    
    found = 0
    success = 0

    employee = input('Enter employee name: ')
    
    for row in reader:
        if employee in row[0]:
            found = 1
            # if row[3] == '15':
            #     success = 1
    if found == 1:
        print('Employee found')
        # if success == 1:
        #     print('Access Granted!')
        # else:
        #     print('Access denied')
    else:
        print('Employee not found')