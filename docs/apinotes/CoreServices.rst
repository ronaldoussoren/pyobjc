API Notes: CoreServices framework
==================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices?preferredLanguage=occ


API Notes
---------

The CoreServices framework is an umbrella framework containing a number of other frameworks:

 * *AE*

   The definitions for this framework (names starting with "AE") are not
   available in Python.

 * *CarbonCore*

  Only definitions from 'BackupCore.h' and 'DiskSpaceRecovery.h'  are available in Python.


 * *DictionaryServices*

   The definitions in the subframework are available both by importing
   ``CoreServices`` and by importing ``DictionaryServices``.

 * *FSEvents*

   The definitions in the subframework are available both by importing
   ``CoreServices`` and by importing ``FSEvents``.

 * *LaunchServices*

   The definitions in the subframework are available both by importing
   ``CoreServices`` and by importing ``LaunchServices``.

 * *Metadata*

  The definitions for this framework are not yet available in Python.

 * *OSServices*

  The definitions for this framework are not yet available in Python.

 * *SearchKit*

   The definitions in the subframework are available both by importing
   ``CoreServices`` and by importing ``SearchKit``.

 * *SharedFileList*

   The definitions in the subframework are available both by importing
   ``CoreServices`` and by importing ``LaunchServices``.
