import time

from pyramid.view import view_config


def call_service(slowness, call):
    # Pretend this is a HTTP microservice call or something
    time.sleep(slowness)
    return call


@view_config(route_name='io', renderer='json')
def io_bound(request):
    # Each downstream request takes N seconds
    time_to_sleep = float(request.matchdict.get('slowness', 1))
    # Have to do N slow downstream requests
    num_requests = int(request.GET.get('num_requests', 3))

    result = []
    for call in range(num_requests):
        result.append(call_service(time_to_sleep, call))

    return {
        'slow service took': '{0}s'.format(time_to_sleep),
        'did': '{0} requests'.format(num_requests),
        'got responses from requests': result
    }
