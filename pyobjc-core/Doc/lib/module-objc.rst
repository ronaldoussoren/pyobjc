:mod:`objc` -- The PyObjC bridge
================================

.. module:: objc
   :platform: MacOS X
   :synopsis: The PyObjC bridge

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>

Introduction
------------

The module :mod:`objc` is the core of PyObjC and provides the automatic 
bridging between Python and Objective-C. It also provides a number of
utility functions and types that make it easier to integrate Python
and Objective-C code.

The module :mod:`objc` defines a number of functions whose names start with
an underscore. Those functions are private and should not be used, they can
be removed from release without warning.

NOTE: This document is currently mostly an exhaustive list of stuff and 
needs to be reorganised once I've filled in the technical details. 

Debugging
.........

.. function:: setVerbose(yesOrNo)

   When the argument is :const:`True` the bridge will log more information.

   This currently results in output on the standard error stream whenever
   an exception is translated from Python to Objective-C.


.. function:: getVerbose()

   Returns the current value of the verbose flag.


Tweaking behaviour
..................

.. function:: setUseKVOForSetattr

   TODO

.. function:: setHideProtected(yesOrNo)

   When the argument is :const:`True` protected methods of an Objective-C
   class will not be included in the output of :func:`dir`. Protected methods
   are those whose selector starts with an underscore.

   This option is on by default.

.. function:: setStrBrigeEnabled

   TODO

   This function is not available in Python 3.x

.. function:: getStrBridgeEnabled

   TODO

   This function is not available in Python 3.x


Utilities
..........

.. function:: allocateBuffer

   TODO

.. function:: CFToObject

   TODO

.. function:: ObjectToCF

   TODO


Accessing classes and protocols
...............................

.. function:: lookUpClass(classname)

   :param classname: the name of an Objective-C class
   :type classname: string
   :return: the named Objective-C class
   :raise: :exc:`objc.nosuchclass_error` when the class does not exist


.. function:: getClassList()

   :return: a list of a classes known to the Objective-C runtime


.. function:: protocolsForClass

   TODO

.. function:: protocolsForProcess

   TODO


.. function:: propertiesForClass(objcClass)

   :type objcClass: an Objective-C class or formal protocol
   :return: a list of properties from the Objective-C runtime

   The return value is a list with information about
   properties on this class or protocol from the Objective-C runtime. This
   does not include properties superclasses.

   Every entry in the list is dictionary with the following keys:

   =============== =============================================================
   Key             Description
   =============== =============================================================
   ``name``        Name of the property (a string)
   --------------- -------------------------------------------------------------
   ``raw_attr``    Raw value of the attribute string (a byte string)
   --------------- -------------------------------------------------------------
   ``typestr``     The type string for this attribute (a byte string)
   --------------- -------------------------------------------------------------
   ``classname``   When the type string is ``objc._C_ID`` this is the
                   name of the Objective-C class (a string).
   --------------- -------------------------------------------------------------
   ``readonly``    True iff the property is read-only (bool)
   --------------- -------------------------------------------------------------
   ``copy``        True iff the property is copying the value (bool)
   --------------- -------------------------------------------------------------
   ``retain``      True iff the property is retaining the value (bool)
   --------------- -------------------------------------------------------------
   ``nonatomic``   True iff the property is not atomic (bool)
   --------------- -------------------------------------------------------------
   ``dynamic``     True iff the property is dynamic (bool)
   --------------- -------------------------------------------------------------
   ``weak``        True iff the property is weak (bool)
   --------------- -------------------------------------------------------------
   ``collectable`` True iff the property is collectable (bool)
   --------------- -------------------------------------------------------------
   ``getter``      Non-standard selector for the getter method (a byte string)
   --------------- -------------------------------------------------------------
   ``setter``      Non-standard selector for the setter method (a byte string)
   =============== =============================================================

   All values but ``name`` and ``raw_attr`` are optional. The other attributes
   contain a decoded version of the ``raw_attr`` value. The boolean attributes
   should be interpreted as ``False`` when the aren't present.

   The documentation for the Objective-C runtime contains more information about
   property definitions.

   This function only returns information about properties as they are defined
   in the Objective-C runtime, that is using ``@property`` definitions in an
   Objective-C interface. Not all properties as they are commonly used  in
   Objective-C are defined using that syntax, especially properties in classes
   that were introduced before MacOSX 10.5.

   This function always returns an empty list on MacOS X 10.4.

   .. versionadded:: 2.3

