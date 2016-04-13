import numpy as np
from datetime import datetime
from collections import defaultdict

f = open('data.csv', 'r')

output=[]
compliant_count = 0
non_compliant_count = 0
data=[]

for line in f:
    l = line.split(',')
    foia_num = l[1]

    # null entries will be skipped
    if not l[0]:
       continue
    #incomplete requests will be skipped / not counted
    if not l[2]:
        continue

    request_date = datetime.strptime(l[0], '%d-%b-%y')
    execute_date = datetime.strptime(l[2], '%d-%b-%y')

    data.append(list((foia_num,request_date,execute_date)))

f.close()
#read in custom calendar, Chicago uses non standard US holidays.
holiday_file = open('chicago_observed_holidays')
holidays=[]

for line in holiday_file:
    line = line.strip('\n')
    if line.startswith("#"):
        continue
    if line.__eq__(''):
        continue
    format_str = '%A %B %d %Y'
    holiday = datetime.strptime(line, format_str)
    holidays.append(holiday.date())
holiday_file.close()

A = [d[1].date() for d in data]
B = [d[2].date() for d in data]
delta_bdays = np.busday_count(A,B,holidays=holidays)

#create frequency distribution for each time to completion
d = defaultdict(int)

for i in xrange(0,len(data)):
    #Give CPD the benefit of the doubt
    compliant = True
    if(delta_bdays[i] > 5):
        compliant = False
        non_compliant_count += 1
    else:
        compliant_count += 1

    d[delta_bdays[i]]+=1

    output.append(list([data[i][0],
                       data[i][1].strftime('%Y-%m-%d'),
                       data[i][2].strftime('%Y-%m-%d'),
                        delta_bdays[i],
                       compliant]))

output_file = open("compliance_distribution.csv", "w")
for key,val in d.iteritems():
    if key >= 0:
        output_file.write(str(key)+str(",")+str(val)+"\n")
output_file.close()

print "compliant: ",compliant_count,\
    " Non Compliant >5 days: ", non_compliant_count,\
    " Percent violated: ", non_compliant_count*100.0/(compliant_count+non_compliant_count)
