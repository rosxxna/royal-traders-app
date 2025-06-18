import mysql.connector
from socket import *
import datetime
import pickle

HOST = 'localhost'
PORT = 8745

ADDRESS = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDRESS)

s.listen(5)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='1234',
    database="trading"
)
mycursor = mydb.cursor()


(client, address) = s.accept()
bin_data=client.recv(1024)
data = pickle.loads(bin_data)
user = data[0]
amount = data[1]
plan = data[2]
date = datetime.date.today()

# Get the user ID from the SQL database
sql = f"SELECT userid FROM login WHERE username = '{user}'"
mycursor.execute(sql)
result = mycursor.fetchone()
if result:
    userid = result[0]

# Insert the transaction data into the SQL database
sql = f"INSERT INTO transaction (userid, amount, type, date) VALUES ('{userid}', '{amount}', '{plan}', '{date}')"
mycursor.execute(sql)
mydb.commit()

'''sql=f"select * from transaction where userid='{userid}';"
mycursor.execute(sql)
d = mycursor.fetchall()
bin_val=pickle.dumps(d)
client.send(bin_val)'''

       
client.close()
