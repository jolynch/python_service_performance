"""WSGI server configuration file

A callable named application MUST be defined by this file which will be run
by the WSGI server.

Anything that is specific to the WSGI server of your choice should be done
here. If you need to pass something through, pass it through
create_application.
"""
import uwsgidecorators
import webob

from service.webapp import create_application


def application(environ, start_response):
    app = create_application()
    return app(environ, start_response)


# Do the minimum request possible to force Pyramid to actually load the app
# This must be done postfork so that non fork safe things like database
# connections are not loaded in the pre fork process
@uwsgidecorators.postfork
def do_warmup():
    mock_request = webob.request.Request.blank(path='/')
    application(
        environ=mock_request.environ,
        start_response=lambda x, y: None
    )
