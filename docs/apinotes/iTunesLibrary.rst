API Notes: iTunesLibrary framework
==================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/ituneslibrary/?preferredLanguage=occ

These bindings are accessed through the ``iTunesLibrary`` package (that is,
``import iTunesLibrary``).


.. note::

   Apple's documentation mentions that these APIs will not return usable data
   unless the application has been code signed.


API Notes
---------

* ``ITLibMediaItemPropertyFileType``

  This constant is declared on header files, but isn't actually present on
  systems (as of macOS 10.12).
