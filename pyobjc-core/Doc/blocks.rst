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

Blocks are only suppored when PyObjC is compiled using an Objective-C compiler
that also supports blocks. 

Calling blocks from Python
--------------------------

The Python representation for a block is a callable object, that is you can
call the block just like you call any other function object.

PyObjC manages the memory for blocks, it is not necessary to manage the reference
counts of blocks in your code.

Limitations
...........

It is not possible to call arbitrary blocks because PyObjC needs to store some
additional metadata for a block. This means it is only possible to call blocks
where the bridge knows the call signature, which means:

* Block was returned from a method for which we know the signature of 
  returned blocks. PyObjC ships with metadata that covers all of Cocoa.

* When a block is stored in a Cocoa datastructure, such as an NSArray, and that
  is the only reference to the block PyObjC will loose the additional information
  that is needed to call the block.

It is possible to retrieve and set the call signature of a block using the 
``__block_signature__`` attribute on blocks.


Implementing blocks in Python
-----------------------------

It is very easy to use Objective-C methods that have a block as one of their
arguments: just pass an arbitrary callable. PyObjC will automaticly wrap your
callable in the right low-level datastructure.

One of the side-effects of this is that the variour storage classes that are
defined for block-related variables are not relevant for Python users. Blocks
behave just like regular functions.

Metadata for blocks
-------------------

The current implementation of blocks doesn't allow for full introspection, 
which means that PyObjC must be taught about the signatures of blocks.  This
is done using the :doc:`metadata system </metadata/index>`.

.. versionchanged:: 2.5
   For basic blocks and (Objective-)C code compiled using a recent enough 
   compiler the bridge can extract the block signature from the runtime.
