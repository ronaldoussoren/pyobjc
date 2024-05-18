.. module:: ColorSync
   :platform: macOS 10.13+
   :synopsis: Bindings for the ColorSync framework

API Notes: ColorSync framework
===============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/colorsync?language=objc

These bindings are accessed through the ``ColorSync`` package (that is,
``import ColorSync``).

.. note::

   This framework is only available on macOS 10.13 and later.

API Notes
---------


Plugins
.......

The APIs for writing new colorsync engines is not supported from Python.
