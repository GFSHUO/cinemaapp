# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:30:20 2019

@author: Continental
"""

import sqlite3  


conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (\'1\', \'seven bai\')')

cursor.execute('select * from user where id=?', ('1',))

cursor.rowcount

values = cursor.fetchall()
print(values)