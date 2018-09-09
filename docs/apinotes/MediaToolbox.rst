API Notes: MediaToolbox framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/mediatoolbox?language=objc

These bindings are accessed through the ``MediaToolbox`` package (that is, ``import MediaToolbox``).


API Notes
---------

The full framework is available from Python. This framework was introduced in OSX 10.7.

* ``MTAudioProcessingTapCreate``

  The "callbacks" argument must be a tuple of 7 items, corresponding to
  the fields in the C structure. The second item ("clientInfo") can be
  an arbtrary python object.

  The third and later elements must be None or a Python callable.

  .. warning::

     The callbacks should not fail, if calling one of the callbacks results
     in an exception that exception is ignored and a warning is printed to
     the "stderr" stream.  The exception will *not* be converted to an Objective-C
     exception.

  .. warning::

     The process will crash if the process callback is too slow, there's nothing
     PyObjC can do to prevent this.
