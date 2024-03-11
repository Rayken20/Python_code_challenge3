class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = self.contributors()
        return [author for author in authors if len(author.articles()) > 2]


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value


# Example usage:
author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

article1 = author1.add_article(magazine1, "Python Tips and Tricks")
article2 = author1.add_article(magazine1, "Understanding Neural Networks")
article3 = author2.add_article(magazine2, "Latest Fashion Trends")

print(article1.author.name)  # Output: John Doe
print(article1.magazine.name)  # Output: Tech Magazine

print(magazine1.contributing_authors())  # Output: [John Doe]
print(magazine1.article_titles())  # Output: ['Python Tips and Tricks', 'Understanding Neural Networks']
