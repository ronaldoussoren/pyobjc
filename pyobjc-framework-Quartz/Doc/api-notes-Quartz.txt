API Notes: Quartz frameworks
============================

Quartz vs. CoreGraphics
-----------------------

The PyObjC bindings for the Quartz related frameworks, including CoreGraphics
and QuartzComposer are in the Python package "Quartz". When you use the
system version of Python there's also a package named "CoreGraphics".  This
is Apple's closed-source binding of CoreGraphics, which is not a direct
mapping of the Quartz API's but includes some convenience APIs that are not 
present in the C API. 

The PyObjC bindings for Quartz are not compatible with the CoreGraphics 
Python package by Apple.

Importing
---------

The prefered way to import from packages in these bindings is::

   import Quartz

It is also possible to import directly from subwrappers (such
as ``Quartz.CoreGraphics``), but it better to import from the toplevel
to ensure you'll get all relevant definitions.

API Notes
---------

API Extensions
..............

See :doc:`/api/coregraphics-context-managers` for some extensions to the API
in the CoreGraphics framework.

Callbacks
.........

The ``userinfo`` for ``CGDataConsumerCreate``, ``CGDataProviderCreate``,
``CGDataProviderCreateDirect``, ``CGDataProviderCreateDirectAccess``,
``CGDataProviderCreateSequential``, ``CGDataProviderCreateWithData``,
``CGDisplayRegisterReconfigurationCallback``, 
``CGDisplayRemoveReconfigurationCallback``, 
``CGFunctionCreate``, ``CGRegisterScreenRefreshCallback``, 
``CGReleaseScreenRefreshRects``, ``CGScreenRegisterMoveCallback``,
``CGScreenUnregisterMoveCallback``, ``CGUnregisterScreenRefreshCallback``,
``CGPDFDictionaryApplyFunction``, ``CGPathApply``, ``CGPatternCreate``,
``CGEventTapCreate``, ``CGEventTapCreateForPSN``, ``CGPDFOperatorTableSetCallback`` and ``CGPSConverterCreate``  can be any Python object.

The function arguments for these functions can be any Python callable, 
including bound methods. Functions mentioned earlier that have a struct with
callback functions take in tuple with those callbacks in Python.

``CGEventTapCreate`` and ``CGEventTapCreateForPSN`` leak some memory when they
are called. This is needed to avoid memory management problems. It is therefore
advisable not to call these functions, are at least call them a small number
of times.

``CGPatternCreate``: the callback argument is a single function: the ``drawPattern`` callback.

``CGDataProviderCreateWithData``: the release callback can be ``None``. If it is not ``None`` it 
must be a function with 1 argument: the ``info`` object.

``CGPDFOperatorTableSetCallback`` is not supported at the moment.



``CGColorSpaceCreateWithPlatformColorSpace``
............................................

This function is not supported because the lowlevel "CMProfileRef" type is
not wrappped by PyObjC.


``kCGDirectMainDisplay``
........................

This value isn't actually a constant and can therefore not be wrapped by
PyObjC. Use ``CGMainDisplayID()`` instead.


``CGWindowListCreate``, ``CGWindowListCreateDescriptionFromArray``, ``CGWindowListCreateImageFromArray``
.........................................................................................................

This function is documented to return a "CFArray of CGWindowID". This specific type cannot be represented by
PyObjC, therefore the (manually wrapped) function returns a tuple of CGWindowID values instead.

For the same reason ``CGWindowListCreateDescriptionFromArray``, ``CGWindowListCreateImageFromArray`` are
manually wrapped and take a tuple of WindowID values as an argument.


``CGBitmapCreate``
..................

The easiest way to use this function is to pass ``None`` as the buffer argument, that way Quartz will create the
buffer for you. If you do want direct access to the buffer you'll have to create a writable buffer, for example
like so::

    bytes = array.array('B', (0 for i in xrange(100*80*4)))
    ctx = CGBitmapContextCreate(bytes, 100, 80, 8, 400, CGColorSpaceCreateDeviceRGB(), kCGImageAlphaPremultipliedLast)

This creates a context for a 100 pixels by 80 pixels image with a RGBA colorspace.

Note that there limitations on the kinds of context's you can create, see the Apple documentation about supported
pixel formats for the details on that.


``CGColorSpaceGetColorTable``
.............................

This function has an output buffer of indetermined size. You cannot pass ``None`` as the value of that buffer but have
to explicitly specify a writable output buffer (such an ``array.array`` or the right type and size).


Low-level PDF support
......................

Low-level PDF support in the CoreGraphics framework (such as the ``PDFArrayRef``
type) are barely supported by PyObjC and these API's are currently not covered 
by PyObjC's testsuite.

Adding support for these API's is on the todo-list, but adding proper support
requires work because the ``PDFArrayRef`` type (and simular types) is not
a CoreFoundation based type.


``CGPSConverter``
.................

The API's related to CGPSConverter are not supported at the moment.


``CIContext``
.............

* ``-render:toBitmap:rowBytes:bounds:format:colorSpace``

  You must pass a writable buffer of the right size to this method (such as 
  a properly sized instance of ``array.array``.


``CVPixelBufferCreate``
.......................

This function requires a manual wrapper and is not supported yet.


``CVPixelBufferCreateWithBytes``
................................

This function requires a manual wrapper and is not supported yet.


``CVPixelBufferCreateWithPlanarBytes``
......................................

This function requires a manual wrapper and is not supported yet.


``CVFillExtendedPixelsCallBack``
................................

Pixel format attributes of this type are not supported.

