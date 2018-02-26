from pyspark import SparkContext

def resultFormat(res):
    return float("{0:.2f}".format(res))

def change(arr):
    nArr = []
    val = 1.0/len(arr)
    for obj in arr:
        nArr.append((obj,float(val)))
    return nArr

sc = SparkContext(appName="pageRank")

data = [("facebook",["yahoo", "google","weibo"]),("yahoo",["facebook"]),("google",["facebook","weibo"]),("weibo",["facebook","google"])]

rdd = sc.parallelize(data)

rdd0 = rdd.mapValues(lambda x: change(x))\
            .flatMap(lambda x: x[1])\
            .reduceByKey(lambda x, y: x+y)\
            .mapValues(lambda val: resultFormat(val))\
            .sortByKey(True)
            # change x -> (x[0],(x[1][i], len(x[1])))
            # remove "[","]" via flatMap()
            # combine result
            # change and format result
            # sort result
print rdd1.collect()


print rdd0.collect()