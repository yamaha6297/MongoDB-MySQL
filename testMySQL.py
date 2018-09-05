#variables and libraries imported
import mysql.connector
import random
from datetime import datetime
from random import sample
from string import digits, ascii_letters
from avgFunc import avg
from mysql.connector import errorcode

#code lines to create db 'test' and table 'person'
db = 'test'
name_table = 'person'
table = ("create table `person` ("
        "`id` int auto_increment not null,"
        "`nick` char(8) not null,"
        "`age` int not null,"
        "primary key(`id`))")
#create conection
cnx = mysql.connector.connect(user='root', password='154198280aA',
                              host='127.0.0.1')

#create cursor
cursor = cnx.cursor()

#function to create db
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
create_database(cursor)
cnx.database = db

#query to insert data
add_query = ("INSERT INTO person "
            "(nick,age) "
            "VALUES (%s,%s)")

#to create table
try:
        print("Creating table {}: ".format(name_table), end='')
        cursor.execute(table)
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
else:
    print("OK")

print ("Insertion times for 10 iterations: \n")
#variable to store times every 1000000 inserts
times = []
#insert 1000000 records
for i in range(0,10):
    d1=datetime.now()
    for n in range(0,1000000):
        chars = digits + ascii_letters
        cadena = ''.join(sample(chars, 8))
        #data to insert
        data_insert = (cadena,random.randint(18,90))
        #run insert
        cursor.execute(add_query,data_insert)
    #confirm transaction
    cnx.commit()
    #time of execution of the query
    time = datetime.now() - d1
    print (time)
    times.append(time)

print ("Avarage time: ", avg(times))
#close conection
cnx.close()
