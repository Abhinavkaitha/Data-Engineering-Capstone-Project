from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import functions as sf
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer, StopWordsRemover
import pyspark.sql.functions as psf
from pyspark.sql.types import StructType
from pyspark.sql.types import IntegerType
from pyspark.ml.classification import LinearSVC
from pyspark.ml.feature import VectorSlicer
import psycopg2

conn = psycopg2.connect(
    "dbname='postgres' user='postgres1' host='postgres1.c8ubsnm2laco.us-west-2.rds.amazonaws.com' password='postgres1'")
cur = conn.cursor()

import re
import string


def remove_punct(data_frame, col_select):
    return data_frame.select(col_select, (lower(regexp_replace('text', "[^a-zA-Z\\s]", "")).alias('text')))


def tokenize(data_frame):
    tokenizer = Tokenizer(inputCol="text", outputCol="tokens")
    tokenizedData = tokenizer.transform(data_frame)
    return tokenizedData


def stop_word_remover(data_frame):
    Stop_word_remover = StopWordsRemover(inputCol='tokens',
                                         outputCol="MeaningfulWords")
    Data_with_no_stop_words = Stop_word_remover.transform(data_frame)
    return Data_with_no_stop_words


def term_frequency(data_frame):
    hashTF = HashingTF(inputCol='MeaningfulWords', outputCol="features")
    Numeric_data = hashTF.transform(data_frame)
    return Numeric_data


def data_split(data_frame):
    dividedData = data_frame.randomSplit([0.7, 0.3])
    trainingData = dividedData[0]
    testingData = dividedData[1]
    return trainingData, testingData


def logistic_regression(trainingData):
    lr = LogisticRegression(labelCol="label", featuresCol="features",
                            maxIter=10, regParam=0.01)

    model = lr.fit(trainingData)
    return model


def get_validation(model, testingData):
    prediction = model.transform(testingData)
    predictionFinal = prediction.select("MeaningfulWords", "prediction", "Label")
    correctPrediction = predictionFinal.filter(predictionFinal['prediction'] == predictionFinal['Label']).count()
    totalData = predictionFinal.count()
    print('Accuracy : ', correctPrediction / totalData)


def svc(trainingData):
    lsvc = LinearSVC(maxIter=10, regParam=0.1)
    lsvcModel = lsvc.fit(trainingData)
    return lsvcModel


def add_new_columns(tweet_data):
    tweet_data = tweet_data.withColumn('date_', tweet_data['created_at'].substr(9, 2))
    tweet_data = tweet_data.withColumn('day', tweet_data['created_at'].substr(1, 3))
    tweet_data = tweet_data.withColumn('month', tweet_data['created_at'].substr(5, 3))
    tweet_data = tweet_data.withColumn('hour', tweet_data['created_at'].substr(12, 2))
    tweet_data = tweet_data.withColumn('year', tweet_data['created_at'].substr(27, 4))
    tweet_with_timestamp = tweet_data.withColumn('time_stamp',
                                                 sf.concat(sf.col('month'), sf.lit('-'), sf.col('date_'), sf.lit('-'),
                                                           sf.col('year')))
    tweet_data = tweet_with_timestamp.withColumn('date',
                                                 to_date(unix_timestamp(col('time_stamp'), 'MMM-dd-yyyy').cast(
                                                     "timestamp")))
    return tweet_data


def blank_as_null(x):
    return when(col(x) != " ", col(x)).otherwise("NULL")


def identify_company(word_list, tweet_data):
    tweet_data = tweet_data.withColumn(
        'company',
        psf.regexp_extract('text', '(?=^|\s)(' + '|'.join(words_list) + ')(?=\s|$)', 0))
    return tweet_data


def rename_companies(words_list1, words_list2, tweet_data):
    for i in words_list1:
        tweet_data = tweet_data.withColumn('company', regexp_replace('company', i, 'Coca-Cola'))

    for i in words_list2:
        tweet_data = tweet_data.withColumn('company', regexp_replace('company', i, 'Pepsi'))
    return tweet_data


def mini_pipe(clean_data):
    tokenizedData = tokenize(clean_data)

    Data_with_no_stop_words = stop_word_remover(tokenizedData)

    Numeric_data = term_frequency(Data_with_no_stop_words)

    return Numeric_data


def write_row(row, conn):
    cur = conn.cursor()
    s = "INSERT INTO tone(company,date,day,hour,location,tone) VALUES ('%s','%s','%s',%s,'%s',%s)" \
        % (row['company'], row['date'], row['day'], row['hour'], row["location"], row['tone'])
    try:
        cur.execute(s)
        conn.commit()
    except:
        conn.rollback()


if __name__ == '__main__':
    tweets_csv = spark.read.csv('s3a://tone-of-the-nation/train.csv', inferSchema=True, header=True)
    data_with_useful_columns = tweets_csv.select(col("SentimentText").alias('text'),
                                                 col("Sentiment").cast("Int").alias("label"))

    data_with_no_punc = remove_punct(data_with_useful_columns, 'label')

    Numeric_data = mini_pipe(data_with_no_punc)

    trainingData , testingData = data_split(Numeric_data)

    model_logistic = logistic_regression(traiingData)

    get_validation(model_logistic, testingData)

    lsvc_model = svc(trainingData)

    get_validation(lsvc_model, testingData)

    tweet_data = spark.read.format("parquet").load("s3a://tone-of-the-nation/new_parque")

    tweet_data = add_new_columns(tweet_data)

    drop_cols = ['created_at', 'date_', 'month', 'year', 'time_stamp']
    tweet_data = tweet_data.drop(*drop_cols)

    words_list1 = ['Coke', 'coke', 'Cola', 'cola', 'CocaCola', 'cocacola', 'Coca-Cola', 'coca-cola']

    words_list2 = ['Pepsi', 'pepsi']

    tweet_data = identify_company(words_list1 + words_list2, tweet_data)

    tweet_data = rename_companies(words_list1, words_list2, tweet_data)

    Tweet_data = tweet_data.withColumn("company", blank_as_null("company"))

    tweet_clean = Tweet_data.select('location', 'day', 'hour', 'date', 'company',
                                    (lower(regexp_replace('text', "[^a-zA-Z\\s]", "")).alias('text')))

    Numeric_data = mini_pipe(tweet_clean)

    prediction_svm = lsvcModel.transform(Numeric_data)
    predictionFinal_svm = prediction_svm.select("MeaningfulWords", "prediction", 'date', 'company', 'day', 'hour',
                                                'location', 'MeaningfulWords', 'features')

    slicer = VectorSlicer(inputCol="rawPrediction", outputCol="tone", indices=[1])
    result = slicer.transform(predictionFinal_svm)

    drop_cols = ['MeaningfulWords', 'features', 'rawPrediction', 'prediction']
    result = result.drop(*drop_cols)

    for row in result.rdd.collect():
        write_row(row, conn)
    print("Data is pushed to database")