import csv

with open('newCSV.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['Name', 'Dept', 'Birth_month'])
    csv_writer.writerow(['John Smith', 'Accounting', 'November'])
    csv_writer.writerow(['Erica Meyers', 'IT', 'March'])
    csv_writer.writerow(['Eric Edward', 'IT', 'April']
