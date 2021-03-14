#!/usr/bin/env/python3
# Name: Thi Thanh Truc Kieu - Student ID: 101140870 - Topic: Library

import db
from objects import Book
from datetime import date


def display_menu():
    print("Welcome to the GBC library. Please choose the options below.")
    print()
    print("COMMAND MENU")
    print("category  - View books by category")
    print("author  - View books by author")
    print("title - View books by title")
    print("add  - Add a book")
    print("del  - Delete a book")
    print("print  - Print receipt")
    print("exit - Exit program")
    print()


def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()


def display_authors():
    print("AUTHORS")
    authors = db.get_authors()
    for author in authors:
        print(str(author.id) + ". " + author.name)
    print()


def display_books(books, title):
    print("BOOKS - " + title)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Category", "Title", "Year",
                             "Author"))
    print("-" * 64)
    for book in books:
        print(line_format.format(str(book.id), book.category.name,
                                 str(book.title),
                                 str(book.year),
                                 book.author.name))
    print()


def display_books_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category is None:
        print("There is no category with that ID.\n")
    else:
        print()
        books = db.search_book_by_category(category_id)
        display_books(books, category.name.upper())


def display_books_by_author():
    author_id = int(input("Author ID: "))
    author = db.get_author(author_id)
    if author is None:
        print("There is no author with that ID.\n")
    else:
        print()
        books = db.search_book_by_author(author_id)
        display_books(books, author.name.upper())


def display_books_by_title():
    title = str(input("Title: "))
    print()
    books = db.search_book_by_title(title)
    display_books(books, title)


def get_cart(cart_list):
    print("LIST BOOKS")
    print()
    if len(cart_list) == 0:
        print("There are no books in the cart.\n")
        return
    else:
        i = 1
        for row in cart_list:
            line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
            print(line_format.format("ID", "Category", "Title", "Year",
                                     "Author"))
            print("-" * 64)
            print(line_format.format(str(row.id), row.category.name,
                                     str(row.title),
                                     str(row.year),
                                     row.author.name))
            print()
            i += 1
        print()
        today = date.today()
        d1 = today.strftime("%m/%d/%y")
        print("Date of borrowing: ", d1)
        dateReturn = int(d1) + 14
        print("Date of returning: ", dateReturn)


def add_cart(cart_list):
    book_id = int(input("Book ID: "))

    confirm = str(input("Add to cart: y/n?"))
    if confirm is "y":
        db.search_book_by_id(book_id)
        if book_id is None:
            print("There is no book with that ID. " +
                  "Book NOT added.\n")
        else:
            book_chosen = []
            book_chosen
            cart_list.append(book_chosen)
            print("Book IDs " + str(book_chosen) + " was added to cart. \n")

    else:
        print("See another options")


def delete_item(cart_list):
    book_id = int(input("Book ID: "))
    if book_id < 1 or book_id > len(cart_list):
        print("Invalid book number.\n")
    else:
        book = cart_list.pop(book_id - 1)
        print("Book ID " + str(book_id) +
              " was deleted from cart.\n")


def main():
    db.connect()
    display_books()
    display_authors()
    display_categories()
    cart_list = []
    while True:
        command = input("Command: ")
        if command == "category":
            display_books_by_category()
        elif command == "author":
            display_books_by_author()
        elif command == "title":
            display_books_by_title()
        elif command == "add":
            add_cart(cart_list)
        elif command == "del":
            delete_item(cart_list)
        elif command == "print":
            get_cart(cart_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")


if __name__ == "__main__":
    main()
