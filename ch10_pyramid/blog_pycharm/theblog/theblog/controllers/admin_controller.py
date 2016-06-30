from pyramid_handlers import action
import pyramid.response
from theblog.controllers.base_controller import BaseController
from theblog.data.db import DB


class AdminController(BaseController):
    @action(renderer='templates/admin/add_book.pt',
            name='add_book',
            request_method='GET')
    def add_book_get(self):
        return {}

    @action(renderer='templates/admin/add_book.pt',
            name='add_book',
            request_method='POST')
    def add_book_post(self):
        print(self.request.POST)
        title = self.request.POST.get('title')
        price = float(self.request.POST.get('price', 0.0))
        pages = int(self.request.POST.get('chapter_count', 0))

        DB.add_book(title, price, pages)
        self.redirect('/home/books')
