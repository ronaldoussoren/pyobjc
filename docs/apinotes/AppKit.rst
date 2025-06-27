.. module:: AppKit
   :platform: macOS
   :synopsis: Bindings for the AppKit framework

API Notes: AppKit framework
===========================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/appkit?preferredLanguage=occ

These bindings are accessed through the ``AppKit`` package (that is, ``import AppKit``).


API Notes
---------

API Extensions
...............

See :doc:`/api/module-PyObjCTools.AppCategories` for same extensions for
the APIs from the AppKit framework.

``NSBezierPath``
................

* ``-drawPackedGlyphs:atPoint:`` and ``-appendBezierPathWithPackedGlyphs:``

  These methods are barely supported...


``NSColorSpace``
................

* ``-initWithColorSyncProfile:`` and ``colorSyncProfile``

  These methods are not supported.

``NSEvent``
...........

* ``-initWithEventRef:`` and ``-eventRef``

  These methods are not supported

``NSGradient``
..............

* ``-initWithColorsAndLocations:``

  This method is not supported, use ``-initWithColors:atLocations:colorSpace:`` instead.


``NSDrawBitmap``
................

This function is deprecated and is not supported by PyObjC. Use an ``NSBitmapImageRep`` instead.

``NSImage``
...........

* ``initWithIconRef:``

  This method is not yet supported.

``NSMovie``
...........

NOTE: This class is deprecated by Apple, use ``QTMovie`` instead.

* ``-QTMovie``, ``-initWithMovie:``

  These methods are not supported.

``NSMovieView``
...............

* ``-movieController``

  This method is not supported.

``NSPrintInfo``
................

* ``-PMPrintSession``, ``-PMPageFormat``, ``-PMPrintSettings``

  These methods are not supported.

``NSQuickDrawView``
...................

* ``-qdPort``

  This method is not supported.

``NSGlyphInfoAtIndex``
......................

This function is not supported.

``NSTypesetterGlyphInfo``
.........................

This structure is not supported, and therefore the method ``-baseOfTypesetterGlyphInfo`` and
``-typesetterLaidOneGlyph`` of ``NSSimpleHorizontalTypesetter`` are not supported as well.

``NSWindow``
............

Methods ``-initWithWindowRef:`` and ``-windowRef`` are not supported.

``NSInputStream``
.................

* ``getBuffer:length:``

   This method is not supported

``NSBitmapImageRep``
....................

* ``-initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:``

  This method is not yet supported. Support for this method requires a manual wrapper, which
  has not been written yet.

``NSDictionaryOfVariableBindings``
...................................

This is a helper macro that cannot be implemented with the same interface in Python.

Instead of::

    NSDictionaryOfVariableBindings(button1, button2, nil)

use::

    { "button1": button1, "button2": button2 }

or::

    AppKit.NSDictionaryOfVariableBindings("button1", "button2")

The first alternative is preferable because it is cleaner Python code, and
the implementation of ``NSDictionaryOfVariableBindings`` has to use an
unstable API of CPython.

``IBInspectable`` and ``IB_DESIGNABLE``
.......................................

These definitions are not supported.
