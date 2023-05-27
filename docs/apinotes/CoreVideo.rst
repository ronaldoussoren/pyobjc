API Notes: CoreVideo framework
=================================

API Notes
---------

* These bindings are barely tested in real code

* A number of API's aren't implemented at the moment because they require
  manual wrappers.

* Getting and setting values for ``kCVPixelFormatFillExtendedPixelsCallback``
  is not supported.

* ``CVPixelBufferCreateWithPlanarBytes`` requires a manual binding and is
  not supported at the moment.
