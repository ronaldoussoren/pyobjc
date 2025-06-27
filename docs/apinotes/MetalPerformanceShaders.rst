.. module:: MetalPerformanceShaders
   :platform: macOS 10.13+
   :synopsis: Bindings for the MetalPerformanceShaders framework

API Notes: MetalPerformanceShaders framework
============================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/metalperformanceshaders/?language=objc

These bindings are accessed through the ``MetalPerformanceShaders`` package (that is, ``import MetalPerformanceShaders``).

.. versionadded:: macOS 10.13

API Notes
---------

```MPSPackedFloat3```
.....................

In Objetive-C this type is a union. In Python the type is presented as a struct
with 3 float fields ("x", "y", "z"), that is one of the two halves of the union.
