cd ~/Desktop

nano sparkcount.txt
Deer Bear River
Car Car River
Deer Bear Car
Deer Deer River

pwd (path + filename)
ls (will find spark-3.5.2-bin-hadoop3/bin)

cd ~/spark-3.5.2-bin-hadoop3/bin

./spark-shell

val rdd1 = spark.sparkContext.textFile("file:///home/hadoop/Desktop/sparkcount.txt")
rdd1.collect()

val rdd2 = rdd1.flatMap(x => x.split(" "))
rdd2.collect()

val rdd3 = rdd2.map(x => (x,1))
rdd3.collect()

val rdd4 = rdd3.reduceByKey((a,b) => a+b)
rdd4.collect()
rdd4.toDF("Word","Count").show()
