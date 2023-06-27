import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    df = spark.read.option("delimiter","\t") \
        .option("header","false") \
        .csv("/workspaces/docker-spark/examples/u.data").show()

    spark.stop()