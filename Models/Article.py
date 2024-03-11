from Author import Author
from Magazine import Magazine

class Article:
    all = []  

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self.__title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters long")

        self.__author = author
        self.__magazine = magazine
        Article.all.append(self)  

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine
