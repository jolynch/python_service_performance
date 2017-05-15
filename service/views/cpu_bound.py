import time
import random

from pyramid.view import view_config


@view_config(route_name='cpu', renderer='json')
def index(request):
    # Find me some bitcoins
    spin_for = random.randint(1, int(request.GET.get('spin_for', 1)))

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
        'so much': 'bitcoin mined, {0} cycles'.format(bitcoin),
        'mined for ': '{0}s'.format(spin_for),
    }