.. function:: listInstanceVariables

   TODO

.. function:: getInstanceVariable

   TODO

.. function:: setInstanceVariable

   TODO

.. function:: protocolNamed

   TODO

.. exception:: ProtocolError

   TODO





Dynamic modification of classes
...............................

.. function:: classAddMethods

   TODO

.. function:: classAddMethod

   TODO (Lib/objc/_category)

.. class:: Category

   TODO (Lib/objc/_category)


Plugin bundles
..............


.. function:: currentBundle

   TODO

.. function:: registerPlugin

   TODO: Deprecated

.. function:: pluginBundle

   TODO: Deprecated


Memory management
.................

PyObjC automaticly manages Cocoa reference counts for you, the functions 
in this section help in finetuning this behaviour.

.. function:: recycleAutoreleasePool()

   Flush the NSAutoreleasePool that PyObjC creates on import. Use this
   before entering the application main loop when you do a lot of work
   before starting the main loop.

.. function:: removeAutoreleasePool()

   Use this in plugin bundles to remove the release pool that PyObjC creates
   on import. In plugins this pool will interact in unwanted ways with the
   embedding application.


Test support
............

The functions in this section are present as support code for PyObjC's 
unittests and are not part of the stable API. Please let us know if you
use these functions in your code.

.. function:: splitSignature(typestring)

   Split an encoded Objective-C signature string into the
   encoding strings for seperate types.

   :param typestring: an encoded method signature
   :return: list of type signatures
   :type typestring: byte string
   :rtype: list of byte strings


.. function:: splitStruct(typestring)

    TODO.

.. function:: repythonify

   TODO

Framework wrappers
..................

.. function:: setSignatureForSelector

   TODO

.. function:: pyobjc_id

   TODO

.. function:: loadBundle

   TODO

.. function:: registerCFSignature

   TODO

.. function:: loadBundleVariables

   TODO

.. function:: loadSpecialVar

   TODO

.. function:: loadBundleFunctions

   TODO

.. function:: _loadFunctionList
 
   TODO

.. function:: createOpaquePointerType

   TODO

.. function:: createStructType

   TODO

.. function:: registerMetaDataForSelector

   TODO

.. function:: parseBridgeSupport

   TODO


.. function:: registerListType

   TODO (Lib/objc/_bridges)

.. function:: registerMappingType

   TODO (Lib/objc/_bridges)

.. function:: initFrameworkWrapper

   TODO

.. function:: addConvenienceForSelector

   TODO

.. function:: addConvenienceForClass

   TODO

.. function:: _setClassSetUpHook

   This is a private hook that is called during the creation of a subclass.

   WARNING: This hook is not part of the stable API.

   .. versionadded:: 2.3

.. function:: _setClassExtender

   This is a private hook that's called during the creation of the proxy for
   an Objective-C class.

   WARNING: This hook is not part of the stable API.
   
   .. versionadded:: 2.2

   .. versionchanged:: 2.3
      TODO: In version 2.2 the hook gets called any time the bridge rescans
      a class, in 2.3 the hook only gets called during initial construction
      and has less oportunity to change things.
    

Types
-----

.. class:: objc_class

   TODO: the meta class for Objective-C classes

.. class:: objc_object

   TODO: the root class for Objective-C classes

.. class:: pyobjc_unicode

   TODO: proxy for :ctype:`NSString*`

.. class:: selector

   TODO: an Objective-C method reference

.. class:: FSRef

   TODO: proxy for :ctype:`FSRef`

.. class:: FSSPec

   TODO: proxy for :ctype:`FSSpec`

.. class:: ivar

   TODO: an instance variable reference

.. class:: informal_protocol

   TODO: add section about protocols

.. class:: formal_protocol

   TODO: add section about protocols


.. class:: varlist

   TODO: a varlist is a list of indeteriminate length

.. class:: function

   TODO: a global function in a framework.

.. class:: IMP

   TODO: proxy for :ctype:`IMP`

.. class:: super

   This is a subclass of :class:`super <__builtin__.super>` that works
   properly for Objective-C classes as well as regular Python classes.

   The statement :samp:`from {Framework} import \*` will replace the
   regular :class:`super <__builtin__.super>` by this class.

Constants
---------

.. data:: nil

   Alias for :const:`None`, for easier translation of existing Objective-C
   code.

