# MongoDB-MySQL

Los scripts escritos en este repositorio estan destinados a relizar operaciones con datos en dos bases de datos muy populares. Por un lado tenemos a MySQL, la base de datos relacional más utilizada. Por otro lado tenemos a MongoDB, una de las bases de datos NoSQL que más a evolucionado y crecido en su categoria. El objetivo es comparar el rendimiento que tienen estos dos motores de bases de datos utilizando consultas como INSERT, SELECT o DELETE, entre otras, mediante los escripts escritos en lenguaje Python.

# Creación de una base de datos

Los scripts testMySQL.py y testMongo.py se encargan de crear una base de datos denominada 'test', y una tabla (colleccion en MongoDB) con los atributos 'id', 'nick' y 'age'. Se realizan 10 iteraciones de INSERTs con 1.000.000 de inserciones de datos aleatorios. Al finalizar el proceso, cada base de datos tendra un total de 10.000.000 de datos cargados, no necesariamente iguales, dado que los datos se generaron aleatoriamente por separado en ambos scripts.

# Test de Consultas 

Los scripts queryMySQL.py y queryMongoDB.py realizan consultas a MySQL y MongooDB respectivamente. Se realizan cinco (5) consultas diferentes, realizando 10 iteraciones de cada una de las mismas. Los datos obtenidos en cada consulta son visualizados en consola y al finalizar el script, se presenta el resultado del tiempo promedio para cada consulta.

    # Query 1-1: Todos los campos de las entidades donde el campo "age" = 25.
    # Query 1-2: Todos los campos de las entidades donde el campo "age" tenga valores entre 35 y 45.
    # Query 1-3: La cantidad de entidades donde su campo "age" tenga valores entre 20 y 60
    # Query 1-4: La cantidad de entidades donde su campo "nick" contenga la expresion "Vv".
    # Query 1-5: Todos los campos de las entidades donde el campo "nick" contenga la expresio "Vv" y ordenados con respecto al campo "age" de manera descendente.

# Scripts adicionales

avgFun.py
    Posee una funcion denominada 'avg' la cual recibe un vector de datos en formato 'timedelta', retornando como resultado el valor promedio de los valores almacenados en el mismo.
