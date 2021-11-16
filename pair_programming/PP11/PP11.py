# coder: Selina Qian
# Listener: Yichun Yao, Feng Ling

import sqlite3
import pandas as pd


pd.set_option('display.width', 500)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)

db = sqlite3.connect('PP11.sqlite')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

with open ("candidates.txt") as candidates:
    next(candidates) # jump over the header
    for line in candidates.readlines():
        cid, first_name, last_name, middle_name, party = line.strip().split('|')
        vals_to_insert = (int(cid), first_name, last_name, middle_name, party)
        cursor.execute('''INSERT INTO candidates 
                  (id, first_name, last_name, middle_init, party)
                  VALUES (?, ?, ?, ?, ?)''', vals_to_insert)
db.commit()

cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
print(all_rows)

db.close()

