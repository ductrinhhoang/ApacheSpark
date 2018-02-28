from pyspark import SparkContext

def resultFormat(res):
    return float("{0:.2f}".format(0.15+0.85*res))

def change(arr, rank):
    nArr = []
    val = float(rank)/len(arr)
    for obj in arr:
        nArr.append((obj,float(val)))
    return nArr

sc = SparkContext(appName="pageRank")

data = [("facebook",["yahoo", "google","weibo"]),("yahoo",["facebook"]),("google",["facebook","weibo"]),("weibo",["facebook","google"])]

# inp = sc.parallelize(data).partitionBy(4) #20s

inp = sc.parallelize(data) #27s

rank = inp.mapValues(lambda val: 1)

i=0
while i<10:
    rank = inp.join(rank)\
                .mapValues(lambda x: change(x[0], x[1]))\
                .flatMap(lambda x: x[1])\
                .reduceByKey(lambda x, y: x+y)\
                .mapValues(lambda val: resultFormat(val))
                # Ghep (K, V), (K, R) -> (K, (V, R))
                # Mapvalues (K, ([v1, ..., vj], R)) -> (K, [(v1, R/j),..., (v2, R/j)] )
                # FlatMap (K, [(v1, R/j),..., (vj, R/j)]) -> (v1, R/j), ..., (vj, R/j)
		
    i = i+1

print rank.collect()
