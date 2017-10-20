API Notes: CFNetwork framework
==============================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/reference/cfnetwork

These bindings are accessed through the ``CFNetwork`` package (that is, ``import CFNetwork``).


API Notes
---------

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
