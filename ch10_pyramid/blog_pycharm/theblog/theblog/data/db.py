import pymongo


class DB:
    @staticmethod
    def get_books():
        client = pymongo.MongoClient()
        db = client.library
        return list(db.book.find())

    @staticmethod
    def add_book(title, price, pages):
        client = pymongo.MongoClient()
        db = client.library
        book = {
            'title': title,
            'price': price,
            'chapter_count': pages,
            'reviews': []
        }

        db.book.save(book)
        return book

    @classmethod
    def get_book(cls, bid):
        client = pymongo.MongoClient()
        db = client.library
        return db.book.find_one({'_id': bid})
