Objective-C Garbage Collection
==============================

Starting from Mac OS X 10.5 Objective-C supports an optional Garbage Collection (GC) for code that is
explictly compiled to support (or require) garbage collection. The GC system is deprecated in OS X 10.8.

PyObjC does *not* support the GC system, the core bridge is currently not GC save and using PyObjC in
a proces that uses GC is not supported (and the default compilation flags for PyObjC also don't mention
that the code supports GC).

Because GC is not supported you cannot write Screen Savers with PyObjC on Mac OS X 10.6 or 10.7 systems when
the system is running with a 64-bit user-space.
