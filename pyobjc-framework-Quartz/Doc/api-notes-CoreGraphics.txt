API Notes: CoreGraphics framework
=================================

API Notes
---------

* See :doc:`/api/coregraphics-context-managers` for some extensions
  to the CoreGraphics API.

* ``CGColorConversionInfoCreateFromList``: This function requires a manual
  wrapper and is not yet supported.

* ``CGColorConverterCreate``: This function requires a manual
  wrapper and is not yet supported.

* ``CGColorSpaceCreateWithPlatformColorSpace``,
  ``CGColorSpaceCreateWithPlatformColorSpace``.

  These functions are not supported.

* The functions and data-types for parsing PDF documents (such
  as ``CGPDFStreamCreateWithStream``) are for the most part unsupported
  at the moment. We have bindings for a subsection of the APIs, but haven't
  those aren't complete nor fully tested.

*  ``CGWaitForScreenUpdateRects``, ``CGWaitForScreenRefreshRects``

   This functions are not yet supported.


* ``CGDataProviderCreate``, ``CGDataProviderCreateDirectAccess``

  These functions are not available when you build PyObjC on OSX 10.8,
  even when you run on earlier releases of OSX.

* ``CGPathCreateWithRoundedRect``, ``CGPathAddRoundedRect``

  These functions will crash hard when the parameters are inconsistent,
  for example when the rounded corners don't fit in the rectangle.

* ``CGColorConversionInfoCreateFromList``

  This function is not yet supported.

* ``CGColorConversionInfoCreateFromListWithArguments``

  This function is not supported. Use
  ``CGColorConversionInfoCreateFromList`` instead.
