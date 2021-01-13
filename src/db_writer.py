# import libraries
from pymongo import MongoClient
from datetime import datetime
from pprint import pprint
from bson.json_util import dumps
import redis
import json
import time
import pandas as pd
import numpy as np
import csv
import redis
import json
import sys

from src.DataReader import DataReader

# paths to data
trump = "../data/trump.csv"
joe = "../data/joe.csv"
indexes = [20, 50, 100, 200, 500, 1000, 5000]

mongo_burak = 'mongodb+srv://kibitzer:c7mVVOJzgcDRxCC0@cluster0.aztrv.mongodb.net/?retryWrites=true&w=majority'
mongo_client = MongoClient(mongo_burak)


def read_trump():
    return DataReader(trump).read_csv_data()


# read joe data from csv
def read_joe():
    return DataReader(joe).read_csv_data()


trump_data = read_trump()
joe_data = read_joe()


def insert_trump(index):
    start = datetime.timestamp(datetime.now())
    mongo_client.db.trump.insert_many(trump_data[:index])
    end = datetime.timestamp(datetime.now())
    return end - start


def insert_joe(index):
    start = datetime.timestamp(datetime.now())
    mongo_client.db.joe.insert_many(joe_data[:index])
    end = datetime.timestamp(datetime.now())
    return end - start


def process_trump():
    for i in indexes:
        print("Starting insert with {} data".format(i))
        ts = insert_trump(i)
        print("Results: {} seconds with {} data".format(round(ts, 3), i))


def process_joe():
    for i in indexes:
        print("Starting insert with {} data".format(i))
        ts = insert_joe(i)
        print("Results: {} seconds with {} data".format(round(ts, 3), i))

# def store_data_to_redis(conn, data):
#     for i in data:
#         conn.setnx(i[0], i[1])
#     return data
# create Redis connection
# conn = redis.Redis(host='mycache.xpz4sa.ng.0001.use1.cache.amazonaws.com',port=6379)
# print("Redis connected....")
# print (json.dumps(store_data(conn, data)))
