================================================
Converting values between Python and Objective-C
================================================

Introduction
------------

PyObjC provides transparent conversion or proxying of values between Python
and Objective-C. In general this works as expected, this document provides
a detailed guide to how values are converted or proxied.


Basic C types
-------------

The Objective-C language not only has classes and objects, but also has the
basic C types which are not classes. PyObjC converts between those and the
corresponding Python type.

The C type 'char' does not have a unambiguous meaning in C, it is used for
a number of tasks. In the table below the various tasks have been represented
separately: booleans (*BOOL*), representing characters in text
(*char*) and representing small integers (*int8_t*).  PyObjC
uses metadata in the framework wrappers to know when to use which
representation.


============================ ========================
C type                       Python 3.x
============================ ========================
*int8_t*                     :class:`int`
---------------------------- ------------------------
*BOOL*                       :class:`bool`
---------------------------- ------------------------
*char*                       :class:`bytes` of len(1)
---------------------------- ------------------------
*unsigned char*              :class:`int`
---------------------------- ------------------------
*short*                      :class:`int`
---------------------------- ------------------------
*unsigned short*             :class:`int`
---------------------------- ------------------------
*int*                        :class:`int`
---------------------------- ------------------------
*unsigned int*               :class:`int`
---------------------------- ------------------------
*int*                        :class:`int`
---------------------------- ------------------------
*unsigned int*               :class:`int`
---------------------------- ------------------------
*long*                       :class:`int`
---------------------------- ------------------------
*unsigned long*              :class:`int`
---------------------------- ------------------------
*long long*                  :class:`int`
---------------------------- ------------------------
*unsigned long long*         :class:`int`
---------------------------- ------------------------
*float*                      :class:`float`
---------------------------- ------------------------
*double*                     :class:`float`
============================ ========================

PyObjC does range checking when converting values to C, and will raise
:exc:`ValueError` when the input value is out of range.

PyObjC will accept negative values when converting a Python numeric value
to an unsigned integer value. This is done due to limitations in the
metadata creation process, sometimes constant values that are used with
unsigned integer arguments are represented as negative values in the
metadata files.  This feature will be fixed in a future version of PyObjC
and users should therefore not rely on being able to convert negative
values to an unsigned integer type.


Compound C types
----------------

Arrays
......

C Arrays are represented a lists where all elements are of the right basic
type (as described earlier).

.. todo::

   * Array arguments (input, output, use of array.array and other buffers)

   * objc.varlist objects for results of unclear size and their limitations

Structs
.......

C structs are by default represented as Python tuples, and you can always use
tuples of the right arity to pass values to a function.

The framework wrappers also provide wrapper types that provide a nicer interface,
those wrappers can be used with indexed access (like tuples), but also have named
attributes. The wrapper types are mutable, and are comparable with mutable
:func:`namedtuple <collections.namedtuple>` objects.

Unions
......

PyObjC cannot convert to and from C union types at the moment.


Classes and instances
---------------------

TBD

Functions and methods
---------------------

TBD
