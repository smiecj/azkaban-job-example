#!/bin/bash

impala_server=$1
sql_file=$2

export PYTHON_EGG_CACHE=/tmp/.python-eggs

impala-shell -i ${impala_server} -f ${sql_file}
