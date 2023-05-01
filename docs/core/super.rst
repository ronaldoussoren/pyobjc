Using ``super()``
=================

The idiomatic way to call methods on a superclass
is using the ``super()`` object to resolve methods
in a super class:

.. sourcecode:: python

   class MyObject(NSObject):
       def init(self):
           self = super().init()
           if self is None:
               return None

           ...
           return self

Because of the way PyObjC is implemented you cannot
use the builtin ``super`` for this, but must use
PyObjC's reimplementation of this builtin:

.. sourcecode:: python

   from objc import super

You must use this exact pattern to use the argumentless
version of ``super``, using ``objc.super()`` in a method
body will result in runtime errors due to the way
the argumentless super fetches the defining class of
the method.

Using this pattern is safe to use in modules that
contain a mix of Python and Cocoa classes, PyObjC's
``super`` reimplements the builtin ``super`` with some
additions to support PyObjC.

Background
..........

PyObjC lazily fills a class ``__dict__`` for two reasons:

1. Correctness: Cocoa classes can change at runtime by way
   of using categories loaded from dynamic libraries. Because
   of this eagerly scanning classes for methods can result
   in an incomplete ``__dict__``. Furthermore the Objective-C
   runtime does not have way to effiencly detect changes
   to a class.

2. Performance: Cocoa contains a large number of classes with
   an even larger number of methods. Eagerly scanning classes
   has a significant overhead when importing framework bindings.

In itself a lazily filled does not cause a problem because the
attribute gets filled as needed. But this is a problem with the
builtin ``super`` because that walks the MRO and directly peeks
in the class ``__dict__`` without a way to intercept this. Because
of this ``objc.super`` is a reimplementation of ``builtin.super``
with special behaviour for Cocoa classes.
