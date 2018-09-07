#variables and libraries imported
import pymongo
from pymongo import MongoClient
from datetime import datetime
import pprint
from avgFunc import avg

client = MongoClient()

db = client.test

collection = db.person

#Query 1
times1 = []
for i in range(0,10):
    d1 = datetime.now()
    for data in collection.find({"age":25}):
        pprint.pprint(data)
    query1_time = datetime.now() - d1
    times1.append(query1_time)

#Query 2
times2 = []
for i in range(0,10):
    d2 = datetime.now()
    for data in collection.find({"age":{"$gte":20,"$lte":50}}):
        pprint.pprint(data)
    query2_time = datetime.now() -d2
    times2.append(query2_time)

#Query 3
times3 = []
for i in range(0,10):
    d3 = datetime.now()
    pprint.pprint(collection.count({"age":{"$gte":20,"$lte":50}}))
    query3_time = datetime.now() - d3
    times3.append(query3_time)

#Query 4
times4 = []
for i in range(0,10):
    d4 = datetime.now()
    pprint.pprint (collection.count({"nick":{"$regex":"Vv"}}))
    query4_time = datetime.now() - d4
    times4.append(query4_time)

#Query 5
times5 = []
for i in range(0,10):
    d5 = datetime.now()
    for data in collection.find({"nick":{"$regex":"Vv"}}).sort("age",pymongo.DESCENDING):
        pprint.pprint(data)
    query5_time = datetime.now() - d5
    times5.append(query5_time)

print ("Avantage time for Query 1: ", avg(times1))
print ("Avantage time for Query 2: ", avg(times2))
print ("Avantage time for Query 3: ", avg(times3))
print ("Avantage time for Query 4: ", avg(times4))
print ("Avantage time for Query 5: ", avg(times5))
