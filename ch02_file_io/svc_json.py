import requests
# import json
import csv

# r = csv.DictReader(csvFile)
# for row in r:
#     title = r['Title']

search = input("Search for a movie? What's the title: ")
url = 'http://www.omdbapi.com/?&y=&plot=short&r=json&s=' + search

resp = requests.get(url)
print(resp.headers)
#data = json.loads(resp.text)
data = resp.json()
print(type(data), data)
data = data['Search']

for m in data:
    print(m['Title'])