from pyramid.view import view_config


@view_config(route_name='index', renderer='json')
def index(request):
    return {
        'app': 'service',
        'description': 'You know, for perf testing'
    }
