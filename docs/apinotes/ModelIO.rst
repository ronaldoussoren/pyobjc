API Notes: ModelIO framework
============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/modelio/?preferredLanguage=occ

These bindings are accessed through the ``ModelIO`` package (that is, ``import ModelIO``).


API Notes
---------

The full API for the ModelIO framework is available from Python, except
for methods that have a SIMD types as one of their arguments or as a return
value (those require changes to PyObjC's core bridge).  Because of this these
bindings are not very usefull at this time.
