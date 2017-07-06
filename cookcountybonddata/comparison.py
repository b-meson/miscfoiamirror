import csv

with open('CCSOFOIA.csv', 'rb') as master:
    master_indices = dict((r[1], i) for i, r in enumerate(csv.reader(master)))

with open('tabuladata.csv', 'rb') as hosts:
    with open('results.csv', 'wb') as results:    
        reader = csv.reader(hosts)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['RESULTS'])

        for row in reader:
            index = master_indices.get(row[3])
            if index is not None:
                message = 'FOUND in master list (row {})'.format(index)
            else:
                message = 'NOT FOUND in master list'
            writer.writerow(row + [message])
