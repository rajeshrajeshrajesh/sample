from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("MySQL Test") \
    .config("spark.jars", "/Users/as-mac-1261/Downloads/mysql-connector-j-9.6.0/mysql-connector-j-9.6.0.jar") \
    .getOrCreate()
# Step 2: Load CSV
df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Users/as-mac-1261/sample/sample/data/ads.csv")

print("Raw Data:")
df.show()
from pyspark.sql.functions import col, sum
clean_df = df.dropna()

platform_spend = clean_df.groupBy("platform") \
    .agg(sum("spend").alias("total_spend"))

# Campaign with most clicks
top_campaign = clean_df.orderBy(col("clicks").desc())

# Low performance ads (low clicks)
low_perf = clean_df.filter(col("clicks") < 100)

print("Platform Spend:")
platform_spend.show()

print("Top Campaigns:")
top_campaign.show()

print("Low Performance Ads:")
low_perf.show()



# Write to MySQL
jdbc_url = "jdbc:mysql://localhost:3306/walmart"

properties = {
    "user": "root",
    "password": "Jeevan@123",
    "driver": "com.mysql.cj.jdbc.Driver"
}

print("Before write...")


clean_df.write.jdbc(url=jdbc_url, table="ads_clean", mode="overwrite", properties=properties)

platform_spend.write.jdbc(url=jdbc_url, table="platform_spend", mode="overwrite", properties=properties)

top_campaign.write.jdbc(url=jdbc_url, table="top_campaign", mode="overwrite", properties=properties)

low_perf.write.jdbc(url=jdbc_url, table="low_performance", mode="overwrite", properties=properties)

print("After write...")

print("Data written to MySQL ✅")

<<<<<<< HEAD
header = rdd.first()
data = rdd.filter(lambda row: row != header)

data=data.map(lambda row: row.split(","))

filtered = data.filter(lambda x:x[5] != '' and float((x[5])>25))
=======
>>>>>>> 179cad8 (Last commit)
