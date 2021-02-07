API Notes: ScreenSaver framework
================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/screensaver/?preferredLanguage=occ

These bindings are accessed through the ``ScreenSaver`` package (that is, ``import ScreenSaver``).


API Notes
---------

The PyObjC bindings for the ScreenSaver framework are complete.


Platform limitations
--------------------

Screen savers are plugins for the screen saver engine, this means
that a screen saver must contain compiled C code for the correct
architectures.

On macOS 10.6 and macOS 10.7 you cannot use PyObjC to write a screen saver
because the screen saver engine uses Objetive-C Garbage Collection and
that is not supported by PyObjC.

Screen savers work again in macOS X 10.8.
