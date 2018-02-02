from pyspark import SparkContext

data = [0, 3 , 5, 2, 7]

print(data)

rdd = SparkContext().parallelize(data, 4)

res = rdd.glom().collect()

print(res)

SparkContext().stop()
