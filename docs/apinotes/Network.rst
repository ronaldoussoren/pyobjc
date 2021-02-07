API Notes: Network framework
============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/network/?preferredLanguage=occ

These bindings are accessed through the ``Network`` package (that is, ``import Network``).


API Notes
---------

.. note::

   This framework is only available on macOS 10.14 and later.

``nw_framer_parse_input``
.........................

The buffer must by ``objc.NULL``.

``nw_framer_parse_output``
..........................

The buffer must by ``objc.NULL``.
