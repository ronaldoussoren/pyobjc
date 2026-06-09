.. module:: Network
   :platform: macOS 10.14+
   :synopsis: Bindings for the Network framework

API Notes: Network framework
============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/network/?preferredLanguage=occ

These bindings are accessed through the ``Network`` package (that is, ``import Network``).

.. macosadded:: 10.14

.. warning::

   Network builds on Libdispatch and because of that invokes callbacks in
   a context where it is not possible to raise Objective-C exceptions.
   This means that Python code that raises
   exceptions in callbacks (both blocks and functions) will cause a hard
   crash.  Make sure that callbacks don't raise exceptions.

API Notes
---------

``nw_framer_parse_input``
.........................

The buffer must by ``objc.NULL``.

``nw_framer_parse_output``
..........................

The buffer must by ``objc.NULL``.
