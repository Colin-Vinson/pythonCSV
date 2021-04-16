import csv
import pandas

user_input = input('Enter employee name: ')

def find_index(input): 
    o = open('hrdata_modified.csv', 'r') 
    myData = csv.reader(o) 
    index = 0 
    for row in myData:
      #print (row)
      if row[0] == input: 
        return index 
      else : index+=1 
val = find_index(user_input)
print (val)

reader = csv.reader(open('hrdata_modified.csv')) 
lines = list(reader)

if lines[val][1]== str(user_input):
    lines[val][4] = '99-999-9999'


    w = open('output.csv', 'w', newline='')
    writer = csv.writer(w)
    writer.writerows(lines)
    w.close()

    df = pandas.read_csv('output.csv',
        index_col='Employee',
        parse_dates=['Hired'],
        header=0, 
        names=['Employee', 'Hired','Salary', 'Sick Days', 'ID#'])

    print(df)

    commit = input('Would you like to commit the changes? (Y/N)')

    if commit == 'Y' or commit == 'y':
        df.to_csv('hrdata_modified.csv')
        print('Changes commited.')
    else:
        print('Changes not commited.')
else:
    print('Employee not found!')        
