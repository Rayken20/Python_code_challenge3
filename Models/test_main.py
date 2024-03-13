from Author import Author
from Article import Article
from Magazine import Magazine


def test_article_creation_valid():
    # Valid article creation with author and title
    author1 = Author("John Doe")
    article = Article(author1, "A New Discovery")
    assert article.title == "A New Discovery"
    assert article.author == author1


def test_article_creation_invalid_author():
    # Invalid article creation with non-Author object
    author1 = Author("John Doe")
    try:
        Article("Not an Author", "Invalid Article")
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised for invalid author"


def test_article_creation_invalid_title_length_too_long():
    # Invalid article creation with title longer than 50 characters
    author1 = Author("John Doe")
    try:
        Article(author1, "This title is way too long to be valid according to the specification")
    except ValueError:
        pass
    else:
        assert False, "ValueError not raised for long title"


def test_article_author_association():
    # Test author association after article creation
    author1 = Author("John Doe")
    article = Article(author1, "Another Article")
    assert article in author1.articles()


def test_article_all_articles():
    # Test adding articles to the class-level list
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    article1 = Article(author1, "First")
    article2 = Article(author2, "Second")
    assert article1 in Article.all
    assert article2 in Article.all


def test_magazine_creation():
    # Test magazine creation with name and category
    magazine1 = Magazine("Science Weekly", "Science")
    assert magazine1.name == "Science Weekly"
    assert magazine1.category == "Science"


def test_magazine_article_association():
    # Test article association with magazine
    author1 = Author("John Doe")
    magazine1 = Magazine("Science Weekly", "Science")
    article = Article(author1, "Science Breakthrough", magazine1)
    assert article in magazine1.articles()


def test_magazine_article_titles():
    # Test retrieving article titles associated with a magazine
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine2 = Magazine("Tech Monthly", "Technology")
    article1 = Article(author1, "Tech News", magazine2)
    article2 = Article(author2, "AI Advancements", magazine2)
    


def test_magazine_top_publisher():
    # Test top publisher identification (consider adding more magazines for a more robust test)
    magazine1 = Magazine("Science Weekly", "Science")
    magazine2 = Magazine("Tech Monthly", "Technology")
    magazine1.add_article(Article(Author("Jane Smith"), "Another Science Article"))
    assert Magazine.top_publisher() == magazine1


# Run the tests
test_article_creation_valid()
test_article_creation_invalid_author()
# ... (call all other test functions)


print("All tests passed!")
