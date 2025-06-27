.. module:: CoreFoundation
   :platform: macOS
   :synopsis: Bindings for the CoreFoundation framework

API Notes: CoreFoundation framework
===================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/corefoundation/?preferredLanguage=occ

These bindings are accessed through the ``CoreFoundation`` package (that is, ``import CoreFoundation``).


.. warning::

   Incorrect usage of CoreFoundation API's will often cause crashes of the Python interpreter. This is
   caused by the way CoreFoundation is implemented and it is not possible work create nice Python exceptions
   when this happens. The same crashes also happen when for incorrect usage in C programs.


Containers
----------

Container datastructures, such as ``CFArray`` and ``CFTree``, are only
supported when the contain only ``CFTypeRef`` values even when the actual
C API supports arbitrary pointer values.


Toll-free bridging
------------------

Toll-free bridging applies to Python as well, and is more convenient than
in Objective-C because you don't have to cast between a CoreFoundation type
and an Objective-C class.

API Notes
---------


CFArrayRef
..........

This type is only supported when the ``callbacks`` are
``kCFTypeArrayCallBacks``, accessing other ``CFArray`` values from Python is
not supported and will crash your interpreter.

Note that all ``CFArrayRef`` instances are instances of ``NSArray`` or
``NSMutableArray`` as well.


* ``CFArrayCreate``, ``CFArrayCreateMutable``

  The ``callbacks`` argument must be ``kCFTypeArrayCallbacks``.

* The ``context`` argument for ``CFArrayApplyFunction``,
  ``CFArrayBSearchValues`` and ``CFArraySortValues``  can be an arbitrary
  object (unlike the ``context`` or ``userdata`` argument in a lot of other
  API's).


CFBagRef
........

This type is only supported when the ``callbacks`` are
``kCFTypeBagCallBacks``, accessing other ``CFBag`` values from Python is not
supported.

* ``CFBagCreate``, ``CFBagCreateMutable``

  These function don't have a ``callBacks`` argument in Python and will always
  use the ``kCFTypeBagCallBacks`` value for that argument in C.

* The ``context`` argument for ``CFBagApplyFunction`` can be an arbitrary
  Python object.


CFBinaryHeapRef
...............

The ``CFBinaryHeap`` wrappers assume that values are instances of CoreFoundation
types or Objective-C classes.

* ``CFBinaryHeapCreate``

  The ``callbacks`` argument is not present in Python and is automatically
  set to a value that allows arbitrary objects that implement the
  ``compare:`` method.

  The ``compareContext`` argument is also not present in Python.

* ``CFBinaryHeapGetMinimumIfPresent``

  This function crashes the interpreter, the reason for that is unclear.


CFBundle
........

* ``CFBundleGetFunctionPointerForName``,
  ``CFBundleGetFunctionPointersForNames``,
  ``CFBundleGetDataPointerForName`` and
  ``CFBundleGetDataPointersForNames``: these functions are not supported,
  use the native PyObjC bundle loading API's instead (the the core
  PyObjC documentation for details).

CFData
......

