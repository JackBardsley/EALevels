#!/bin/bash

. "$(pwd)/config/pgconfig.conf"

export PGPASSWORD=$password

curl http://environment.data.gov.uk/flood-monitoring/id/stations | python utils/stationParser.py | psql -U $user -h $host -p $port -d $db -c " DELETE FROM stations; COPY stations(RLOIid,catchmentName,dateOpened,easting,label,lat,long,northing,notation,riverName,stationReference,town,wiskiID) FROM STDIN WITH (DELIMITER ',', FORMAT CSV, HEADER TRUE);"