API Notes: SceneKit framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/scenekit/?preferredLanguage=occ

These bindings are accessed through the ``SceneKit`` package (that is, ``import SceneKit``).


API Notes
---------

The full API for the SceneKit framework is available from Python, except for methods that have a
vector_float3 or vector_float4 as one of their arguments or as a return value (those require changes
to PyObjC's core bridge).

This means ``SCNVector3ToFloat3`` and ``SCNVector3FromFloat3`` are not available from Python.

The type "SCNVector3FromGLKVector3" is also not available at the moment.

.. note::

   This framework is only available on macOS 10.8 and later.


* ``SCNErrorDomain``

  This variable is documented to exist on OSX 10.10, but isn't actually available there.
