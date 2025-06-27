.. module:: Foundation
   :platform: macOS
   :synopsis: Bindings for the Foundation framework

API Notes: Foundation framework
===============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/foundation/?preferredLanguage=occ

These bindings are accessed through the ``AppKit`` package (that is, ``import AppKit``).


API Notes
---------

API additions
.............

See :doc:`/api/module-PyObjCTools.FndCategories` for some API extensions
for the Foundation framework.

NSAppleEventDescriptor, NSAppleEventManager
...........................................

These classes are barely supported, interaction with the lowlevel AppleEvent
machinery is not tested at all and probably doesn't work.

Use the ScriptingBridge and/or the (deprecated) `appscript library`_ instead
of this class.

.. _`appscript library`: https://appscript.sourceforge.io/


NSCoder
.......

* ``-encodeValuesOfObjCTypes:``: Use the basic encoding methods instead

* ``-decodeValuesOfObjCTypes:``: Use the basic decoding methods instead


NSData, NSMutableData
......................

* ``-getBytes:``: Use ``-bytes`` instead.

* ``+dataWithBytesNoCopy:length:``, ``-initWithBytesNoCopy:length``: Don't use these, Cocoa
   will try to use the C function ``free()`` on the buffer when the data object is released and
   that won't work.

* ``+dataWithBytesNoCopy:length:freeWhenDone:``, ``-initWithBytesNoCopy:length:freeWhenDone:``:
  Using these is fairly dangerous, your program can crash when the data buffer is cleaned up by
  the Python garbage collector before the ``NSData`` object is deallocated.

  The ``freeWhenDone`` argument must be ``False``.

  Use ``buffer(value)`` instead, those will automatically be bridged to an instance of a
  ``NSData`` subclass.


``NSDictionary``
................

* ``-getObjects:andKeys:``

   This method is not supported.


NSDebug
.......

* ``NSDebugEnabled``, ``NSZombieEnabled``, ``NSDeallocateZombies``,
  ``NSHangOnUncaughtException``, ``NSKeepAllocationStatistics``: These values are not available
  from Python.

* ``NSIsFreedObject``, ``NSFrameAddress``, ``NSReturnAddress``, ``NSCountFrames``:
   These functions are not available from Python.


NSException
...........

* ``NSSetUncaughtExceptionHandler`` is not supported

* ``NSAssert5``, ``NSAssert4``, ``NSAssert3``, ``NSAssert2``, ``NSAssert1``, ``NSAssert``,
  ``NSParameterAssert``, ``NSCAssert5``, ``NSCAssert4``, ``NSCAssert3``, ``NSCAssert2``,
  ``NSCAssert1``, ``NSCAssert`` and ``NSCParameterAssert`` are not supported.


NSGarbageCollector
..................

PyObjC does not fully support running with the garbage collector enabled at the moment.

* ``disableCollectorForPointer:``, ``enableCollectorForPointer:``: These API's are not
  supported at all.


NSGeometry
...........

* ``NSZeroPoint``, ``NSZeroSize``, ``NSZeroRect``: these are mutable. Do not use them
  to initialize a variable that you'll modify later on, use the default constructor instead.

  This is, instead of::

     point = NSZeroPoint
     # ...
     point.x = 4

  Use::

     point = NPoint()
     # ...
     point.x = 4

  (or even: ``point = NSPoint(x=4)``).

* The CoreGraphics types ``CGPoint``, ``CGSize`` and ``CGRect`` are interchangeable with
  their Foundation counterparts, there is no need to explicitly convert between them.


NSInvocation
............

* Struct ``NSObjCValue`` and related constants (such as ``NSObjCNoType``) are not available in
  Python.

* It is possible to get and set argument values and the return value of an invocation, but only
  for the simple cases, that is when the value is a single value and not a pointer to value or
  an array of values.

  That is, the following methods cannot be accessed through an ``NSInvocation`` at the moment:

  * `NSArray.arrayWithObjects_count_`: The first argument is a C-array of values

  * `NSFormatter.getObjectValue_forString_range_error_`: The first and last arguments are a by-reference arguments.

  It is possible to get/set values whose type is a basic C type, that is the return value ``NSArray.count`` can
  be extracted from an ``NSInvocation`` object.

  This limitation should be fine for most usecases of ``NSInvocation``, please let us know if you
  run into cases where this limitation is a problem.


NSMapTable
..........

* Using ``NSMapTableObjectPointerPersonality`` is not supported. Trying to access values in
  a maptable with this personality for the keys or values will crash your program.


Generic Macros
..............

* The function/macros ``MIN``, ``MAX`` and ``ABS`` are not available in Python. Use the
  regular python functions ``min``, ``max`` and ``abs`` instead.


NSPointerArray
..............

This class is only usable when the array is configured for Object use.


NSPointerFunctions
...................

Accessing the actual function properties (such as ``hashFunction``) is not supported.


NSMachPort delegate
...................

Implementing or calling ``handleMachMessage:`` is not supported. The argument is mapped on
a plain python integer, accessing the actual Mach message buffer is not possible.


``NSUUID``
..........

The method ``initWithUUIDBytes:`` has an argument of type bytes with length 16.

The method ``getUUIDBytes:`` returns an instance of bytes of length 16.


``NSString``
............

- ``initWithCharactersNoCopy:length:deallocator:``, ``initWithBytesNoCopy:length:encoding:deallocator:``:
  These methods are available from Python, but are not really useful because the pointer argument for
  the deallocator will not be the same as the argument passed in the first argument of this selector.

``NSAttributedString``
......................

- ``initWithFormat:options:locale:arguments:`` cannot be  used from Python.


``NSDecimalNumber``
...................

Subclassing ``NSDecimalNumber`` is support in theory, but in practice this won't work because
the Foundation framework doesn't support this.
