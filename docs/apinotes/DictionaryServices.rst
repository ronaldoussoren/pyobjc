API Notes: DictionaryServices framework
=======================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices/?preferredLanguage=occ

These bindings are accessed through the ``CoreServices`` package (that is, ``import CoreServices``).


API Notes
---------

PyObjC provides complete wrappers for the DictionaryServices framework.

.. warning::

   On macOS 10.12 the interpreter crashes when using this framework
   using a python.org binary, it works fine using a locally build
   interpreter (such as Homebrew)
