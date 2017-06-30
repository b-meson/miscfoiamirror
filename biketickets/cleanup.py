import csv

with open('BikeTickets.csv', 'rb') as csvfile:
     for line in csvfile.readlines():
         line.strip('\n')
         if line and (not line.isspace()):
             print(line.strip('\n'))
