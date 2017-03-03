import mysql.connector
def getNextId():
    cnx = mysql.connector.connect(host='localhost', database='test')
    cursor = cnx.cursor()
    cursor.execute("select max(id)+1 as newId from employee")
    row = cursor.fetchone()
    maxValue = row[0]
    cursor.close()
    cnx.commit()
    cnx.close()
    return maxValue

print(getNextId())
