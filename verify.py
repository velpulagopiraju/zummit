#!C:\Users\Gopi Raj\AppData\Local\Programs\Python\Python311\python.exe

import cgi
import mysql
import mysql.connector

print('content-Type:text/html\r\n\r\n')

form = cgi.FieldStorage()
otp = form.getvalue('otp')
email = form.getvalue('email')
value = 1

conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
cur = conn.cursor()
query = 'update userdetails set email=%s where otp=%s'
update_data = (email,otp)
cur.execute(query,update_data)
conn.commit()
cur.close()
conn.close()

conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
cur = conn.cursor()
q_set = 'SELECT OTP FROM USERDETAILS'
cur.execute(q_set)
li = []
for i in cur:
    li.append(list(i)[0])
a = li[-1]
b = str(a)
conn.commit()
cur.close()
conn.close()

conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
cur = conn.cursor()
q_set1 = 'SELECT EMAIL FROM USERDETAILS'
cur.execute(q_set1)
li1 = []
for i in cur:
    li1.append(list(i)[0])
email1 = li1[-1]
li1.remove(email1)
conn.commit()
cur.close()
conn.close()
   
if email1 not in li1 and otp == str(a):
     conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
     cur = conn.cursor()
     query = 'update userdetails set verified=%s where email=%s'
     update_data = (value,email)
     cur.execute(query,update_data)
     conn.commit()
     cur.close()
     conn.close()
     print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/zummit3/index.html")+'" />')
     
else:
     try:
        conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
        cur = conn.cursor()
        q_set3 = 'DELETE FROM USERDETAILS WHERE otp = {}'.format(b)
        cur.execute(q_set3)
        conn.commit()
        cur.close()
        conn.close()
        print('enter correct otp')
        #print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/zummit-main/index.html")+'" />')
     except Exception as v:
         print(v)



          
     




