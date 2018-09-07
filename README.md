# MongoDB-MySQL

Los scripts escritos en este repositorio estan destinados a relizar operaciones con datos en dos bases de datos muy populares. Por un lado tenemos a MySQL, la base de datos relacional más utilizada. Por otro lado tenemos a MongoDB, una de las bases de datos NoSQL que más a evolucionado y crecido en su categoria. El objetivo es comparar el rendimiento que tienen estos dos motores de bases de datos utilizando consultas como INSERT, SELECT o DELETE, entre otras, mediante los escripts escritos en lenguaje Python.

# Creación de una base de datos

Los scripts testMySQL.py y testMongo.py se encargan de crear una base de datos denominada 'test', y una tabla (colleccion en MongoDB) con los atributos 'id', 'nick' y 'age'. Se realizan 10 iteraciones de INSERTs con 1.000.000 de inserciones de datos aleatorios.

# Scripts adicionales

avgFun.py
    Posee una funcion denominada 'avg' la cual recibe un vector de datos en formato 'timedelta', retornando como resultado el valor promedio de los valores almacenados en el mismo.
