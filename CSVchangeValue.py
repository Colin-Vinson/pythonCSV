import csv

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

r = csv.reader(open('hrdata_modified.csv')) 
lines = list(r)

lines[val][4] = '88-888-8888'

writer = csv.writer(open('output.csv', 'w'))
writer.writerows(lines)
