API Notes: HIServers subframework of the ApplicationServices framework
======================================================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/applicationservices/?preferredLanguage=occ


API Notes
---------

This framework is mostly supported. Definitions can be accessed through both the *HIServices* and the
*ApplicationServices* modules (both part of ``pyobjc-framework-ApplicationServices``

*  ``AXValueGetValue`` is not yet supported, it requires a manual wrapper.

*  The Internet Config API's are not supported, they are deprecated and macOS 10.7 and are replaced by
   LaunchServices.

*  The Process Manager Interfaces are not supported.

*  The Icon Utilities and Icon Services Interfaces are not supported.
