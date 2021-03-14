# Name: Thi Thanh Truc Kieu - Student ID: 101140870 - Topic: Library
import sqlite3
from contextlib import closing

conn = sqlite3.connect("libraries.sql")
conn.row_factory = sqlite3.Row

try:
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Book'''
        c.execute(query)
        musics = c.fetchall()
except sqlite3.OperationalError as e:
    print("Error reading database -", e)
    books = None


if books is not None:
    for book in books:
        print(books["title"], "|", books["year"])
    print()

