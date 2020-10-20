#!/bin/bash

. "$(pwd)/config/pgconfig.conf"

touch "logdir/log$(date +%y%m%d).out"
exec &>>"logdir/log$(date +%y%m%d).out"

echo "
---------------------------------------------
Job started: $(date)

"

export PGPASSWORD=$password

curl "https://environment.data.gov.uk/flood-monitoring/archive/readings-full-$(date --date="-2 days" +%Y-%m-%d).csv" | python utils/measureParser.py | psql -U $user -h $host -p $port -d $db -c "COPY measurements(datetime,date,label,stationreference,parameter,qualifier,period,unitname,valuetype,value) FROM STDIN WITH (FORMAT CSV, HEADER TRUE); DELETE FROM measurements WHERE datetime < (SELECT current_date-9);"

echo "Job complete at $(date)
---------------------------------------------
"
