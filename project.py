# Create a spark Instance
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("heart_disease_classification").getOrCreate()

#Reading data from csv and creating a Spark Dataframe
df = spark.read.csv("C:/Users/Praveen/Desktop/2ndSem/BigData/Project/heart_2020_cleaned.csv", inferSchema=True, header=True)
df.show(2)
