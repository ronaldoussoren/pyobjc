Introspecting PyObjC
====================

Introduction
------------

The normal introspection facilities can be used to introspect
Objective-C classes as well. This document describes some
differences between Objective-C classes and normal Python
classes that might cause confusion, as well as some additional
introspection mechanisms.

Using :func:`dir`
------------------

The :func:`dir` function is used to check which attributes
are available on a class or instance, and can be used without
problem on Objective-C classes.

There is a significant difference between regular Python
classes and Objective-C classes w.r.t. class methods:
Objective-C class methods are methods defined on a meta
class, and do not use the :func:`classmethod` decorator.
Because of this ``dir(NSObject)`` only lists instance methods,
and not class methods, use ``dir(type(NSObject))`` to list
the class methods of an Objective-C class.

.. note::

   Class methods are methods on a meta class because Objective-C
   classes can have class- and instance-methods with the same
   name, for example ``+[NSObject description]`` and
   ``-[NSObject description]``.


Using :mod:`pydoc` or :func:`help`
----------------------------------

:mod:`Pydoc <pydoc>`, and the :func:`help` function in the
interactive interpreter, can introspect Objective-C classes,
but might not give as much information as you'd like.

As with :func:`dir`, class methods are not mentioned in the
documentation for a class, and it is not yet clear if it is
possible to teach :mod:`pydoc` to list methods on the metaclass.

For python versions earlier than 3.4 the prototype of methods lists
``...`` instead of an actual argument list. That's due to a
limitation in :mod:`pydoc` w.r.t.  functions implemented in C.
The documentation string does list a full prototype, and
information about arguments.


Function and method metadata
----------------------------

Objective-C methods and functions have an ``__metadata__`` method
that can be used to retrieve the information that the bridge
has about a specific method or function.

The result of this function is a copy of a :ref:`metadata dictionary <metadata-dictionary>`.


Type attributes
---------------

The struct and opaque pointer types created by PyObjC have
a ``__typestr__`` attribute. This attribute contains the Objective-C
type encoding for variables of this type.


Introspecting instance variables
--------------------------------

The functions :func:`listInstanceVariables`, :func:`getInstanceVariable`
and :func:`setInstanceVariable` can be used to introspect, and
change, instance variables of arbitrary Objective-C objects,
irrespecitive of whether or not those variables are public.

This can be useful during debugging, or when exploring the internals
of a framework implementation, but shouldn't be used in production code:
instance variables aren't part of public API and could therefore change
without notice between releases. Changing instance variables can
break class invariants and might cause misbehavior (including hard
crashes).

.. _`issue #17053 in Python's tracker`: https://bugs.python.org/issue17053
