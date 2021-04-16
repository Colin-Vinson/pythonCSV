import csv
import pandas

user_input=input('Enter employee name: ')

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

lines[val][4] = str('77-777-7777')

w = open('output.csv', 'w', newline='')
writer = csv.writer(w)
writer.writerows(lines)
w.close()

df = pandas.read_csv('output.csv')

print(df)
commit = input('Would you like to commit the changes? (Y/N)')
if commit == 'Y' or 'y':
    df.to_csv('hrdata_modified.csv')
    print('Changes commited.')
else:
    print('Changes not commited.')
