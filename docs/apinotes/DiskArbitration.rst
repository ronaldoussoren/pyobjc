API Notes: DiskArbitration framework
====================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/diskarbitration/?preferredLanguage=occ

These bindings are accessed through the ``DiskArbitration`` package (that is, ``import DiskArbitration``).



API Notes
---------

The entire framework is available from Python.


DADiskCreateFromIOMedia
.......................

This function cannot be called from Python because IOKit is not yet
wrapped.

DADiskCopyIOMedia
.................

This function cannot be called from Python because IOKit is not yet
wrapped.


``DAUnregisterCallback`` and ``DAUnregisterApprovalCallback``
.............................................................

The *callback* argument should be the result of calling ``objc.callbackPointer``
on the function that was used to register a callback.
