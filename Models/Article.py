from Author import Author


class Article:
    all = []  # Define 'all' as a class attribute

    def __init__(self, author, title, magazine=None):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self.__title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters long")

        self.__author = author  # Establish association with author
        self.__magazine = magazine  # Optionally associate with a magazine
        self.__author.add_article(self)  # Add this article to the author's list of articles
        Article.all.append(self)  # Add this article to the list of all articles

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine
