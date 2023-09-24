API Notes: ScriptingBridge framework
====================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/scriptingbridge/?preferredLanguage=occ

These bindings are accessed through the ``ScriptingBridge`` package (that is, ``import ScriptingBridge``).



Basic usage
-----------

The Objective-C documentation for the scripting bridge frameworks
focuses on static tools for creating proxy classes for scriptable
applications. This is in general not needed when you're programming
in Python.

In Python you can just as easy create a dynamic proxy object::

	iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

This can then be used to call "AppleScript" methods, like this::

	print iTunes.currentTrack().name()


API Notes
---------

``-[SBObject sendEvent:id:parameters]``
.......................................

This method is not supported at the moment. Please file an issue if you have
a use-case for directly calling this method.
