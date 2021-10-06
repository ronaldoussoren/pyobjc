API Notes: CoreAudio framework
=================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreaudio/?language=objc

These bindings are accessed through the ``CoreAudio`` package (that is, ``import CoreAudio``).


API Notes
---------

.. warning::

   CoreAudio is a fairly low-level framework and has no Python examples,
   due to the style of the API I'm not yet convinced that the API actually
   works correctly from Python.


* A number of structures have a custom wrapper and therefore aren't passed to functions
  as usual.

  - AudioBuffer
  - AudioBufferList
  - AudioChannelDescription
  - AudioChannelLayout
  - AudioValueTranslation

  In all cases you should explicitly pass an instance of these structure to functions,
  even for pass-by-reference output parameters. This is needed due to the low-level
  structure of these types.

* The APIs to implement CoreAudio plugins are not supported.

* ``CalculateLPCMFlags``: all arguments to this function must be provided, there is no default value for the
  last argument.


* ``FillOutASBDForLPCM``: all arguments to this function must be provided, there is no default value for the
  last argument.
