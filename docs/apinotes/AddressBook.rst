API Notes: AddressBook framework
================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/addressbook?preferredLanguage=occ

These bindings are accessed through the ``AddressBook`` package (that is, ``import AddressBook``).


API Notes
---------

Plugin API
..........

The C API for creating plugin bundles is not supported. Use the Objective-C API instead.

ABPeoplePicker C API
....................

``ABPickerSetDelegate`` and ``ABPickerGetDelegate`` use an API that isn't
wrapped by PyObjC.

The C API has some problems on Snow Leopard, use the Object-Oriented API instead.

ABActionCallbacks C API
.......................

The ``ABActionCallbacks`` plugin interface for C based CFBundles is not supported
