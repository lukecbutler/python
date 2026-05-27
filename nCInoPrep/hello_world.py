from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("hello-world").master("local[*]").getOrCreate()
print("\n")

print(spark.version)

