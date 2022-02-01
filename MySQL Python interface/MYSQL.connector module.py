import mysql.connector
p = 'root'

db1 = mysql.connector.connect(host = 'localhost', user = 'root' \
, password = p, database = 'classicmodels' \
, auth_plugin = 'mysql_native_password')


'''Checking whether database is connected or not'''


if db1.is_connected():
    print('connected')
else:
    print('Not connected')


'''Saving changes and Closing a connection'''


db1.commit()
#this function saves what we have done in this particular connection
db1.close()
#this function closes the connection


'''Creating a cursor object and how to use it'''


db2 = mysql.connector.connect(host = 'localhost', \
user = 'root', password = p, auth_plugin = 'mysql_native_password')

mycursor = db2.cursor()

# mycursor.execute('CREATE DATABASE SCHOOL')
'''Since this database already exists, executing this command again
will give a traceback'''


'''Looking at all the databases'''


mycursor.execute('SHOW DATABASES')
for database in mycursor:
    print(database)
mycursor.execute('use classicmodels')


'''Looking at all the tables'''

mycursor.execute('SHOW TABLES')
for table in mycursor:
    print(table)


'''Creating a table at run time'''


db3 = mysql.connector.connect(host = 'localhost', \
user = 'root', password = p, database = 'classicmodels', auth_plugin = 'mysql_native_password')
mycursor = db3.cursor()
# mycursor.execute('CREATE TABLE STUDENTS(ROLL_number int(3) primary key \
# , Name varchar(20), Age int(2))')


'''Fetchall() Method'''
#The method fetches all (or all remaining) rows of a query result set 
# and returns a list of tuples. If no more rows are available, it 
# returns an empty list.

'''Looking at Records'''
mycursor.execute('select * from offices')
records = mycursor.fetchall()
print(records)

'''Looking at Tables'''
mycursor.execute('show tables')
tables = mycursor.fetchall()
for table in tables:
    print(table)