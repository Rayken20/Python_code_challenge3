class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []  # Initialize empty list to hold articles

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        """
        Method to add an article to the author's list of articles.
        """
        self._articles.append(article)  # Add article to the list of articles associated with the author

    def articles(self):
        return self._articles

    def magazines(self):
        """
        Method to retrieve a list of magazines the author has contributed to.
        """
        return list(set(article.magazine for article in self._articles if hasattr(article, 'magazine')))

    def topic_areas(self):
        """
        Method to retrieve a list of topic areas the author has contributed to.
        """
        categories = []
        for article in self._articles:
            if hasattr(article, 'magazine') and hasattr(article.magazine, 'category'):
                categories.append(article.magazine.category)
        return list(set(categories))
