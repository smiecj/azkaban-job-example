# -*- coding: UTF-8 -*-

from impala.dbapi import connect
from common import ConfigParser


if __name__ == '__main__':
    import sys
    config_file = sys.argv[1]
    config_parser = ConfigParser(config_file)
    impala_host = config_parser.get("impala.host")
    impala_port = config_parser.get("impala.port")
    

    conn = connect(host=impala_host, port=impala_port)
    cursor = conn.cursor()
    cursor.execute('show databases')
    results = cursor.fetchall()
    print(results)
