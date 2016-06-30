import pyramid_handlers
from theblog.data.db import DB

from theblog.controllers.base_controller import BaseController


class HomeController(BaseController):
    # /
    # /home
    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'project': 'from handler', 'more': "Yes"}

    # /home/about
    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'project': 'about', 'more': "No"}

    # /home/contact
    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'project': 'contact', 'more': "No"}

    # /home/books
    @pyramid_handlers.action(renderer='templates/home/books.pt')
    def books(self):
        books = DB.get_books()
        self.logbook.info("Processing request for {} books".format(books))
        return {'books': books}
