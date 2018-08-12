API Notes: CoreAudio framework
=================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/coreaudio/?language=objc

These bindings are accessed through the ``CoreAudio`` package (that is, ``import CoreAudio``).


API Notes
---------

.. warning::

   CoreAudio is a fairly low-level framework and has no Python examples,
   due to the style of the API I'm not yet convinced that the API actually
   works correctly from Python.


* The AudioBuffer has a custom wrapper, and therefore has an API that is slightly different from
  automaticly wrapped structs.

  - Instances have the same attributes as the C struct
  - There is a method "create_buffer(size)" to create the buffer for audio samples
  - Create a new buffer with "AudioBuffer(\*, num_channels=1, buffer_size=None)"
  - The underlying storage of buffers returned by Apple APIs is not controlled by PyObjC. Read
    Apple's API documention to dermine when it is safe to access buffers.

* The AudioBufferList has a custom wrapper, and therefore has an API that is slightly different from
  automaticly wrapped structs.

  - The type behaves like a basic sequence of AudioBuffer instances, use len(audio_buffer_list) to get
    the number of buffers in teh AudioBufferList, use audio_buffer_list[n] to access an item.
  - "AudioBufferList(n)" creates a bufferlist of "n" items.
  - As with AudioBuffers the lifetime of the underlying storage of buffer lists returned by
    Apple APIs is not controlled by PyObjC, read the API documentation to determine when it is
    safe to use a buffer list.

* The APIs to implement CoreAudio plugins are not supported.

* ``CalculateLPCMFlags``: all arguments to this function must be provided, there is no default value for the
  last argument.


* ``FillOutASBDForLPCM``: all arguments to this function must be provided, there is no default value for the
  last argument.


