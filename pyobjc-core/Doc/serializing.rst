Object-graph serialization
==========================

.. |br| raw:: html

   <br/>

Introduction
------------

Both Python and Cocoa have a standard way to serialize
more or less arbitrary object graphs. In Python this
is done using the :mod:`pickle` module, in Cocoa this
is done with an "NSArchiver" or "NSKeyedArchiver" (for
all objects that implemented the NSCoding protocol).

There is currently only one way to serialize an object
graph that contains both Python and Cocoa objects: using
Cocoa's "NSKeyedArchiver" or "NSArchiver" classes (and
preferably the former). At this time it is not possible to
encode Cocoa objects using the :mod:`pickle` module.

.. todo::

   Explain why it is not possible to pickle Cocoa objects.

Pickling support for Cocoa objects
----------------------------------

It is currently not possible to serialize a arbitrary Cocoa
object into a :mod:`pickle` archive due to slight
incompatibilities in the overal serialization mechanism.

It is possible to pickle a Python subclass of a Cocoa
class when that Python class implements the "__reduce__"
hook.

NSCoding support for Python objects
-----------------------------------

PyObjC implements the NSCoding protocol for any Python object
that can be serialized using :mod:`pickle`. During serialization
and deserialization PyObjC will use the same hooks and mechanisms
as the :mod:`pickle` module.

Archiving instances of :class:`str` (:class:`unicode` in Python 2),
:class:`bytes` (Python 3 only), :class:`list`, :class:`tuple`,
:class:`set`, :class:`frozenset` and :class:`dict` (but not instances
of subclasses of these types) with a plain, not keyed, archiver
and will result in objects of the corresponding Cocoa type when
reading them back, even when reading them back in Python. Programs
than need high fidility when roundtripping object graphs therefore
need to use keyed archiving when possible.

Python subclasses of a Cocoa class can only be archived when they
implement the NSCoding protocol, that is the subclass must implement
"initWithCoder:" and "encodeWithCoder:" to serialize the object
state.

.. note::

   In Mac OS X 10.8, an likely other OSX releases as well, the
   Cocoa collection classes cannot properly archive and unarchive
   object graphs with cycles between collections.

   Because of this serializing the graph below with an NSArchiver
   will result in a grabled datastructure when read back. The
   same will be true when archiving with NSKeyedArchiver and
   reading the archive back in pure Objective-C.

   .. sourcecode:: python

      a = []
      a.append(a)

   This is an unfortunate limitation in Cocoa that PyObjC cannot
   paper over.


Backward compatibility
......................

The format used for serializing Python objects has changed a couple
of times. Because of this it is not always possible to read back
archives created with a newer version of PyObjC using older versions
of PyObjC.

The following table lists the changes in the encoding, with "forward compatible" meaning
that this version of PyObjC can read older archives, and "backward compatible" meaning that older
versions of PyObjC can read back newer archives.

  +-----------+--------------------+--------------------+--------------------------------------+
  | *Version* | *Backward*  |br|   | *Forward* |br|     | *Notes*                              |
  |           | *compatible*       | *compatbile*       |                                      |
  +===========+====================+====================+======================================+
  |           |                    |                    | TODO: check C code                   |
  |           |                    |                    |                                      |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 2.5       | Yes                | Maybe              | Encoding of pure python objects      |
  |           |                    |                    | other than those with explicit       |
  |           |                    |                    | support in PyObjC was broken for a   |
  |           |                    |                    | number of edge cases.                |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 2.5.1     | Yes                | Yes                | Instances of :class:`unicode`        |
  |           |                    |                    | (or :class:`str` in Python 3) or now |
  |           |                    |                    | archived as instances of NSString.   |
  |           |                    |                    | These archives can be read back by   |
  |           |                    |                    | pure Objective-C code, and when using|
  |           |                    |                    | using plain archiving the object will|
  |           |                    |                    | be read as an NSString instance in   |
  |           |                    |                    | Python code.                         |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 3.0       | Yes                | Yes                | Instances of basic types (...)       |
  |           |                    |                    | are archived as instances of the     |
  |           |                    |                    | Cocoa class when using a non-keyed   |
  |           |                    |                    | archiver.                            |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 3.0       | Yes                | No                 | Changes in encoding of               |
  |           |                    |                    | archives for OC_PythonData .         |
  |           |                    |                    | These archives can now be read back  |
  |           |                    |                    | by pure Objective-C programs when    |
  |           |                    |                    | the python object has type           |
  |           |                    |                    | :class:`bytes` (only for Python 3)   |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 3.0       | Yes                | Yes                | Changes in encoding of keyed         |
  |           |                    |                    | archives for OC_PythonArray.         |
  |           |                    |                    | These archives can now be read back  |
  |           |                    |                    | by pure Objective-C programs when    |
  |           |                    |                    | the python object has type           |
  |           |                    |                    | :class:`list` or :class:`tuple`.     |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 3.0       | Yes                | Yes                | Changes in encoding of keyed         |
  |           |                    |                    | archives for OC_PythonDictionary.    |
  |           |                    |                    | These archives can now be read back  |
  |           |                    |                    | by pure Objective-C programs when    |
  |           |                    |                    | the python object has type           |
  |           |                    |                    | :class:`dict`.                       |
  +-----------+--------------------+--------------------+--------------------------------------+
  | 3.0       | No                 | No                 | Changes in encoding of OC_PythonSet. |
  |           |                    |                    | Instances of :class:`set` and        |
  |           |                    |                    | :class:`frozenset` can now be read   |
  |           |                    |                    | back by pure Objective-C code when   |
  |           |                    |                    | using keyed archiving.               |
  +-----------+--------------------+--------------------+--------------------------------------+


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
