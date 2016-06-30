import json
import requests
# url = 'http://127.0.0.1:6543/api/book/57750abe25ca7609a8aeb28a'
#
# resp = requests.get(url)
# book = resp.json()
# print(book)

print("Your turn to make a book!")
title = input("Title: ")
price = float(input("Price: "))
chapter_count = int(input("chapter_count: "))

book = dict(title=title, price=price, chapter_count=chapter_count)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
create_url = 'http://127.0.0.1:6543/api/add_book'
book = requests.post(create_url, json.dumps(book), headers=headers)
print("New book: {}".format(book.json()))
