.. module:: CoreText
   :platform: macOS
   :synopsis: Bindings for the CoreText framework

API Notes: CoreText framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coretext/?preferredLanguage=occ

These bindings are accessed through the ``CoreText`` package (that is, ``import CoreText``).


API Notes
---------

* ``CTFontCreateWithQuickdrawInstance``

  This function is not supported by PyObjC.

* ``CTFrameGetLineOrigins``

  The ``length`` of the ``range`` argument must
  not be ``0``.

* ``CTParagraphStyleSetting``

  This structure is not yet supported.

* ``CTFontGetPlatformFont``

  This function is not supported, because the ATS framework
  does not have wrappers.

* ``CTFontCopyAvailableTables``

  This function returns a python tuple, not a ``CFArrayRef``. That's because the C version
  returns a CFArray that doesn't contain objects.

* ``CTParagraphStyleGetValueForSpecifier``

  This returns a python string containing the actual value, you'll have to
  decode this using the ``struct`` module to get at the real value.

* ``CTParagraphStyleCreate`` and ``CTParagraphStyleGetValueForSpecifier``

  Both API's have a rather low-level interface in Python: you'll have to encode the value to a python
  buffer (string), or decode it from such a buffer yourself using the ``struct`` module.

  As a convenience the sizes of value types are defined as ``sizeof_TYPE``, for example ``sizeof_CGFloat``.

  A special case is ``kCTParagraphStyleSpecifierTabStops``, it's value should be an instance of
  ``NSArray`` when using with ``CTParagraphStyleCreate``. Note that arbitrary Python sequences won't work
  here.

  Use ``CTParagraphStyleGetTabStops`` to fetch the tabstops from a style object, using
  ``CTParagraphStyleGetValueSpecifieker`` is not supported with key ``kCTParagraphStyleSpecifierTabStops``.

* All types and constants defined in "SFNTLayoutTypes.h" and "SFNTTypes.h" are not yet supported

* ``CTRunDelegateGetRefCon``

  This function is only supported when the *runDelegate* argument was created in Python.

* ``CTRunDelegateCreate``

  The first argument is a tuple with the ``getAscent``, ``getDescent`` and ``getWidth`` functions,
  the second argument is an arbitrary python object.
