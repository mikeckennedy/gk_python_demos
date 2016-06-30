import mongoengine

from models import Book, Review


def setup_db():
    mongoengine.register_connection('default', name='library')


def add_some_data():
    if Book.objects().count():
        print("Data already loaded")
        return

    print("Loading data...")

    book = Book(title="The big mongo book", price=7.99, chapter_count=10)
    book.reviews.append(Review(stars=7))
    book.reviews.append(Review(stars=9))
    book.reviews.append(Review(stars=8))
    book.save()

    book = Book(title="PHP: Winning on the internet", price=47.99, chapter_count=100)
    book.reviews.append(Review(stars=1))
    book.reviews.append(Review(stars=0))
    book.reviews.append(Review(stars=0))

    book.save()


def run_query():
    bad_books = Book.objects(reviews__stars=0)
    print("Bad books!")
    for b in bad_books:
        print(b.title)




