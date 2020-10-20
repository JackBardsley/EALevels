"""
Parse and clean historic measurements csv
"""
import csv
import sys

# read from stdin and get header
measurements = sys.stdin.read().splitlines()
measurements = [x for x in csv.reader(measurements)]
header = [x.lower() for x in measurements[0]]
measurements = measurements[1:]

# table field cols
cols = ['datetime','date','label','stationreference','parameter','qualifier','period','unitname','valuetype','value']
# get field ix from csv header
cols_ix = {x:header.index(x) for x in cols}

# write to stdout
writer = csv.writer(sys.stdout)
writer.writerow(cols)
for row in measurements:
    outrow = []
    for k in cols:
        # Clean value field
        if k == 'value' and '|' in row[cols_ix['value']]:
            outrow.append(str(row[cols_ix[k]].split('|')[-1]))
        elif k == 'qualifier' and row[cols_ix[k]] == '':
            outrow.append('N/A') 
        else:
            outrow.append(row[cols_ix[k]])
    writer.writerow(outrow)

