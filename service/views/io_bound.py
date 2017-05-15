import asyncio
import time

from pyramid.view import view_config


@asyncio.coroutine
def call_service(slowness, call):
    # Pretend this is a HTTP microservice call or something
    yield from asyncio.sleep(slowness)
    return call


@view_config(route_name='io', renderer='json')
def io_bound(request):
    # Each downstream request takes N seconds
    time_to_sleep = float(request.matchdict.get('slowness', 1))
    # Have to do N slow downstream requests
    num_requests = int(request.GET.get('num_requests', 3))

    loop = asyncio.get_event_loop()
    tasks = []
    for call in range(num_requests):
        tasks.append(loop.create_task(call_service(time_to_sleep, call)))

    loop.run_until_complete(asyncio.gather(*tasks))

    result = [t.result() for t in tasks]

    return {
        'slow service took': '{0}s'.format(time_to_sleep),
        'did': '{0} requests'.format(num_requests),
        'got responses from requests': result
    }
