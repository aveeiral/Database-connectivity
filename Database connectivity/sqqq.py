# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:50:37 2020

@author: Aviral Gaur
"""

import sqlite3 as sq
import pandas as pd

# 1.connect to database
#2. crete object for cursor
# 3.close all connection at the end
dataset = pd.read_csv("MOCK_DATA.csv")
conn = sq.connect('mydata31_new.db')
obj = conn.cursor()

# we create table only once
obj.execute("create table new_data1 (id REAL, first_name TEXT, last_name TEXT, email TEXT, gender TEXT, bill REAL)")
conn.commit()

for i in range(0, 10):
    da = dataset.iloc[i, 0:6].values
    obj.execute("INSERT INTO new_data1 VALUES(?, ?, ?, ?, ?, ?)", (int(da[0]), da[1], da[2], da[3], da[4], int(da[5])))
    conn.commit()
    
   

obj.execute("SELECT first_name FROM new_data1 WHERE bill>2000 ")
result = obj.fetchall()
print(result)


conn.close()
obj.close()
 