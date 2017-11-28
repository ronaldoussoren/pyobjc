PyObjC support for vector/SIMD types
====================================

Apple uses vector/SIMD types, like ``vector_float3``, in
a number of APIs. These types are not yet supported by
PyObjC. Support will be added in a future versions.

The technical reason for the lack of support is twofold:

1. The low-level library used to construct C function calls
   (`libffi <https://sourceware.org/libffi/>`_) does not
   support these types.

2. The Objective-C compiler does not include information about
   arguments/return values of these types in the runtime
   metadata.

The latter point is primarily annoying and can easily be
circumvented using PyObjC's metadata system. The first point
is more serious and requires significant work to be able
to support these types.
