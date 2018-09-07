#variables and libraries imported
import mysql.connector
from datetime import datetime
from avgFunc import avg

#Create conecction
cnx = mysql.connector.connect(user = 'root', password = '154198280aA',
                      host = '127.0.0.1',
                      database = 'test')
#Create cursor
cursor = cnx.cursor()

#Query 1
timesQuery1 = []
query1 = ("SELECT * FROM person "
          "WHERE age=25")
for i in range(0,10):
    d1 = datetime.now()
    cursor.execute(query1)
    data1 = cursor.fetchall()
    print (data1)
    cnx.commit()
    query1_time = datetime.now() - d1
    timesQuery1.append(query1_time)

#Query 2
timesQuery2 = []
query2 = ("SELECT * FROM person "
          "WHERE age BETWEEN 35 AND 45")
for i in range(0,10):
    d2=datetime.now()
    cursor.execute(query2)
    data2 = cursor.fetchall()
    print (data2)
    cnx.commit()
    query2_time = datetime.now() - d2
    timesQuery2.append(query2_time)

#Query 3
timesQuery3 = []
query3 = ("SELECT count(*) FROM person "
          "WHERE age BETWEEN 20 AND 60")
for i in range(0,10):
    d3=datetime.now()
    cursor.execute(query3)
    data3 = cursor.fetchall()
    print (data3)
    cnx.commit()
    query3_time = datetime.now() - d3
    timesQuery3.append(query3_time)

#Query 4
timesQuery4 = []
query4 = ("SELECT count(*) FROM person "
          "WHERE nick LIKE '%Vv%'")
for i in range(0,10):
    d4=datetime.now()
    cursor.execute(query4)
    data4 = cursor.fetchall()
    print (data4)
    cnx.commit()
    query4_time = datetime.now() - d4
    timesQuery4.append(query4_time)

#Query 5
timesQuery5 = []
query5 = ("SELECT * FROM person "
          "WHERE nick LIKE '%Vv%' ORDER BY age DESC")
for i in range(0,10):
    d5=datetime.now()
    cursor.execute(query5)
    data5 = cursor.fetchall()
    print (data5)
    cnx.commit()
    query5_time = datetime.now() - d5
    timesQuery5.append(query5_time)

print ("Avantage time for Query 1: ", avg(timesQuery1))
print ("Avantage time for Query 2: ", avg(timesQuery2))
print ("Avantage time for Query 3: ", avg(timesQuery3))
print ("Avantage time for Query 4: ", avg(timesQuery4))
print ("Avantage time for Query 5: ", avg(timesQuery5))

cursor.close()
cnx.close()
