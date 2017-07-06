import csv
from datetime import datetime
import numbers

output_file = open("output.csv", 'w')
writer = csv.DictWriter

with open('CCSOFOIA.csv', 'rbt') as master:
    reader = csv.reader(master)
    next(master)
    for row in reader:
        if row[0] and row[0]!='#REF!':
            newdate = datetime.strptime(row[0], '%m/%d/%y')
            row[0] = datetime.strftime(newdate, '%-m/%-d/%Y')
        if row[0] == '#REF!': 
            row[0] = 'unknown'
        if row[3]:
            row[3] = ("%.2f" % float(row[3]))
        if row[10]:
            row[10] = row[10].strip()
        if row[11]:
            row[11] = row[11].strip()
        writer = csv.writer(output_file)
        writer.writerow(row)

master.close()
output_file.close()
