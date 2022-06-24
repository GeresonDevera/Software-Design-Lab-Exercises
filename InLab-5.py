import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("create table lang(name,First_appeared")

cursor.execute("insert into lang values (?,?)", ("C", 2001))

lang_list = [
    ("Gereson De Vera", 2001),
    ("Engr. Jay-Ar Pentacostes"),
    ("Engineering",2020),
]
cursor.executemany("insert into lang values (?,?)", lang_list)

cursor.execute("select * from where First_appeared:year", {"year": 1995})
print(cursor.fetchall())

conn.close()