from Article import Article
from Author import Author

class Magazine:
    all_magazines = []  

    def __init__(self, name, category):
        self.__name = name
        self.__category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))

    def contributing_authors(self):
        authors = self.contributors()
        author_counts = {author: sum(1 for article in self.articles() if article.author == author) for author in authors}
        contributing_authors = [author for author, count in author_counts.items() if count > 2 and isinstance(author, Author)]
        if not contributing_authors:
            return None
        return contributing_authors

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_article_counts = {magazine: len(magazine.articles()) for magazine in cls.all_magazines}
        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get)
        return top_magazine
