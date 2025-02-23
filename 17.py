#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
mysql.connector.connect(host = 'localhost', database = 'test', user = 'root', password = '')

'''
connect.ini file example

[mysql]
host = localhost
database = test
user = root
password = 

'''

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print('Total Row(s):', cursor.rowcount)
for row in rows:
    print(row)
    
cursor.close()

SELECT * FROM users LIMIT 0, 50
SELECT * FROM users LIMIT 50, 50

def iter_row(cursor, size = 10):
    while True:
        rows = cursor.fetchmany(size)
        
        if not rows:
            break
        
        for row in rows:
            yield row

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
for row in iter_row(cursor, 10):
    print(row)
    
if cursor.lastrowid:
    print('last insert id', cursor.lastrowid)
else:
    print('last insert id not found')

def add_user(login, psswrd):
    query = "INSERT INTO users(login, psswrd) VALUES(%s, %s)" 
    args = (login, psswrd)
    
    cursor = conn.cursor()
    cursor.execute(query, args)
    
    if cursor.lastrowid:
        print('last insert id', cursor.lastrowid)
    else:
        print('last insert id not found')
        
    conn.commit()
    cursor.close()

add_user('john', '12345')
