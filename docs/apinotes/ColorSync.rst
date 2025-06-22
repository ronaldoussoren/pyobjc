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

.. macosadded:: 10.13

API Notes
---------


Plugins
.......

The APIs for writing new colorsync engines is not supported from Python.
