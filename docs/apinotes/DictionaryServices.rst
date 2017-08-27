API Notes: DictionaryServices framework
=======================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/reference/dictionaryservices/

These bindings are accessed through the ``DictionaryServices`` package (that is, ``import DictionaryServices``).


API Notes
---------

PyObjC provides complete wrappers for the DictionaryServices framework.

.. warning::

   On OSX 10.12 the interpreter crashes when using this framework
   using a python.org binary, it works fine using a locally build
   interpreter (such as Homebrew)
