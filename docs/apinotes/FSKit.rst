API Notes: FSKit framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/fskit?preferredLanguage=occ

These bindings are accessed through the ``FSKit`` package (that is, ``import FSKit``).

.. note::

   This framework is available on macOS 15 and later

API Notes
---------

* ``-[FSMessageConnection logLocalizedMessage:table:bundle:arguments:]``

  This method is not available in Python, use one of the other log methods instead.
