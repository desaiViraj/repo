import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS albums(title text,artist text,release_date text,publisher text,media_type text)""")

cursor.execute("INSERT INTO albums VALUES ('Glow','Hunter','7/24/2017','Rec','MP3')")
conn.commit()

albums = [('Exodus','Mr.Bone','7/10/2017','Rec0','MP3'),('Hound','Armour','17/06/2017','Rec','CD'),('Jon','Snow','12/12/2017','Rec','CD'),('Tyrion','Lannister','12/05/2015','Rec','MP3')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",albums)
conn.commit()


sql = "SELECT * from albums"
cursor.execute(sql)
print(cursor.fetchall())
