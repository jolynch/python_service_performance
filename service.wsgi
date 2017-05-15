"""WSGI server configuration file

A callable named application MUST be defined by this file which will be run
by the WSGI server.

Anything that is specific to the WSGI server of your choice should be done
here. If you need to pass something through, pass it through
create_application.
"""
from service.webapp import create_application


def application(environ, start_response):
    app = create_application()
    return app(environ, start_response)
