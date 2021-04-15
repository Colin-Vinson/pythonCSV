import csv

with open('newCSV.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Name', 'Dept', 'Birth_month'])
    employee_writer.writerow(['John Smith', 'Accounting', 'Nov'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'Mar'])
    employee_writer.writerow(['Eric Edward', 'IT', 'Apr'])
    employee_writer.writerow(['Ryan Curtis', 'BA', 'Jan'])