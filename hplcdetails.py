#!C:\Users\Gopi Raj\AppData\Local\Programs\Python\Python311\python.exe

print('content-Type:text/html\r\n\r\n')



import cgi
import mysql
import mysql.connector

form = cgi.FieldStorage()


n_samples=form.getvalue('samples')
type_hplc_1=form.getvalue('type1')
type_hplc_2=form.getvalue('type2')
type_columns=form.getvalue('columns')
no_injections=form.getvalue('injections')
nature_samples=form.getvalue('nature')
volume_samples=form.getvalue('volume')
method_analysis=form.getvalue('myfile')
method_is=form.getvalue('method')


conn = mysql.connector.connect(
user='root',password='',host='localhost',database='test')

cur = conn.cursor()
cur.execute("insert into hplcdetails values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (n_samples,type_hplc_1,type_hplc_2,type_columns,no_injections,nature_samples,volume_samples,method_analysis,method_is))

conn.commit()
cur.close()
conn.close()


print('<html>')
print('<head>')
print('<meta http-equiv="refresh" content="0;url='+str("http://localhost/zummit3/Page3.html")+'" />') 
print('</head>')
print('</html>')




