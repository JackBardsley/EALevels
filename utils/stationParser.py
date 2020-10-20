"""
Parse station json data to csv for postgres copy
"""
import csv
import json
import sys

data = json.loads(sys.stdin.read())
stations = data['items']

cols = ['RLOIid','catchmentName','dateOpened','easting','label','lat','long','northing','notation','riverName','stationReference','town','wiskiID']

writer = csv.writer(sys.stdout)
writer.writerow(cols)
for row in stations:
    # check for primary key and corrupted data
    if 'notation' in row and 'lat' in row:
        if row['notation'] and '[' not in str(row['lat']):
            outrow = []
            for k in cols:
                if k in row:
                    outrow.append(row[k])
                else:
                    outrow.append(None)
            writer.writerow(outrow)