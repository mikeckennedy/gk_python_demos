import json

class BlogPost:
    def __init__(self, title=None, link=None):
        self.link = link
        self.title = title

    # @staticmethod
    # def from_xml(item_dom):
    #     post = BlogPost()
    #     post.title = item_dom.find('title').text
    #     post.link = item_dom.find('link').text
    #
    #     return post

    @classmethod
    def from_xml(cls, item_dom):
        post = cls()
        post.title = item_dom.find('title').text
        post.link = item_dom.find('link').text

        return post

    def load_from_xml(self,item_dom):
        self.title = item_dom.find('title').text
        self.link = item_dom.find('link').text

    def to_json(self):
        return json.dumps(self.__dict__)
