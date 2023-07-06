#!C:\Users\Gopi Raj\AppData\Local\Programs\Python\Python311\python.exe

import cgi
import mysql
import mysql.connector
import random
import math
import smtplib

print('content-Type:text/html\r\n\r\n')

form = cgi.FieldStorage()
email=form.getvalue('email')
name=form.getvalue('name')
organization=form.getvalue('organization')
designation=form.getvalue('designation')
verified = 0

def generate_otp():
    digits = '123456789'
    otp = ''
    for i in range(6):
        otp += digits[math.floor(random.random()*10)]
    return otp
otp = generate_otp()

conn = mysql.connector.connect(
user='root',password='',host='localhost',database='test')
cur = conn.cursor()

cur.execute("insert into userdetails values (%s,%s,%s,%s,%s,%s)",
            (email,name,organization,designation,otp,verified))

conn.commit()
cur.close()
conn.close()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("#####@gmail.com","#########")
emailid = '##########@gmail.com'
s.sendmail('########@gmail.com',emailid,'your otp is '+otp)
a = otp
if a == otp:
    print(a)
else:
    print("Please Check your OTP again")






