service
=======
A demonstration of Python Service performance techniques

Note that I construct this demo with git commits, so I will be force pushing
and rebasing quite a bit. If you want a copy of master I'd suggest forking.

Running
=======
To give it a try in dev mode run::

    tox -e rundev
    # separate window
    curl localhost:1234

or to run the "prod" instance::

    tox -e runprod
    # separate window
    nginx -c "$(pwd)/nginx.cfg"
    # separate window
    curl localhost:1234


Performance Techniques Covered
==============================

Core techniques for scaling a Python Service
--------------------------------------------
These are simple, good architectural choices that will make your Python
services scale way farther than before.

1. Post-fork warming the application to prevent cold workers
2. Async downstream requests to protect against slow downstreams
3. Async accept to increase scalability when downstreams get slow
4. Scaling CPU bound workloads with workers and offloading to mules
5. Solving mixed IO/CPU work with proper load balancing and NGINX

Bonus material
--------------
These strategies are more hit or miss, but depending on the workload it can
help you.

1. Disabling GC during the request and enabling it post request
2. JSON -> msgpack
2. cythonize the slow CPU bits
