from pyspark import SparkContext


def main():
    sc = SparkContext(appName="SparkWordCount")

    inputFile = sc.textFile("input.txt")

    print(sc)

    counts = inputFile.flatMap(lambda line: line.split())\
        .map(lambda word: word(0, 1))\
        .reduceByKey(lambda a, b: a+b)

    print("Word Count: ", counts)

    sc.stop()


main()
