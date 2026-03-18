from pyspark import SparkContext
sc=SparkContext()
xyz=sc.parallelize([1,2,3,4,5,6,7,7,8,8,8,8,8])
print(type(xyz))

rdd = sc.textFile("data/titanic_data.csv")

print(rdd.take(5)) 

header = rdd.first()
data = rdd.filter(lambda row: row != header)

data=data.map(lambda row: row.split(","))
