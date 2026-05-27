from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

# Create a DataFrame
census_df = spark.read.csv("census.csv").toDF(
    "gender", "age", "zipcode", "salary_range_usd", "marriage_status"
)

# Show the DataFrame
census_df.show()
