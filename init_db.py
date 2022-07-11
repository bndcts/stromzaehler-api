import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO mapping (uuid, partei, art, bezug) VALUES (?, ?, ?, ?)",
            ('cf3d8c00-faf3-11ec-a111-b59a0b0d2484', 'Benedikt', 'Zaehlerstand', '1')
            )

cur.execute("INSERT INTO mapping (uuid, partei, art, bezug) VALUES (?, ?, ?, ?)",
            ('74cae800-faf5-11ec-909a-e56ba089e4a1', 'Benedikt', 'Leistung', '1')
            )

connection.commit()
connection.close()