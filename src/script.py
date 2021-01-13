from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps

client = MongoClient('mongodb+srv://kibitzer:c7mVVOJzgcDRxCC0@cluster0.aztrv.mongodb.net/?retryWrites=true&w=majority')
all_db_names = client.list_database_names()[:-2]  # last 2 db is admin and local that are not related

# key is database name
# value is an array
# 1st element of this array is db object
# 2nd element is dict of collection name and colleciton object
db_dict = dict()

for db_name in all_db_names:
    db_dict[db_name] = [client[db_name]]

for key, value in db_dict.items():
    db_obj = value[0]
    collections_names = db_obj.list_collection_names()

    # keep collection name and colleciton obj as key value
    temp_col_dict = dict()
    for col_name in collections_names:
        temp_col_dict[col_name] = db_obj[col_name]

    db_dict[key].append(temp_col_dict)

# for db_name, dict_value in db_dict.items():
#     db_obj = dict_value[0]
#     col_dict = dict_value[1]
#     print(db_name, end='\n')
#     for col_name, col_value in col_dict.items():
#         print(col_name, end='\n')
#         cursor = col_value.find({})
#         for inventory in cursor:
#             pprint(inventory)
#             break
#         break
#     break

listingsAndReviews = client.sample_airbnb.listingsAndReviews

data_cursor = listingsAndReviews.find({})
data = list(data_cursor)
