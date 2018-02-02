from pyspark import SparkContext 
def show(x):
    print "Show:", x, ", len:", len(x)
    return len(x)

sc = SparkContext(appName="LineCount")

lines = sc.textFile("input.txt")

line_lengths = lines.map(lambda x: show(x))

# line_lengths.persist()

result = line_lengths.reduce(lambda x,y: x+y)

print "Result: ", result

sc.stop()
