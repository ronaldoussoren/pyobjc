.. module:: OpenDirectory
   :platform: macOS
   :synopsis: Bindings for the OpenDirectory framework

API Notes: OpenDirectory frameworks
===================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/opendirectory/?preferredLanguage=occ

These bindings are accessed through the ``OpenDirectory`` package (that is, ``import OpenDirectory``).


API Notes
---------

ODQuerySetCallback
..................

The callback function is stored by the framework, the callable can therefore not be
a generic callable, but must be a callable that is annotated using the ``objc.callbackFor``
decorator::

   @objc.callbackFor("CFOpenDirectory.ODQuerySetCallback")
   def query_callback(query, value, context, error, info):
      pass

The ``userInfo`` argument needs to be an integer.
