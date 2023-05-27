API Notes: CFNetwork framework
==============================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/cfnetwork?preferredLanguage=occ

These bindings are accessed through the ``CFNetwork`` package (that is, ``import CFNetwork``).


API Notes
---------

* ``CFHTTPReadStreamSetRedirectsAutomatically``

  This API was removed in macOS 10.15.

* ``CFNetServiceGetProtocolSpecificInformation``

  This API was removed in macOS 10.15.

* ``CFNetServiceSetProtocolSpecificInformation``

  This API was removed in macOS 10.15.

* ``CFNetworkExecuteProxyAutoConfigurationScript`` and ``CFNetworkExecuteProxyAutoConfigurationURL``

  The ``context`` argument can be an arbitrary Python object.

* ``CFHostSetClient``

  The ``context`` argument can be an arbitrary Python object, in particular
  the creation of a ``CFHostClientContext`` is performed by the bridge and
  is not exposed to Python.

* `CFNetServicesSetClient``

  The ``context`` argument can be an arbitrary Python object, in particular
  the creation of a ``CFNetServiceClientContext`` is performed by the bridge and
  is not exposed to Python.

* ``CFNetServiceBrowserCreate``

  The ``clientContext``  argument can be an arbitrary python object

* ``CFNetServiceSetClient``

  The ``clientContext``  argument can be an arbitrary python object

* ``CFNetServiceMonitorCreate``

  The ``clientContext``  argument can be an arbitrary python object