* ``CFDataGetBytePtr``, ``CFDataGetMutableBytePtr``: these functions return
  an ``objc.varlist`` of bytes. A varlist doesn't implement the buffer
  interface, but can be used to peek into the buffer (and poke bytes into
  the buffer when you're using ``CFDataGetMutableBytePtr``).

CFDictionary
............

* ``CFDictionaryCreate``, ``CFDictionaryCreateMutable``: the callback
  arguments are must be ``kCFTypeDictionaryKeyCallBacks`` and
  ``kCFTypeDictionaryValueCallBacks``.

  instances contain objects (both as keys and as values)

* ``CFDictionaryApplyFunction``: the ``context`` argument can be an
  arbitrary Python object.

CFFileDescriptor
................

* The ``context`` argument for ``CFFileDescriptorCreate`` is a python object,
  the ``CFFileDescriptorContext`` is automatically added by the bridge.

* The ``CFFileDescriptorGetContext`` results the python object that was
  used in ``CFFileDescriptorContext``, not a ``CFFileDescriptorContext``
  structure.

  NOTE: This means it is unsafe to call ``CFFileDescriptorGetContext`` on
  objects that weren't created in Python code.

CFMachPort
..........

.. note::

   The current bindings for the CFMachPort API are probably useless, as
   there doesn't seem to be a proper binding of the low-level API's.

* The ``context`` argument for ``CFMachPortCreate``  and
  ``CFMachPortCreateWithPort`` is a python object, the
  ``CFMachPortContext`` is automatically added by the bridge.

* The ``CFMachPortGetContext`` results the python object that was
  used in ``CFMachPortContext``, not a ``CFMachPortContext``
  structure.

  .. note::

     This means it is unsafe to call ``CFMachPortContext`` on
     objects that weren't created in Python code.

CFMessagePort
.............

* ``CFMessagePortInvalidationCallback``: The second argument of the
  callback is an integer that should be ignored. The context value
  can be retrieved using ``CFMessagePortGetContext`` (for local
  ports, remote ports don't have a context).

CFNumber
........

Note that Python numbers are automatically translated to/from Objective-C
numbers (NSNumber, which toll-free bridged to CFNumber). This means the
CFNumber functions should almost never be necessary.

That said, all CFNumber API's do actually work.

CFNumberFormatter
.................

* ``CFNumberFormatterCreateStringWithValue``: this function is not
  supported at the moment, use ``CFNumberFormatterCreateStringWithNumber``
  instead.

* ``CFNumberFormatterGetValueFromString``: this function is not
  supported at the moment, use ``CFNumberFormatterCreateNumberFromString``
  instead.

.. note::

   Both function require a manual wrapper to support, implementations are
   welcome.


CFPlugin
........

The ``CFPlugin`` API's are not supported at the moment. Likewise for the
COM interface support in CoreFoundation.


CFRunLoopSource
...............

The 'context' argument for ``CFRunLoopSourceCreate`` should be a tuple. The first
element of the tuple is ``0``, the other elements are: a ``schedule`` callback,
a ``cancel`` callback, a ``perform`` callback and an ``info`` object. The callbacks
may be ``None``.

Version 1 of the context object is not yet supported.

The ``CFRunLoopSourceGetContext`` returns this tuple, and will raise an exception
when the context was not set from Python (that is, when asking for the context of
a runloop source that was created in C code).


CFRunLoopTimer
..............

The ``context`` argument of ``CFRunLoopTimerCreate`` can be an arbitrary python
object. This object is returned by ``CFRunLoopTimerGetContext``.


CFRunLoopObserver
.................

The ``context`` argument of ``CFRunLoopObserverCreate`` can be an arbitrary python
object. This object is returned by ``CFRunLoopObserverGetContext``.


CFSet
.....

* ``CFSetCreate``, ``CFSetCreateMutable``: the ``callbacks`` argument is
  a magic argument in Python, not a collection of function pointers. It
  must be ``kCFTypeSetCallbacks``.

* ``CFSetApplyFunction``: The ``context`` argument can be an arbitrary object.


CFSocket
........

The socket context is an arbitrary object, not a callback structure. This has
several effects:

* Do not try to access the context of sockets that aren't created in Python

* The ``context`` argument for ``CFSocketCreate``, ``CFSocketCreateWithNative``,
  ``CFSocketCreateWithSocketSignature``,
  ``CFSocketCreateConnectedToSocketSignature`` is an arbitrary python object.

* The function ``CFSocketGetContext`` returns that python object and will crash
  when the context was not set from Python.


CFStream
........

* You can use any Python object as the client context for ``CFReadStreamSetClient``
  and ``CFWriteStreamSetClient``. Use ``objc.NULL`` to remove a client.


CFString
........

* The 'Pascal String' API's are not supported (that is,
  ``CFStringAppendPascalString``, ``CFStringCreateWithPascalString``,
  ``CFStringCreateWithPascalStringNoCopy``, ``CFStringGetPascalString``, and
  ``CFStringGetPascalStringPtr``).
  Use the regular Python string API's instead (or access the string
  contents using the ``CString`` functions, use as
  ``CFStringCreateWithCString``).


CFTree
......

* The ``context`` attribute (that is ``context`` argument for
  ``CFTreeCreate`` and ``CFTreeGetContext``) can be an arbitrary python
  object, it is not a ``CFTreeContext`` structure as in C.


CFXMLParser, CFXMLNode
......................

* These API's are not supported for now. The ``Create`` functions need
  manual wrappers, which haven't been written yet. There are also no
  uninttests for the automatically created bindings.

* Use a Python XML parser (such as ElementTree) instead.

CFFileSecurityCopyAccessControlList
...................................

This function is not supported.
