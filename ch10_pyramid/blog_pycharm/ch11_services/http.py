import requests

search = input("Enter a title to search for: ")
url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s=cat'.format(search)

resp = requests.get(url)
if resp.status_code != 200:
    print("Yikes, didn't work, we got: {}".format(resp.status_code))

print(resp.headers)