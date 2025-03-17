.. module:: ScreenSaver
   :platform: macOS
   :synopsis: Bindings for the ScreenSaver framework

API Notes: ScreenSaver framework
================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/screensaver/?preferredLanguage=occ

These bindings are accessed through the ``ScreenSaver`` package (that is, ``import ScreenSaver``).


API Notes
---------

Screen savers are plugins for the screen saver engine, this means
that a screen saver must contain compiled C code for the correct
architectures. Using py2app's bundle mode can be used to bundle
a screensaver bundle, but do take care to use the same version of
Python for all such bundles.
