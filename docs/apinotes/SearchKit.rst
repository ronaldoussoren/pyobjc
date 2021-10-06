API Notes: SearchKit framework
==============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices/search_kit?preferredLanguage=occ

These bindings are accessed through the ``CoreServices`` package (that is, ``import CoreServices``).


API Notes
---------


SKIndexClose
............

Do not call this function, the garbage collector will automatically close the index
when it is no longer needed.
