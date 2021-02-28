API Notes: AE framework
=======================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices/?language=objc

These bindings are accessed through the ``CoreServices`` package (that is, ``import CoreServices``).


API Notes
---------

``typeSMInt``, ``typeShortInteger``, ``typeInteger``, ``typeLongInteger``, ``typeMagnitude``, ``typeComp``, ``typeSMFloat``, ``typeShortFloat``, ``typeFloat``, ``typeLongFloat``, ``typeExtended``, ``typeFSS``
............................. ..................................................................................................................................................................................

These constants are not available in Python. Apple has removed these for 64-bit code and I've decided to not make them available at all to Python code.
