import logbook
import sys
from pyramid.config import Configurator
import theblog.controllers.home_controller as home
import theblog.controllers.admin_controller as admin
import theblog.controllers.api_controller as api
from theblog.views import not_found_there
import pymongo


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    logbook.StreamHandler(sys.stdout).push_application()

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('home', '/')
    # config.add_notfound_view(not_found_there)

    config.add_handler('slash', '/', handler=home.HomeController, action='index')
    add_routes(home.HomeController, 'home', config)
    add_routes(admin.AdminController, 'admin', config)
    add_routes(api.ApiController, 'api', config)
    # add_routes(account.AccountController, 'account')


    config.scan()

    return config.make_wsgi_app()


def add_routes(handler, base_name, config):
    config.add_handler(base_name + '_all', '/' + base_name + '/{action}', handler=handler)
    config.add_handler(base_name + '_all_id', '/' + base_name + '/{action}/{id}', handler=handler)
