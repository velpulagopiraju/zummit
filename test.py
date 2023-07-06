#!C:\Users\Gopi Raj\AppData\Local\Programs\Python\Python311\python.exe


import cgi
import mysql
import mysql.connector

print('content-Type:text/html\r\n\r\n')

form = cgi.FieldStorage()

name=form.getvalue('name')
organization=form.getvalue('organization')
designation=form.getvalue('designation')

conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
cur = conn.cursor()

q_set1 = 'SELECT EMAIL FROM USERDETAILS'
cur.execute(q_set1)
li = []
for i in cur:
    li.append(list(i)[0])
email = li[-1]
li.remove(email)

q_set2 = 'SELECT verified FROM USERDETAILS'
cur.execute(q_set2)
li1 = []
for i in cur:
    li1.append(list(i)[0])
value = li1[-1]

conn.commit()
cur.close()
conn.close()

for i in li1:
     if (i == 0):
          conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
          cur = conn.cursor()
          q_set3 = 'DELETE FROM USERDETAILS WHERE verified = {}'.format(0)
          cur.execute(q_set3)
          conn.commit()
          cur.close()
          conn.close()


if (email not in li) and (value == 1):
      conn = mysql.connector.connect(user='root',password='',host='localhost',database='test')
      cur = conn.cursor()
      query = 'update userdetails set name=%s,organization=%s,designation=%s where email=%s'
      update_data = (name,organization,designation,email)
      cur.execute(query,update_data)
      conn.commit()
      cur.close()
      conn.close()
      print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/zummit3/Page2.html")+'" />')
      
else:
      print('email is already registerd...')
     
            
            
    
    
        
        
            

