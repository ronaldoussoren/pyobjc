API Notes: CoreAudio framework
=================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/coreaudio/?language=objc

These bindings are accessed through the ``CoreAudio`` package (that is, ``import CoreAudio``).


API Notes
---------

.. warning::

   CoreAudio is a fairly low-level framework and has no Python examples,
   due to the style of the API I'm not yet convinced that the API actually
   works correctly from Python.

* The APIs to implement CoreAudio plugins are not supported.

