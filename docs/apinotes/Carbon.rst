API Notes: Carbon framework
===========================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/carbon/?preferredLanguage=occ

These bindings are accessed through the ``Carbon`` package (that is, ``import Carbon``).


API Notes
---------

.. note::

   Only a limited subset of the framework has been exposed to Python. Please file and
   issue if you have a use case for using an unexposed API.



The following API groups are *not* available:

* HIToolbox: Use :module:`AppKit` instead

  * :func:`RegisterEventHotKey`: Is available.

  * :func:`UnregisterEventHotKey`: Is available.

  * :func:`CopySymbolicHotKeys`: Is available.

  * :func:`PushSymbolicHotKeyMode`: Is available.

  * :func:`PopSymbolicHotKeyMode`: Is available.

  * :func:`GetSymbolicHotKeyMode`: Is available.

* OpenScripting: Use :mod:`ScriptingBridge` instead.

* SecurityHI: Use :mod:`SecurityInterface` instead.

* SpeechRecognition: Use :class:`NSSpeechRecognizer <AppKit.NSSpeechRecognizer>` instead.
