.. module:: AVFoundation
   :platform: macOS
   :synopsis: Bindings for the AVFoundation framework

API Notes: AVFoundation framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/avfoundation?language=objc

These bindings are accessed through the ``AVFoundation`` package (that is, ``import AVFoundation``).

API Notes
---------



``[AVAudioBuffer -floatChannelData]``
.....................................

This method requires manual wrappers and is not yet available from Python.


``[AVAudioBuffer -int16ChannelData]``
.....................................

This method requires manual wrappers and is not yet available from Python.


``[AVAudioBuffer -int32ChannelData]``
.....................................

This method requires manual wrappers and is not yet available from Python.

``[AVAudioFormat -streamDescription]``
......................................

The result is a tuple of size 1, the element is the actual description.
