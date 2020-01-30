from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, upper, col, column, instr
from pyspark.sql import SQLContext
from pyspark.sql import SQLContext

spark = SparkSession.builder.appName("Preprocessing App").getOrCreate()
sc = spark.sparkContext
sqlcontext = SQLContext(sc)

def reduce_dataframe_to_essential_fields(df):
    return df.select(col('created_at'),col('text'),col('place.name').alias('location')) 

if __name__ = '__main__':
	folder_data = sqlcontext.read.json("s3a://tone-of-the-nation/back_up/twitter_bz2/twitter-2018-05-02/2018/05/02/08")

	folder_data = reduce_dataframe_to_essential_fields(folder_data)

	folder_data.write.format("parquet").mode("overwrite").save("s3a://tone-of-the-nation/test")
    
    spark.stop()