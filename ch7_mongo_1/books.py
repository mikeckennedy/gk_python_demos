import pymongo
from bson import ObjectId, SON


def main():
    db = connect()
    count(db)
    search(db)

def connect():
    client = pymongo.MongoClient(document_class=SON)
    db = client.bookstore
    return db

def count(db):
    c = db.Book.count()
    print("There are {:,} books".format(c))


def search(db):
    book_id = ObjectId("525867313a93bb2198103c13")
    book = db.Book.find_one({'_id': book_id})
    print(type(book))
    print("Found book: {}".format(book))

    user_id = ObjectId("525867833a93bb21981567fc")
    books = db.Book.find({"Ratings.UserId": user_id})
    print("Books rated by the user:")
    for b in books:
        print(" * " + b['Title'])





if __name__ == '__main__':
    main()



# client = pymongo.MongoClient()
# db = client.accounting
# db.payables.save({'due_to': 'jeff', 'value': 50000})
#  rows = db.payables.find({'due_to': 'jeff'})
#  for r in rows:
#      print(r)