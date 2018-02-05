from pyspark import SparkContext

sc = SparkContext()

data = [("a",1), ("b",2), ("a",3)]

pairRdd1 = sc.parallelize(data)

print "count", pairRdd1.reduceByKey(lambda x, y: x+y).collect()

pairRdd = pairRdd1.groupByKey()

print pairRdd.collect()

sc.stop()
