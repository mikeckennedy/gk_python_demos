import pyramid.httpexceptions
from pyramid.renderers import get_renderer
import logbook


class BaseController:
    def __init__(self, request):
        self.request = request
        self.setup_layouts()
        self.setup_logging()

    def setup_logging(self):
        name = 'ctrls-' + type(self).__name__.replace("Controller", "").lower()
        self.logbook = logbook.Logger(name)

    def setup_layouts(self):
        layoutRenderer = get_renderer("theblog:templates/shared/_layout.pt")
        self.layout = layoutRenderer.implementation().macros['layout']

    def redirect(self, url, permanent=False):
        if not permanent:
            raise pyramid.httpexceptions.HTTPFound(url)
        else:
            raise pyramid.httpexceptions.HTTPMovedPermanently(url)
