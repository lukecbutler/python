from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("load-csv")
    .config("spark.driver.extraJavaOptions",
            "--add-opens=java.base/javax.security.auth=ALL-UNNAMED "
            "--add-opens=java.base/java.lang=ALL-UNNAMED")
    .config("spark.executor.extraJavaOptions",
            "--add-opens=java.base/javax.security.auth=ALL-UNNAMED "
            "--add-opens=java.base/java.lang=ALL-UNNAMED")
    .getOrCreate()
)

df = spark.read.csv("nCinoPrep/AAPL.csv", header=True, inferSchema=True)
df.show()