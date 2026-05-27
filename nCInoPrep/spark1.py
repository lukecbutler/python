from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("mySparkApp").getOrCreate()

