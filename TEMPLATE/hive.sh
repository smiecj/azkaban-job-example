#!/bin/bash

hive_server=$1
sql_file=$2

echo "[test] ${hive_server}"
echo "[test] ${sql_file}"

beeline -u ${hive_server} -n $(whoami) -e ${sql_file}