### Overview

Quick demo/learning project to play around with pulling historic readings data from the Environment Agency API and storing in a local Postgresql DB.  

Runs as a cron job on a Raspberry Pi storing 7 days worth of readings (-2 to -9 days).

---

### Scripts

- initTables.sh - Create the tables as defined in sql/createTables.sql
- updateStations.sh - Get the most recent station data, parse JSON API response and update `stations` table
- updateMeasures.sh - Batch job, get the most recent (2 days ago to account for delay in publishing historic data) data, parse and copy in `measurements` table and remove measurements older than 9 days.

Postgres connection (host, port, credentials etc.) and batch job log output directory defined in `config/pgconfig.conf` (see template).