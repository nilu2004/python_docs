import mysql.connector
from mysql.connector import errorcode

def getNextId(dbconnection):
    cursor = dbconnection.cursor()
    cursor.execute("select max(id)+1 as newId from employee")
    row = cursor.fetchone()
    maxValue = row[0]
    cursor.close()
    return maxValue


try:
    cnx = mysql.connector.connect(host='localhost',database='test')
    print('connection established')

    cursor = cnx.cursor()

    insert_query_positional = ("INSERT INTO employee VALUES (%s, %s)")
    nextEmployeeId = getNextId(cnx)
    print("new id :: {}", nextEmployeeId)
    data_positional = (nextEmployeeId, 'ramesh')

    cursor.execute(insert_query_positional, data_positional)
    print("insert successfull for positional parameter")

    insert_query_named = ("INSERT INTO employee VALUES (%(id)s, %(name)s)")
    nextEmployeeId = getNextId(cnx)
    data_named = {"id":nextEmployeeId, "name":"sachin"}

    cursor.execute(insert_query_named, data_named)
    print("insert successfull for named parameter")

    print("populating all records from employee table")
    cursor.execute("Select * from employee")
    for (id, name) in cursor:
        print("id={}, name={}", id, name)

    cursor.close();
    cnx.commit();
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("something else happened :: ",err)
else:
    cnx.close()


