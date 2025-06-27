Free-threading support
======================

PyObjC supports free-threading as introduced in Python 3.13
to run without the GIL.

PyObjC protects against threading issues in its own implementation,
such as exposing partial updates of fields.

Fields defined in Python (``__slots__``, ``objc.ivar``, adding attributes)
are thread-safe, their implementation locks access to the object when
reading and updating.

Note that Apple's frameworks are not necessarily thread safe. The
following is an incomplete list of pitfalls:

* Apple's regular collection classes (such as :class:`NSMutableArray`)
  are not safe for concurrent updates, use locking when one
  thread might update the collection.

* Objective-C properties can be ``nonatomic``, in that case accessing
  these properties concurrently is not thread-safe when one or
  more threads can change the property.

* Not all classes can be used on threads other than the main thread,
  in particular most GUI classes in AppKit.

Please check Apple's documentation on how to use their frameworks
in a thread-safe manner.
