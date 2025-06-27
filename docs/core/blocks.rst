PyObjC support for "blocks"
===========================

Introduction
------------

Objective-C has the concept of "blocks", which are basically anonymous inline
functions. The syntax for them is like this:

.. sourcecode:: objective-c

	^{ printf("x is %d\n", 42); }

This is a literal for a block that takes no arguments and prints a value when
called.

Calling blocks from Python
--------------------------

The Python representation for a block is a callable object, that is you can
call the block just like you call any other function object.

PyObjC manages the memory for blocks, it is not necessary to manage the reference
counts of blocks in your code.

Limitations
...........

Ancient versions of the Apple Objective-C compiler did not include information
to make blocks runtime introspectable. For those systems all APIs returning blocks
need to be annotated with the Objective-C signatures of the returned block.

For all APIs that have a block as its argument the Objective-C signature for the
block needs to be specified through the metadata system.

The required annotations are shipped with PyObjC's bindings for system frameworks,
that is block APIs "just work".

It is possible to retrieve and set the call signature of a block using the
``__block_signature__`` attribute on blocks.

.. versionchanged:: 2.5

   PyObjC can use runtime introspection to retrieve the Objective-C signature
   for a block.


Implementing blocks in Python
-----------------------------

It is very easy to use Objective-C methods that have a block as one of their
arguments: just pass an arbitrary callable. PyObjC will automatically wrap your
callable in the right low-level datastructure.

One of the side-effects of this is that the variour storage classes that are
defined for block-related variables are not relevant for Python users. Blocks
behave just like regular functions.

Metadata for blocks
-------------------

The current implementation of blocks doesn't allow for full introspection,
which means that PyObjC must be taught about the signatures of blocks.  This
is done using the :doc:`metadata system </metadata/index>`.
