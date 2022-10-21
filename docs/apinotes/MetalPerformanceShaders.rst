API Notes: MetalPerformanceShaders framework
============================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/metalperformanceshaders/?language=objc

These bindings are accessed through the ``MetalPerformanceShaders`` package (that is, ``import MetalPerformanceShaders``).


API Notes
---------

.. note::

   This framework is only available on macOS 10.13 and later.

Most of the API is available from Python, except for APIs using vector types.


```MPSPackedFloat3```
.....................

In Objetive-C this type is a union. In Python the type is presented as a struct
with 3 float fields ("x", "y", "z"), that is one of the two halves of the union.
