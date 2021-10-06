(Historical) Objective-C Garbage Collection
===========================================

On macOS versions 10.5 up to 10.12 Objective-C supported optional Garbage Collection (GC) instead of
retain counts for code that is explicitly compiled to support (or require) garbage collection.

PyObjC does *not* support the GC system, which means you cannot use PyObjC in host programs that
use the GC feature. This primarily means you cannot use PyObjC to write Screen Savers for macOS 10.6 or 10.7
because those systems used GC in the screensaver engine.
