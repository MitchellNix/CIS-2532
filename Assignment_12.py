'''
    Author:     Mitchell Nix
    Date:       5/10/2020
    Progr:      ASsignment_12.py
    Descr:
        This is the progrmaing portion of assignment 12
        exercise 17.2 from the book



'''


import sqlite3
import pandas as pd

#sqlite3 < books.db books.sql
connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
pd.read_sql('SELECT * FROM titles', connection)

df = pd.read_sql('SELECT * FROM author_ISBN', connection)

df.head()

pd.read_sql('SELECT first, last FROM authors', connection)

pd.read_sql("""SELECT title, edition, copyright
FROM titles WHERE copyright > '2016'""", connection)

pd.read_sql("""SELECT id, first, last
FROM authors WHERE last LKE 'D%""", connection, index_col=['id'])

pd.read_sql("""SELECT id, first, last
FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])


pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""",
            connection, index_col=['id'])

pd.read_sql("""SELECT isbn, title, edition, copyright
FROM titles WHERE title LIKE '%How to Program'
ORDER BY title""", connection)


pd.read_sq("""SELECT first, last, isbn
FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id
ORDER BY last, first""", connection).head()
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('SUE', 'RED') """)

pd.read_SQL('SELECT id, first, last FROM authors',
            connection, index_col=['id'])

pd.read_sql('SELECT id, first, last, FROM authors', connection, index_col=['id'])

cursors = cursor.execute('DELETE FROM authors WHERE id=6')

pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])

pd.read_sql("""SELECT title, edition FROM titles
ORDER BY edition DESC""")

pd.read_sql("""SELECT * FROM authors 
WHERE first LIKE 'A%'""")

pd.read_sql("""SELECT isbn, title, edition, copyright
FROM titles WHERE title NOT LIKE '%How to Program'
ORDER BY title""", connection)