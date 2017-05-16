import time
import random

from pyramid.view import view_config


def call_service(slowness):
    # Pretend this is a HTTP microservice call or something
    time.sleep(slowness)
    return 'so slow'


@view_config(route_name='mixed', renderer='json')
def mixed(request):
    # Do an IO bound service call
    time_to_sleep = float(request.matchdict.get('slowness', 0.2))
    service_result = call_service(time_to_sleep)

    # Now do some CPU bound work, like JSON decoding or like ...
    # mining bitcoins or the such. But make this dependent on the service
    # response (e.g. because large JSON bodies take longer)
    spin_for = time_to_sleep * (random.randint(0, 4))

    start = time.time()
    bitcoin = 0
    found = False
    while not found:
        # mine some bitcoins
        bitcoin += 1
        if bitcoin % 10000:
            if time.time() > start + spin_for:
                found = True
    return {
        'slow service took': '{0}s'.format(time_to_sleep),
        'so much': 'bitcoin mined, {0} cycles'.format(bitcoin),
        'mined for ': '{0}s'.format(spin_for),
    }
