# Name: Thi Thanh Truc Kieu - Student ID: 101140870 - Topic: Library
import sys
import os
import sqlite3
from contextlib import closing
from objects import Category
from objects import Author
from objects import Book

conn = None


def connect():
    global conn
    if not conn:
        if sys.platform == "win64":
            DB_FILE = "libraries.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "libraries.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def make_category(row):
    return Category(row["categoryID"], row["categoryName"])


def make_author(row):
    return Author(row["authorID"], row["authorName"])


def make_book(row):
    return Book(row["bookID"], make_category(row), row["title"], row["year"], make_author(row))


def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories


def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()

    category = make_category(row)
    return category


def get_authors():
    query = '''SELECT authorID, name as authorName
               FROM Author'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    authors = []
    for row in results:
        authors.append(make_author(row))
    return authors


def get_books(book_id):
    query = '''SELECT bookID, Music.categoryID as categoryID, title, year,
                          Music.authorID as authorID,
                          Category.name as categoryName, Author.name as authorName
                   FROM Book JOIN Category
                          ON Book.categoryID = Category.categoryID
                          JOIN Author on Book.authorID = Author.authorID
                   WHERE Book.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        results = c.fetchall()

        book_chosen = []
        for row in results:
            book_chosen.append(make_book(row))
            return book_chosen


def get_author(author_id):
    query = '''SELECT authorID, name AS authorName
               FROM Author WHERE authorID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (author_id,))
        row = c.fetchone()

    author = make_author(row)
    return author


def search_book_by_category(category_id):
    query = '''SELECT bookID, Music.categoryID as categoryID, title, year,
                      Music.authorID as authorID,
                      Category.name as categoryName, Author.name as authorName
               FROM Book JOIN Category
                      ON Book.categoryID = Category.categoryID
                      JOIN Author on Book.authorID = Author.authorID
               WHERE Book.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

        books = []
        for row in results:
            books.append(make_book(row))
            return books


def search_book_by_author(author_id):
    query = '''SELECT bookID, Music.categoryID as categoryID, title, year,
                      Music.authorID as authorID,
                      Category.name as categoryName, Author.name as authorName
               FROM Book JOIN Category
                      ON Book.categoryID = Category.categoryID
                      JOIN Author on Book.authorID = Author.authorID
               WHERE Book.authorID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (author_id,))
        results = c.fetchall()

        books = []
        for row in results:
            books.append(make_book(row))
            return books


def search_book_by_title(title):
    query = '''SELECT bookID, Music.categoryID as categoryID, title, year,
                      Music.authorID as authorID,
                      Category.name as categoryName, Author.name as authorName
               FROM Book JOIN Category
                      ON Book.categoryID = Category.categoryID
                      JOIN Author on Book.authorID = Author.authorID
               WHERE title = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (title,))
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books


def search_book_by_id(book_id):
    query = '''SELECT bookID, Music.categoryID as categoryID, title, year,
                      Music.authorID as authorID,
                      Category.name as categoryName, Author.name as authorName
               FROM Book JOIN Category
                      ON Book.categoryID = Category.categoryID
                      JOIN Author on Book.authorID = Author.authorID
               WHERE bookID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (book_id,))
        results = c.fetchall()

    books = []
    for row in results:
        books.append(make_book(row))
    return books
