API Notes: DiscRecording framework
===================================

Apple documentation
-------------------

The full API is described in Apple's documentation, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

These bindings are accessed through the ``DiscRecording`` package (that is, ``import DiscRecording``).


API Notes
---------

This framework exposes both a C API and an Objective-C API. The Objetive-C API
is easier to use and should work without problems in Python. The C API is
harder to use and requires some manual wrappers to use nicely from Python, those
manual wrappers aren't present at the moment.

``DRFileProductionInfo``, ``DRTrackProductionInfo``
---------------------------------------------------

These types are not fully useful at the moment. The types require
a manual wrapper that is not yet written.


``DRSetRefCon``
---------------

The 'refCon' must be an integer. The 'callbacks' argument must be None.

Use :func:`context.register` if you want to store an arbitrary python
object.

.. note::

   Changing the API to allow arbitrary python objects here is not
   possible as the function ``DRGetRefCon`` doesn't return the callback
   info, and hence PyObjC cannot know how to bridge the result of that
   function back to python unless we treat is as an arbitrary 'handle'.
