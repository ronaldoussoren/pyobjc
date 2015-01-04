API Notes: ApplicationServices framework
========================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/ApplicationServices/ApplicationServices.html


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

   Definitions in the framework are not yet available in Python.

 * *QD*

   This framework is deprecated an definitions in this framework are not available in Python.

 * *SpeechSynthesis*

   Definitions in the framework are not yet available in Python.


.. note::

   This framework is only available on OSX 10.9 and later and requires a 64-bit binary.
