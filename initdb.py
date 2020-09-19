import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO posts(title,content) VALUES (?,?)",
    ('First post', 'hola este es el primer posteo de mi blog')
)

cursor.execute(
    "INSERT INTO posts(title,content) VALUES (?,?)",
    ('Another post', 'otro posteo mas')
    
)

connection.commit()
connection.close()