.. data:: YES

   Alias for :const:`True`, for easier translation of existing Objective-C
   code.

.. data:: NO

   Alias for :const:`False`, for easier translation of existing Objective-C
   code.

.. data:: NULL

   TODO: add description of pass by reference arguments and the 
   difference between None and NULL

.. data:: MAC_OS_X_VERSION_MAX_ALLOWED

   The value of ``MAC_OS_X_VERSION_MAX_ALLOWED`` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_MIN_REQUIRED

   The value of ``MAC_OS_X_VERSION_MIN_REQUIRED`` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_10_N

   There are currently 6 constants of this form, for ``N`` from 1 to 6,
   and these have the same value as the Objective-C constant of the same
   name.
 
.. data:: platform

   This always has the value ``"MACOSX"``.



Objective-C type strings
------------------------

The Objective-C runtime and the PyObjC bridge represent the types of
instance variables and methods arguments and return values as a string
with a compact representation. The Python representation of that string is
a byte string (that is type :class:`bytes` in Python 3.x and :class:`str`
in Python 2.x).

Basic types
............

The representation for basic types is a single character, the table below
lists symbolic constants in the for those constants.

======================== =================================================
Name                     Objective-C type
======================== =================================================
:const:`_C_ID`           :ctype:`id` (an Objective-C instance)
------------------------ ------------------------------------------------- 
:const:`_C_CLASS`        an Objective-C class
------------------------ -------------------------------------------------
:const:`_C_SEL`          a method selector
------------------------ -------------------------------------------------
:const:`_C_CHR`          :ctype:`char`
------------------------ -------------------------------------------------
:const:`_C_UCHR`         :ctype:`unsigned char`
------------------------ -------------------------------------------------
:const:`_C_SHT`          :ctype:`short`
------------------------ -------------------------------------------------
:const:`_C_USHT`         :ctype:`unsigned short`
------------------------ -------------------------------------------------
:const:`_C_BOOL`         :ctype:`bool`  (or :ctype:`_Bool`)
------------------------ -------------------------------------------------
:const:`_C_INT`          :ctype:`int`
------------------------ -------------------------------------------------
:const:`_C_UINT`         :ctype:`unsigned int`
------------------------ -------------------------------------------------
:const:`_C_LNG`          :ctype:`long`
------------------------ -------------------------------------------------
:const:`_C_ULNG`         :ctype:`unsigned long`
------------------------ -------------------------------------------------
:const:`_C_LNG_LNG`      :ctype:`long long`
------------------------ -------------------------------------------------
:const:`_C_ULNG_LNG`     :ctype:`unsigned long long`
------------------------ -------------------------------------------------
:const:`_C_FLT`          :ctype:`float`
------------------------ -------------------------------------------------
:const:`_C_DBL`          :ctype:`double`
------------------------ -------------------------------------------------
:const:`_C_VOID`         :ctype:`void`
------------------------ -------------------------------------------------
:const:`_C_UNDEF`        "other" (such a function)
------------------------ -------------------------------------------------
:const:`_C_CHARPTR`      C string (:ctype:`char*`)
------------------------ -------------------------------------------------
:const:`_C_NSBOOL`       :ctype:`BOOL`
------------------------ -------------------------------------------------
:const:`_C_UNICHAR`      :ctype:`UniChar`
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_TEXT` :ctype:`char` when uses as text or a byte array
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_INT`  :ctype:`int8_t` (or :ctype:`char` when 
                    used as a number)
======================== =================================================

The values :const:`_C_NSBOOL`, :const:`_C_UNICHAR`, :const:`_C_CHAR_AS_TEXT`
and :const:`_C_CHAR_AS_INT` are inventions of PyObjC and are not used in
the Objective-C runtime.

Complex types
..............

More complex types can be represented using longer type strings: 

* a pointer to some type is :const:`_C_PTR` followed by the type string 
  of the pointed-to type.

* a bitfield in a structure is represented as :const:`_C_BFLD` followed
  by an integer with the number of bits. 
  
  Note that PyObjC cannot convert bitfields at this time.

* a C structure is represented as :const:`_C_STRUCT_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_STRUCT_E`. The field name (including the
  closing equals sign) is optional.

* a C union is represented as :const:`_C_UNION_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_UNION_E`. The field name (including the
  closing equals sign) is optional.

  Note that PyObjC cannot convert C unions at this time.

