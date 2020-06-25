API Notes: ApplicationServices framework
========================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/applicationservices?preferredLanguage=occ


API Notes
---------

The ApplicationServices framework is an unbrella framework containing a number of other frameworks:

 * *ATS*

   The definitions for this framework (names starting with "ATS") are not available in Python, all of
   them appear to be deprecated.

 * *ColorSync*

  The definitions for this framework (names starting with "CM") are not yet available in Python.

 * *CoreGraphics*

   This framework is primarily wrapped through the *Quartz* module in ``pyobjc-framework-Quartz``, but
   all definitions are also available through the *ApplicationServices* module.

 * *CoreText*

   This framework is primarily wrapped through the *CoreText* module in ``pyobjc-framework-CoreText``, but
   all definitions are also available through the *ApplicationServices* module.

 * *HIServices*

   This framework is fully supported. Definitions can be accessed through both the *HIServices* and the
   *ApplicationServices* modules (both part of ``pyobjc-framework-ApplicationServices``

   ``AXValueGetValue`` is not yet supported, it requires a manual wrapper.

   The Internet Config API's are not supported, they are deprecated and OSX 10.7 and are replaced by
   LaunchServices.

   The Process Manager Interfaces are not supported.

   The Icon Utilities and Icon Services Interfaces are not supported.

 * *ImageIO*

   This framework is primarily wrapped through the *Quartz* module in ``pyobjc-framework-Quartz``, but
   all definitions are also available through the *ApplicationServices* module.

 * *LangAnalysis*

   This framework is deprecated and its definitions (names starting with "LA") are not available in Python.

 * *PrintCore*

   The definitions for non-deprecated functions are available. The "PMObject" class in this framework
   is not a CoreFoundation or Objective-C class, and this means that users of the API are responsible
   for calling ``PMRetain`` and ``PMRelease`` where appropriate.

   The definitions related to Apple Evens (such as kPMPrintSettingsAEType) are not supported.

   ``PMPrintSettingsToOptions`` and ``PMPrintSettingsToOptionsWithPrinterAndPageFormat`` require
   manual bindings and is not yet supported.

 * *QD*

   This framework is deprecated an definitions in this framework are not available in Python.

 * *SpeechSynthesis*

   Definitions in the framework are not yet available in Python.


.. note::

   This framework is only available on macOS 10.9 and later.
