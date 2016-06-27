from xml.etree import ElementTree
import requests

from blogpost import BlogPost

resp = requests.get('http://feeds.feedburner.com/Pycharm')
xml_data = resp.text

dom = ElementTree.fromstring(xml_data)
print(dom)

for item in dom.findall('channel/item'):
    post = BlogPost.from_xml(item)

    # post = BlogPost()
    # post.load_from_xml(item)
    print(post.to_json())

    print('{} (at {})'.format(post.title, post.link))



