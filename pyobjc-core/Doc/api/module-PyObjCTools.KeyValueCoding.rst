:mod:`PyObjCTools.KeyValueCoding` -- Key-Value Coding API 
=========================================================

.. module:: PyObjCTools.KeyValueCoding
   :platform: MacOS X
   :synopsis: Key-Value Coding API

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>

Support for Key-Value Coding in Python. This provides a simple functional
interface to Cocoa's Key-Value coding that also works for regular Python
objects.

Key-Value Coding is Cocoa functionality that is simular to
the :func:`getattr` and :func:`setattr` functions in Python. The APIs
in this module are modelled on those functions and work on 
Cocoa objects as well as basic Python objects.

Key-Value Coding works with keys, basically attribute names, as well as
key-paths. A key-path is a string that contains a sequence of dot-separated
keys and is used to chain a number of keys together.

Accessor functions
------------------

.. function:: getKey(object, key)

   Return the value of the attribute referenced by ``key``. The key
   is used to build the name of an accessor method or attribute name. 

   The following methods are tried for regular Python objects:

   * Accessor method ``getKey``

   * Accessor method ``get_key``

   * Accessor method or attribute ``key``

   * Accessor meethod or attribute ``isKey``

   * Attribute ``_key``
 
   (In all of these "key" is replaced by the value of ``key``).

   This function calls the regular Key-Value Coding methods for Cocoa objects,
   including those implemented in Python.

   :param object: An arbitrary object
   :param key: name of a key
   :type key: string
   :result: the value of a key
   :raise: :exc:`KeyError` when the key does not exist.


.. function:: setKey(object, key, value)

   Set the value of the attribute referenced by ``key`` to
   ``key``. The key is used to build the name of an accessor 
   method or attribute name. 

   The following methods are tried for regular Python objects:

   * Accessor method ``setKey``

   * Accessor method ``set_key``

   * attribute ``_key``

   * Attribute ``key``
 
   (In all of these "key" is replaced by the value of ``key``).

   This function calls the regular Key-Value Coding methods for Cocoa objects,
   including those implemented in Python.

   :param object: An arbitrary object
   :param key: name of a key
   :param value: The value to set
   :type key: string
   :result: the value of a key
   :raise: :exc:`KeyError` when the key does not exist.


.. function:: getKeyPath(object, keypath)

   The ``keypath`` is a string containing a path of keys. The keys
   are separated by colons, for example :data:`"owner.firstName"`. 

   The key path is used to traverse an object graph to an attribute. This
   function also supports set and array operators. Those are keys of 
   the form ``@operator`` are are used as ``pathToArray.@operator.pathToProperty``,
   for example ``system.disks.@max.capacity``. 

   The table below lists the supported array operators

   =========================== =======================================================
   Operator
   =========================== =======================================================
   ``avg``                     Use the rest of the keypath to fetch the value 
                               of each item in the container and returns the
			       average of those values.
   --------------------------- -------------------------------------------------------
   ``count``                   Returns the number of items in the container
   --------------------------- -------------------------------------------------------
   ``distinctUnionOfArrays``   Use the rest of the keypath to fetch the value of
                               each item, which must be a sequence. Those sequences
			       are merged into an array with distict values.
   --------------------------- -------------------------------------------------------
   ``distinctUnionOfObjects``  Use the rest of the keypath to fetch the value of
                               each item and return an array with all distinct
			       values.
   --------------------------- -------------------------------------------------------
   ``max``		       Use the rest of the keypath to fetch the value
		               of each item in the container and returns the
			       maximum of those values.
   --------------------------- -------------------------------------------------------
   ``min``		       Use the rest of the keypath to fetch the value
		               of each item in the container and returns the
			       minimum of those values.
   --------------------------- -------------------------------------------------------
   ``sum``		       Use the rest of the keypath to fetch the value
		               of each item in the container and returns the
			       sum of those values.
   --------------------------- -------------------------------------------------------
   ``unionOfArrays``	       Like ``distinctUnionOfArrays``, but without
                               removing duplicates.
   --------------------------- -------------------------------------------------------
   ``unionOfObjects``	       Like ``distinctUnionOfObjects``, but without
                               removing duplicates
   =========================== =======================================================

   This function calls the regular Key-Value Coding method for Cocoa objects.

   :param object: An arbitrary object
   :param keypath: The keypath, colon seperated keys
   :type keypath: string

.. function setKeyPath(object, keypath, value)

   The ``keypath`` is a string containing a path of keys. The keys
   are separated by colons, for example :data:`"owner.firstName"`. 

   The key path is used to traverse an object graph to an attribute and
   the value is then set simularly to how :func:`setKey` sets the value.
   
   :param object: An arbitrary object
   :param keypath: The keypath, colon seperated keys
   :type keypath: string
   :param value: The value to set


Key-Value Coding wrapper
------------------------

.. class:: kvc(value)

   This wrappers ``value`` in an object that uses KeyValue Coding
   to implement the attribute and item accessors.

   .. method __getattr__(key)

      Returns ``getKey(self, key)``.

   .. method __setattr__(key, value)

      Returns ``setKey(self, key, value)`` if the key
      does not start with an underscore. 
      
      Sets an attribute of the wrapper
      when the key does start with an undercore.

   .. method __getitem_(self, keypath)

      Returns ``getKeyPath(self, keypath)``

   .. method __setitem_(self, keypath, value)

      Returns ``setKeyPath(self, keypath, value)``