* a C array is represented as :const:`_C_ARY_B` followed by an integer 
  representing the number of items followed by the encoded element type,
  followed by :const:`_C_ARY_E`.

* The C construct 'const' is mapped to :const:`_C_CONST`, that is a 
  :ctype:`const char*` is represented as ``_C_CONST + _C_CHARPTR``.

Additional annotations for method and function arguments
........................................................

Method arguments can have prefixes that closer describe their functionality.
Those prefixes are inheritted from Distributed Objects are not used by the
Objective-C runtime, but are used by PyObjC.

* When a pointer argument is an input argument it is prefixed by
  :const:`_C_IN`.

* When a pointer argument is an output argument it is prefixed by
  :const:`_C_OUT`.

* When a pointer argument is an input and output argument it is prefixed 
  by :const:`_C_INOUT`.

* Distributed objects uses the prefix :const:`_C_BYCOPY` to tell that a 
  value should be copied to the other side instead of sending a proxy
  reference. This is not used by PyObjC.

* Distributed objects uses the prefix :const:`_C_ONEWAY` on the method return
  type to tell that the method result is not used and the caller should not
  wait for a result from the other side. This is not used by PyObjC.

When a pointer argument to a function prefixed by :const:`_C_IN`, 
:const:`_C_OUT` or :const:`_C_INOUT` the brige assumes that it is a pass by
reference argument (that is, a pointer to a single value), unless other 
information is provided to the bridge.

TODO: Write how to write Objective-C code to ensure that the right prefixes
are added by the compiler.

Special encoded types
.....................

The table below shows constants for a number of C types that are used 
in Cocoa but are not basic C types.

  ======================= ==============================
  Constant                Objective-C type
  ======================= ==============================
  :const:`_C_CFTYPEID`    :ctype:`CFTypeID`
  ----------------------- ------------------------------
  :const:`_C_NSInteger`   :ctype:`NSInteger`
  ----------------------- ------------------------------
  :const`:_C_NSUInteger`  :ctype:`NSUInteger`
  ----------------------- ------------------------------
  :const:`_C_CFIndex`     :ctype:`CFIndex`
  ----------------------- ------------------------------
  :const:`_C_CGFloat`     :ctype:`CGFloat`
  ----------------------- ------------------------------
  :const:`_sockaddr_type` :ctype:`struct sockaddr`
  ======================= ==============================


Context pointers
----------------

A number of Objective-C APIs have one argument that is a context pointer,
which is a :ctype:`void*`. In Objective-C your can pass a pointer to an
arbitrary value, in Python this must be an integer.

PyObjC provides a :data:`context` object that can be used to allocate
unique integers and map those to objects.

(NOTE: The markup below here is probably incorrect)

.. function:: context.register(value)

   Add a value to the context registry.

   :param value: An arbitrary object
   :return: A unique integer that's suitable to be used as a context pointer

.. function:: context.unregister(value):

   Remove an object from the context registery, this object must be have
   been added to the registry before.

   :param value: An object in the context registry

.. function:: context.get

   Retrieve an object from the registry given the return value from
   ``context.register``.


Descriptors
-----------

.. function:: IBOutlet([name])

   Creates an instance variable that can be used as an outlet in 
   Interface Builder. When the name is not specified the bridge will 
   use the name from the class dictionary.

   The code block below defines an instance variable named "button" and
   makes that available as an outlet in Interface Builder.

   .. code-block:: python

      class SomeObject (NSObject):

          button = IBOutlet()

.. function:: IBAction

   Mark an method as an action for use in Interface Builder. 
   
   Usage:

   .. code-block:: python

      class SomeObject (NSObject):

         @IBAction
         def saveDocument_(self, sender):
             pass


.. function:: instancemethod

   Explicitly mark a method as an instance method. Use this when
   PyObjC incorrectly deduced that a method should be a class method.

   Usage:

   .. code-block:: python

        class SomeObject (NSObject):

           @instancemethod
           def alloc(self): 
               pass



.. function:: accessor

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

.. function:: typedAccessor(valueType)

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The ``valueType`` is the encoded string for a single value.

.. function:: typedSelector

   Use this decorator to explicitly set the type signature for a method.

   An example:

   .. code-block:: python

        @typedSelector(b'I@:d')
        def makeUnsignedIntegerOfDouble_(self, d):
           return d
   
.. function:: namedSelector(name [, signature])

   Use this decorator to explictly set the Objective-C method name instead
   of deducing it from the Python name. You can optionally set the method
   signature as well.

