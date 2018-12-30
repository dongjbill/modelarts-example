# coding:utf-8
from sklearn.datasets import load_iris
import xgboost as xgb
from sklearn.model_selection import train_test_split
import os
from obs import ObsClient
from pyspark import SparkConf,SparkContext
from pyspark.mllib.regression import LabeledPoint 
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

AK=os.getenv('MINER_USER_ACCESS_KEY')
if AK is None:
    AK=''

SK=os.getenv('MINER_USER_SECRET_ACCESS_KEY')
if SK is None:
    SK=''

obs_endpoint=os.getenv('MINER_OBS_URL')
if obs_endpoint is None:
    obs_endpoint=''
print "obs_endpoint: " + str(obs_endpoint)

obs_path=os.getenv('TRAIN_URL')
if obs_path is None:
    obs_path=''
print "obs_path: " + str(obs_path)

data_path=os.getenv('DATA_URL')
if data_path is None:
    data_path=''
print "data_path: " + str(data_path)

OBS_MODEL_DIR = '/model/recommend'
TRAIN_DATASET = 'ratings.csv'
MODEL_NAME = 'recommend'
LOCAL_WORK_DIR = '/tmp/'

def print_title(title=""):
    print("=" * 15 + " %s " % title + "=" * 15)

def download_dataset():
    print("Start to download dataset from OBS")

    TestObs = ObsClient(AK, SK, is_secure=True, server=obs_endpoint)

    try:
        bucketName = data_path.split("/",1)[0]
        resultFileName = data_path.split("/",1)[1] + '/' +TRAIN_DATASET
        resp = TestObs.getObject(bucketName, resultFileName, downloadPath=os.path.join(LOCAL_WORK_DIR, TRAIN_DATASET))
        if resp.status < 300:
            print('Succeeded to download training dataset')
        else:
            print('Failed to download ')

    finally:
        TestObs.close()

def upload_to_obs(model_local_path):

    TestObs = ObsClient(AK, SK, is_secure=True, server=obs_endpoint)

    bucketName = obs_path.split("/",1)[0]
    resultFileName = obs_path.split("/",1)[1] + OBS_MODEL_DIR
    TestObs.putFile(bucketName, resultFileName, file_path=model_local_path)
    return 0

def train_model():
    print_title("download ratings data!")
    download_dataset()
    print_title("load data!")
    
    conf = SparkConf().setAppName("testapr").setMaster("local")
    sc = SparkContext(conf=conf)
    data_local_path = os.path.join(LOCAL_WORK_DIR, TRAIN_DATASET)
    data = sc.textFile(data_local_path)
    ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

    rank = 10
    numIterations = 10
    lambda_ = 0.02
    blocks = 100
    model = ALS.train(ratings, rank, numIterations, lambda_, blocks)

    testdata = ratings.map(lambda p: (p[0], p[1]))
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    #print ratesAndPreds
    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    print("Mean Squared Error = " + str(MSE))
    user_predict = model.recommendProductsForUsers(10).collect()

    model_local_path = os.path.join(LOCAL_WORK_DIR, MODEL_NAME)   
    model.save(sc, model_local_path)
   
    print_title("upload model to obs!")
    upload_to_obs(model_local_path)
 

if __name__ == '__main__':
    train_model()
