from csv import writer
  
newEntry=['Andrew Earlwood','2013-05-07',75000.0,12]
  
with open('hrdata_modified.csv', 'a') as employee_file:
  
    employee_writer = writer(employee_file)
    employee_writer.writerow(newEntry)
  
    employee_file.close()