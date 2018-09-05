#variables and libraries imported
import pymongo
from pymongo import MongoClient
import random
from datetime import time
from random import sample
from string import digits, ascii_letters
from avgFunc import avg

#MongoClient to running mongod instance
client = MongoClient()

#getting a database
db = client.test

#getting a collection
collection = db.person

times = []

for i in range(0,10):
    d1=time.now()
    #insert 1000000 records
    for n in range(0,1000000):
        chars = digits + ascii_letters
        cadena = ''.join(sample(chars, 8))
        #(dictionary of data) data to insert
        data_id = collection.insert_one({"nick": cadena,
                                        "age":random.randint(18,90)}).inserted_id
    time = datetime.now() - d1
    print (time)
    times.append(time)

print ("Avarage time: ", avg(times))
