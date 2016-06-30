import bson
from pyramid_handlers import action
import pyramid.response as r

from theblog.controllers.base_controller import BaseController
from theblog.data.db import DB


class ApiController(BaseController):

    @action(renderer='json')
    def books(self):
        books = DB.get_books()
        return [
            {'title': b['title'], 'price': b['price'], 'id': str(b['_id'])}
            for b in books
        ]

    @action(renderer='json',
            name='book',
            request_method='GET')
    def get_book(self):

        bid = self.request.matchdict.get('id')
        b = DB.get_book(bson.ObjectId(bid))
        return {'title': b['title'], 'price': b['price'], 'id': str(b['_id'])}

    @action(renderer='json',
            name='add_book',
            request_method='POST')
    def add_book(self):
        book = self.request.json_body

        b = DB.add_book(book['title'], book['price'], book['chapter_count'])
        return {'title': b['title'], 'price': b['price'], 'id': str(b['_id'])}