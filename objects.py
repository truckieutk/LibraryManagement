# Name: Thi Thanh Truc Kieu - Student ID: 101140870 - Topic: Library
class Book:
    def __init__(self, id=0, categoryID=0, title=None,
                 year=0, authorID=None):
        self.id = id
        self.categoryID = categoryID
        self.title = title
        self.year= year
        self.authorID = authorID


class Category:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name


class Author:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name
