#!/bin/bash

hive_server=$1
sql_file=$2

beeline -u ${hive_server} -n $(whoami) -e ${sql_file}