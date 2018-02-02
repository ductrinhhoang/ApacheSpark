from pyspark import SparkContext

sc = SparkContext(appName='TestFilter')

lines = sc.textFile("ex1/Readme.md")

pythonLines = lines.filter(lambda line: "Python" in line)

print "Filter Line: ", pythonLines.collect()