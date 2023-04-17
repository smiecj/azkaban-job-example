# -*- coding: UTF-8 -*-

# findspark: for load SPARK_HOME
# https://sparkbyexamples.com/pyspark/pyspark-py4j-protocol-py4jerror-org-apache-spark-api-python-pythonutils-jvm/
import findspark
findspark.init()

from pyspark.sql import SparkSession
from common import ConfigParser


if __name__ == '__main__':
    import sys
    config_file = sys.argv[1]
    config_parser = ConfigParser(config_file)

    import os
    os.environ["CLASSPATH"] = os.environ["CLASSPATH"] + ":" + config_parser.get("hive.config.site.path")
    os.environ["HADOOP_CONF_DIR"] = config_parser.get("hadoop.config.path")
    yarn_job_name = os.environ["yarn_job_name"]

    hive_metastore_uri = config_parser.get("hive.metastore.uri")

    spark = SparkSession \
        .builder \
        .appName(yarn_job_name) \
        .config("hive.metastore.uris", hive_metastore_uri) \
        .enableHiveSupport() \
        .getOrCreate()

    my_dataframe = spark.sql("show databases")
    my_dataframe.show()