.. function:: callbackFor(callable, argIndex=-1)

   Use this decorator to tell that this function is the callback for
   an (Objective-C) API.

   TODO: further describe

.. function:: selectorFor

   Decorator to tell that this is the "callback" selector for another 
   API.

   TODO: further describe

.. function:: synthesize

   Use this to synthesize a property with getter and setter methods.

   TODO: futher describe


Interacting with ``@synchronized`` blocks
-----------------------------------------

PyObjC provides an API that implements locking in the same way as the
``@synchronized`` statement in Objective-C.

.. code-block:: python

  with object_lock(anNSObject):
      pass

.. class:: object_lock(value)

   This class represents the mutex that protects an Objective-C object
   for the ``@synchronized`` statement. This can be used as a context
   manager for the ``with`` statement, but can also be used standalone.

   .. method:: lock

      Acquire the object mutex

   .. method:: unlock

      Release the object mutex


Archiving Python and Objective-C objects
----------------------------------------

Python and Objective-C each provide a native object serialization method,
the :mod:`pickle` module in Python and the ``NSCoding`` protocol in Objective-C.

It is possible to use an ``NSKeyedArchiver`` to store any Python object that
can be pickled in an Objective-C serialized data object. 

Due to technical details it is not possible to pickle an Objective-C object,
unless someone explicitly implements the pickle protocol for such an object.

Properties
----------

Introduction
............

Both Python and Objective-C have support for properties, which are object attributes
that are accessed using attribute access syntax but which result in a method call.

The Python built-in :class:`property <__builtin__.property__` is used to define new
properties in plain Python code. These properties don't full interoperate with 
Objective-C code though because they do not necessarily implement the Objective-C
methods that mechanisms like Key-Value Coding use to interact with a class.

PyObjC therefore has a number of property classes that allow you to define new
properties that do interact fully with the Key-Value Coding and Observation
frameworks.

TODO: Implement method for enabling properties on existing classes and tell
why that is off by default and when it will be turned on by default.

TODO: The description is way to minimal, even the design document contained
more information.

.. class:: object_property(name=None, read_only=False, copy=False, dynamic=False, ivar=None, typestr=_C_ID, depends_on=None)


   :param name: Name of the property, the default is to extract the name from the class dictionary
   :param read_only: Is this a read-only property? The default is a read-write property.
   :param copy: Should the default setter method copy values? The default retains the new value without copying.
   :param dynamic: If this argument is ``True`` the property will not generate default accessor, 
   but will rely on some external process to create them.
   :param ivar: Name of the instance variable that's used to store the value. When this value is ``None``
   the name will be calculated from the property name. If it is ``NULL`` there will be no instance variable.
   :param typestr: The Objective-C type for this property, defaults to an arbitrary object.
   :param depends_on: A sequence of names of properties the value of this property depends on.

During the class definition you can add accessor methods by using the property as a decorator


.. method:: object_property.getter

   Decorator for defining the getter method for a property. The name of the method should be the
   same as the property::

       class MyObject (NSObject):

           prop = objc.object_property()

           @prop.getter
           def prop(self):
              return 42


.. method:: object_property.setter

   Decorator for defining the setter method for a property. The name of the method should be the
   same as the property.


.. method:: object_property.validate

   Decorator for defining a Key-Value Coding validator for this property. 

  
It is possible to override property accessor in a subclass::

   class MySubclass (MyObject):
       @MyObject.prop.getter
       def getter(self):
           return "the world"

This can also be used to convert a read-only property to a read-write one
by adding a setter accessor.


Properties for structured types
...............................

Key-Value Coding is slightly different for structured types like sets and
lists (ordered and unordered collections). For this reason PyObjC also provides
subclasses of :class:`object_property` that are tuned for these types.

.. class:: array_property

   This property implements a list-like property. When you access the property
   you will get an object that implements the ``MutableSequence`` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: set_property

   This property implements a set-like property. When you access the property
   you will get an object that implements the ``MutableSet`` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: dict_property

   This property is like an :class:`object_property`, but has an empty
   NSMutableDictionary object as its default value. This type is mostly
   provided to have a complete set of property types.

These collection properties are at this time experimental and do not yet
provide proper hooks for tweaking their behavior. Future versions of PyObjC
will provide such hooks (for example a method that will be called when an
item is inserted in an array property).
