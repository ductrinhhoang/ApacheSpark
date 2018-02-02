# ApacheSpark

After clone this resposity and if you don't know anything of spark, you need do folow under link (only for ubuntu):
https://medium.com/@josemarcialportilla/installing-scala-and-spark-on-ubuntu-5665ee4b62b1

Then, you need set path for spark. Turn on terminal -> vi ~/.bashrc
In the bottom of file, write:
	export SPARK_HOME="/home/superhorse/ApacheSpark/spark-2.2.1-bin-hadoop2.7"
	export PATH=$PATH:$SPARK_HOME/bin
