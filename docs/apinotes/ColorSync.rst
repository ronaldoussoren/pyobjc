API Notes: ColorSync framework
===============================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/colorsync?language=objc

These bindings are accessed through the ``ColorSync`` package (that is,
``import ColorSync``).


API Notes
---------

.. note::

   This framework is only available on OSX 10.13 and later and requires a 64-bit binary.

Plugins
.......

The APIs for writing new colorsync engines is not supported from Python.
