# -*- coding: UTF-8 -*-

from impala.dbapi import connect
from backports import configparser

DEFAULT_SECTION = 'default'


if __name__ == '__main__':
    import sys
    config_file = sys.argv[1]
    config = configparser.RawConfigParser()

    with open(config_file, 'r') as f:
        config_string = f'[{DEFAULT_SECTION}]\n' + f.read()

    config.read_string(config_string)
    impala_host = config.get(DEFAULT_SECTION, "impala.host")
    impala_port = config.get(DEFAULT_SECTION, "impala.port")
    

    conn = connect(host=impala_host, port=impala_port)
    cursor = conn.cursor()
    cursor.execute('show databases')
    results = cursor.fetchall()
    print(results)
