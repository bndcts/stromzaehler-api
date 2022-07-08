import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO zaehlerstaende (id, uuid, stand) VALUES (?, ?, ?)",
            (1,'Testabc', '8803')
            )

cur.execute("INSERT INTO zaehlerstaende (uuid, stand) VALUES (?, ?)",
            ('Testabc3', '2')
            )

connection.commit()
connection.close()