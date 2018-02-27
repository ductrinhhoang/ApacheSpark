from pyspark import SparkContext

sc = SparkContext(appName="WordCount")

lines = sc.textFile("/home/superhorse/ApacheSpark/spark-2.2.1-bin-hadoop2.7/python/trainning/wordCount/Introduction.txt")

print lines.collect()

result = lines.map(lambda line: len(line.split(" ")))\
                .reduce(lambda x,y: x+y)

print "Word Count: ", result

sc.stop()
