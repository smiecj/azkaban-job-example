#!/bin/bash

python_bin=$1
python_file=$2
config_file=$3

source /etc/profile

${python_bin} ${python_file} ${config_file}