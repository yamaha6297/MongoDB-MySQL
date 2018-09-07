#variables and libraries imported
import pymongo
from pymongo import MongoClient
import random
from datetime import datetime
from avgFunc import avg
from listMongo import list

#MongoClient to running mongod instance
client = MongoClient()

#getting a database
db = client.test

#getting a collection
collection = db.person

times = []
#insert 1000000 records
for n in range(0,10):
    d1=datetime.now()
    #(dictionary of data) data to insert
    data_id = collection.insert_many(list()).inserted_ids
    time = datetime.now() - d1
    print (time)
    times.append(time)

print ("Avarage time: ", avg(times))
