import time
from pyramid.config import Configurator


def add_routes(config):
    """Add in routes to our views"""
    config.add_route('index', '/')


def create_application():
    """ This function returns a Pyramid WSGI application.
    """
    time.sleep(1)
    config = Configurator(settings={
        'service_name': 'service'
    })
    config.include('pyramid_jinja2')
    add_routes(config)

    config.scan('service')
    return config.make_wsgi_app()
