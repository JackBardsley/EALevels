#!/bin/bash

. "$(pwd)/config/pgconfig.conf"

export PGPASSWORD=$password

psql -U $user -h $host -p $port -d $db -f sql/createTables.sql