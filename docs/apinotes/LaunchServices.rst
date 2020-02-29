API Notes: LaunchServices subframework of the CoreServices framework
====================================================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices/launch_services?language=objc

These bindings are accessed through the ``CoreServices`` package (that is, ``import CoreServices``).


.. note::

   The LaunchServices bindings are fairly new and are not yet fully complete,
   there are likely problems with these bindings that are not described in this
   file.

API Notes
---------

* ``LSSharedFileListSetAuthorization``

  Not supported at the moment because the Authorization framweork isn't properly
  wrapped yet.

* ``LSLaunchFSRefSpec``, ``LSLaunchURLSpec``

  These types aren't supported in this version.

* ``LSOpenApplication``

  This function is not yet supported. The bridge itself isn't smart
  enough yet to process the first argument without a manual wrapper.

* ``LSOpenItemsWithRole``, ``LSOpenURLsWithRole``

  The ``inAEParam`` and ``inAppParams`` must be None.

* ``LSOpenFromRefSpec``, ``LSOpenFromURLSpec``

  This functions are not yet supported and need manual wrappers.
