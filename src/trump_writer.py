# import libraries
from pymongo import MongoClient
from datetime import datetime
from src.DataReader import DataReader

# paths to data
trump = "../data/trump.csv"
# indexes = [0, 25, 75, 175, 375, 875, 1875, 6875, 16875, 66875, 166875]
indexes = [25, 50, 100, 200, 500, 1000, 5000, 10000, 50000, 100000]

mongo_burak = 'mongodb+srv://<<username>>:<<password>>@cluster0.aztrv.mongodb.net/?retryWrites=true&w=majority'
mongo_client = MongoClient(mongo_burak)


def read_trump():
    return DataReader(trump).read_csv_data()


trump_data = read_trump()


def insert_trump(i_s, i_e):
    start = datetime.timestamp(datetime.now())
    mongo_client.db.trump.insert_many(trump_data[i_s:i_e])
    end = datetime.timestamp(datetime.now())
    return end - start


def read_trump():
    start = datetime.timestamp(datetime.now())
    cursor = mongo_client.db.trump.find({})
    for inventory in cursor:
        pass
    end = datetime.timestamp(datetime.now())
    return end - start


def delete_trump():
    start = datetime.timestamp(datetime.now())
    mongo_client.db.trump.delete_many({})
    end = datetime.timestamp(datetime.now())
    return end - start


print("Total row: {}".format(len(trump_data)))
results_insert = dict()
results_read = dict()
results_delete = dict()


def process_trump():
    for i in indexes:
        print("Starting insert with {} data".format(i))
        ts_insert = insert_trump(0, i)
        ts_read = read_trump()
        ts_delete = delete_trump()
        print("Results insert: {} seconds with {} data".format(round(ts_insert, 3), i))
        print("Results read: {} seconds with {} data".format(round(ts_read, 3), i))
        print("Results delete: {} seconds with {} data".format(round(ts_delete, 3), i))
        results_insert[str(i)] = ts_insert
        results_read[str(i)] = ts_read
        results_delete[str(i)] = ts_delete


process_trump()
