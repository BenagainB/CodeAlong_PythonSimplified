# sqlite.py
""" SQLite Backend for Beginners """
import os
import sqlite3

# Have to remove prior existing file gta.db or it interferes with loading/saving
path = 'gta.db'
if os.path.isfile(path):
    os.remove(path)


## Create SQLite DB
connection = sqlite3.connect("gta.db")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
]


## SQL Cursor Object
cursor = connection.cursor()


## Insert rows of data into a table
cursor.execute("create table gta (release_year integer, release_name text, city text)")
cursor.executemany("insert into gta values (?,?,?)", release_list)


## Select and print database rows
for row in cursor.execute("select * from gta"):
    print(row)
print("")


## Print filtered rows
cursor.execute("select * from gta where city=:c", {"c":"Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)
print("")


## Combine tables
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City", "New York City"))
cursor.execute("select * from cities where gta_city=:c", {"c":"Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)
print("")


## Manipulate database data
for i in gta_search:
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjusted)

connection.close()
