import time
import random

from pyramid.view import view_config
from service.mules import mine_bitcoin


@view_config(route_name='cpu_offload', renderer='json')
def index(request):
    # Find me some bitcoins
    spin_for = random.randint(1, int(request.GET.get('spin_for', 1)))
    mine_bitcoin(spin_for)
    return {
        'offloaded work!': True
    }
