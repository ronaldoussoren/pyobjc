Objective-C Garbage Collection
==============================

Starting from Mac OS X 10.5 Objective-C supports an optional Garbage Collection (GC) for code that is 
explictly compiled to support (or require) garbage collection. The GC system is deprecated in OS X 10.8.

PyObjC does *not* support the GC system, the core bridge is currently not GC save and using PyObjC in
a proces that uses GC is not supported (and the default compilation flags for PyObjC also don't mention
that the code supports GC).


Because GC is not supported you cannot write Screen Savers with PyObjC on Mac OS X 10.6 or 10.7 systems when
the system is running with a 64-bit user-space.

Technical issues w.r.t. GC support
----------------------------------

The following is an incomplete list of issues that make it impossible to use PyObjC with GC.  

* The ``OC_*`` classes (Objective-C proxies for Python objects) have a ``-dealloc`` method, but 
  no ``-finalize`` method. This will cause memory leaks when using GC because the Python reference count
  is never decreased.

* Python subclasses of Cocoa classes have a (generated) ``-dealloc`` method that cleans up the python
  state of the object. They don't have a ``finalize`` method, once again causing memory leaks.

* The bridge uses ``NSMapTable`` instances to store the proxy objects for Python and Objective-C objects
  (one to get the proxy object for Python objects and one to get the proxy objects for Objective-C objects).

  Those currently contain strong references for both keys and values, which means Python objects that have 
  passed the bridge cannot die because their proxy will never be garbage collected.

* The ``NSMapTable`` instances mentioned in the previous item are likely not used thread safely in GC-ed
  processes (the use is currently serialized using Python's GIL)

* *All* Objective-C code needs to be reviewed to check if it is GC-safe.

I don't expect that PyObjC will ever support GC because Apple has deprecated GC in OS X 10.8, and will likely 
remove GC support in some future release.  It is therefore not worthwhile to spend a signficant amount of time
on making PyObjC GC-safe.
