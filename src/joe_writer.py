# import libraries
from pymongo import MongoClient
from datetime import datetime

from src.DataReader import DataReader

# paths to data
joe = "../data/joe.csv"
indexes = [20, 50, 100, 200, 500, 1000, 5000]

mongo_burak = 'mongodb+srv://kibitzer:c7mVVOJzgcDRxCC0@cluster0.aztrv.mongodb.net/?retryWrites=true&w=majority'
mongo_client = MongoClient(mongo_burak)


# read joe data from csv
def read_joe():
    return DataReader(joe).read_csv_data()


joe_data = read_joe()


def insert_joe(index):
    start = datetime.timestamp(datetime.now())
    mongo_client.db.joe.insert_many(joe_data[:index])
    end = datetime.timestamp(datetime.now())
    return end - start


def process_joe():
    for i in indexes:
        print("Starting insert with {} data".format(i))
        ts = insert_joe(i)
        print("Results: {} seconds with {} data".format(round(ts, 3), i))
