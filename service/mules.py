import time

import uwsgidecorators


@uwsgidecorators.mulefunc
def mine_bitcoin(spin_for):
    start = time.time()
    bitcoin = 0
    found = False

    while not found:
        # mine some bitcoins
        bitcoin += 1
        if bitcoin % 10000:
            if time.time() > start + spin_for:
                found = True

    print({
        'so much': 'bitcoin mined, {0} cycles'.format(bitcoin),
        'mined for ': '{0}s'.format(spin_for),
    })
