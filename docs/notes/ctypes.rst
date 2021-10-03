Integration with ctypes
=======================

The standard library module :mod:`ctypes` can be used to interact
with arbitrary C APIs. PyObjC contains some APIs that make interacting
with ctypes easier by having a way to convert PyObjC objects to and
from instances of :class:`c_void_p <ctypes.c_void_p>`.

Converting Objective-C instances to and from c_void_p
-----------------------------------------------------

* Converting an ``c_void_p`` to a PyObjC proxy type of the
  right type can be done by calling :class:`objc.objc_object`
  with a *c_void_p* argument:

  .. sourcecode:: python

     ctypes_value = ... # Somehow get a ctypes pointer
     instance = objc.objc_object(c_void_p=ctypes_value)

* Converting an PyObjC proxy instance to a ``c_void_p``
  is done by the method :meth:`__c_void_p__ <objc.objc_object.__c_void_p__>`.

Converting Opaque Pointer values to and from c_void_p
-----------------------------------------------------

* Converting an ``c_void_p`` to a PyObjC opaque pointer type
  can be done by calling the proxy type with a
  with a *c_void_p* argument:

  .. sourcecode:: python

     ctypes_value = ... # Somehow get a ctypes pointer
     instance = Foundation.NSZonePtr(c_void_p=ctypes_value)

* Converting an PyObjC proxy instance to a ``c_void_p``
  is done by the method ``__c_void_p__()``.
