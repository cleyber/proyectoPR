import MySQLdb

db = MySQLdb.connect('localhost','root','','testdb')

cursor = db.cursor()
sql = """
        CREATE TABLE EMPLOYEE (
            firts_name varchar(20),
            last_name varchar(20),
            age int,
            sex char(1),
            income double
        );
      """
cursor.execute(sql)
data = cursor.fetchone()

print('Version de Db :%s' % data)

db.close()

