API Notes: SystemConfiguration framework
========================================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/systemconfiguration/?preferredLanguage=occ

These bindings are accessed through the ``SystemConfiguration`` package (that is, ``import SystemConfiguration``).

API Notes
---------

callbacks
.........

There are several APIs that have a callback function and context structure in the
(Objective-)C API. In all cases an arbitrary object can be passed as the context,
PyObjC will wrap that in the proper context structure for you.


SCDynamicStore
...............

The ``context`` argument for ``SCDynamicStoreCreate`` is an arbitrary python object,
not a ``SCDynamicStoreContext`` structure as it is in C. The bridge will manage that
context structure for you.


SCNetworkCheckReachabilityByAddress
...................................

The ``address`` argument should have a value that can also be used with the Python socket
APIs (that is, a ``(host, port)`` tuple for IPv4 addresses or
``(host, port, flowinfo, scopeid)`` tuple for IPv6 addresses).

The ``addrlen`` argument should be ``objc._size_sockaddr_ip4`` for IPv4 addresses and
``_size_sockaddr_ip6`` for IPv6 addresses.
