Object-graph serialization
==========================

Introduction
------------

Both Python and Cocoa have a standard way to serialize
more or less arbitrary object graphs. In Python this
is done using the :mod:`pickle` module, in Cocoa this
is done with an "NSArchiver" or "NSKeyedArchiver" (for
all objects that implemented the NSCoding protocol).

There is currently only one way to serialize an object
graph that contains both Python and Cocoa objects: using
Cocoa's "NSArchiver" or "NSKeyedArchiver" classes. At this
time it is not possible to encode Cocoa objects using the
:mod:`pickle` module.

.. todo::

   Explain why it is not possible to pickle Cocoa objects.

NSCoding support for Python objects
-----------------------------------

PyObjC implements the NSCoding protocol for any Python object
that can be serialized using :mod:`pickle`. During serialization
and deserialization PyObjC will use the same hooks and mechanisms
as the :mod:`pickle` module.

.. todo::

   Does PyObjC automaticly implement NSCoding for subclasses of
   NSObject that implemented NSCoding?

Backward compatibility
......................

The format used for serializing Python objects has changed a couple
of times. Because of this it is not always possible to read back
archives created with a newer version of PyObjC using older versions
of PyObjC.

.. todo::

   Insert table that lists incompatibilities.

Backward compatibility code does ensure that newer versions of PyObjC
can read archives created by older versions of PyObjC


Interoperability with pure Objective-C programs
...............................................

A pure Objective-C program (that is, one where PyObjC is not loaded)
can read back a limited subset of archives created by PyObjC.

In particular, the following subset of objects are encoded in such
a way that they can be read back by pure Objective-C programs:

* Instances of :class:`dict`, :class:`list`, :class:`tuple`,
  :class:`set`, :class:`frozenset` (but not subclasses of these classes)
  when all values in these containers are compatible as well.

* Instances of :class:`float`, :class:`bool`.

* Instances of :class:`int` (or :class:`long` on Python 2) when the value
  can be represented as a 64-bit signed or unsigned integer.

* Instances of unicode strings (:class:`str` on Python 3 and :class:`unicode` on
  Python 2), but not instances of subclasses of the builtin unicode type.

* Instances of :class:`bytes`, but only for Python 3

* Instances of Cocoa objects that implement the NSCoding protocol, both for
  "native" classes and classes implemented in Python.
