import requests

search = input("Enter a title to search for: ")
url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s={}'.format(search)

resp = requests.get(url)
if resp.status_code != 200:
    print("Yikes, didn't work, we got: {}".format(resp.status_code))

# print(resp.headers)
# import json

# data = json.loads(resp.text)
# print(data)

data = resp.json()
data = data['Search']

for m in data:
    print(" * {} {}".format(m['Year'], m['Title']))

