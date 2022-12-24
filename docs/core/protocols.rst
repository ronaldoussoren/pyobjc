=======================
PyObjC protocol support
=======================

Introduction
------------

Apple makes use of both formal and informal protocols in the Cocoa framework.
Formal protocols are those protocols that are implemented using Objective-C
protocols:

 .. sourcecode:: objective-c

	@protocol NSFoo <NSSomeProtocol>
	-(int)doesIt;
	@end

Conforming to a formal protocol requires the interface of a class to explicitly
declare that it implements that protocol, and the implementation must implement
all required methods of the protocol.

Informal protocols are defined as categories on NSObject with no implementation:

 .. sourcecode:: objective-c

	@interface NSObject(FooDelegate)
	-(void)optionalFooDelegateMethod;
	@end

Conforming to an informal protocol is much like conforming to a protocol in Python,
the class simply implements the methods as documented.  In most cases, informal
protocols are comprised entirely of optional methods (i.e. NSApplicationDelegate)
and a check is made (i.e. ``-[NSObject respondsToSelector:]``) before sending
the message to the target.

Informal protocols and PyObjC
-----------------------------

PyObjC has an explicit representation for informal protocols.  This makes
it possible to use the protocol description to provide better error messages and
to automatically deduce the method signatures for classes that implement an
informal protocol.

Informal protocols are represented using instances of
:class:`objc.informal_protocol`.  Instances of this class are added to
a internal registration in the bridge, and are automatically used when a new
class is declared. Because of this classes don't have to declare that they
conform to an informal protocol.

Formal protocols and PyObjC
---------------------------

PyObjC also has an explicit representation for formal protocols.

Formal protocols are represented as instances of ``objc.formal_protocol``.
Unlike informal protocols, it is necessary to explicitly declare
conformance to formal protocols.  However, all formal protocols in Cocoa
are also described using ``objc.informal_protocol`` objects.

.. todo::

   Is this necessary? we could also use the same strategy as for informal
   protocols, and drop the informal_protocol wrappers for formal protocols.

Protocol conformance is declared by using a ``protocols`` keyword to
the class definitions:

 .. sourcecode:: python
    :linenos:

	NSLocking = objc.protocolNamed('NSLocking')

	class MyLockingObject(NSObject, protocols=[NSLocking]):
		def lock(self):
			pass

		def unlock(self):
			pass

Alternatively, it is also possible to specify the protocols that the class
conforms to using an attribute named ``__pyobjc_protocols__`` in the class body.

 .. sourcecode:: python
    :linenos:

	NSLocking = objc.protocolNamed('NSLocking')

	class MyLockingObject(NSObject):
                __pyobjc_protocols__ = [NSLocking]

		def lock(self):
			pass

		def unlock(self):
			pass

The class now formally implements the ``NSLocking`` protocol, this can be
verified using the Objective-C introspection methods:

  .. sourcecode:: pycon

	>>> MyLockingObject.pyobjc_classMethods.conformsToProtocol_(NSLocking)
	1

This is useful for API's that require (and check) the implementation of formal
protocols.
