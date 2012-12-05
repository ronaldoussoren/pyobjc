:mod:`objc` -- The PyObjC bridge
================================

.. module:: objc
   :platform: MacOS X
   :synopsis: The PyObjC bridge

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>

.. todo::

   This document is too long and needs to be split.


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

   Sets the default value for the *__useKVO__* attribute on
   classes defined after this call. Returns the previous value.

   When the *__useKVO__* attribute of a class is true instances
   of the class will generate Key-Value Observation notifications when
   setting attributes from Python.

.. function:: setHideProtected(yesOrNo)

   When the argument is :const:`True` protected methods of an Objective-C
   class will not be included in the output of :func:`dir`. Protected methods
   are those whose selector starts with an underscore.

   This option is on by default.

.. function:: setStrBridgeEnabled(yesOrNo)

   If *yesOrNo* is true instances of :class:`str` are bridged
   as NSString instances, otherwise bridging issues a :data:`PyObjCStrBridgeWarning`
   warning and still bridges as an NSString instances.

   By default PyObjC behaves as if ``setStrBridgeEnabled(True)`` was called.

   .. note::
   
      This function is not available in Python 3.x

   .. note::

      Setting this option to false is discouraged and is mostly usefull when porting
      to Python 3.

.. function:: getStrBridgeEnabled

   Returns :data:`True` if the str bridge is enabled and :data:`False` when it is
   not.

   .. note::
   
      This function is not available in Python 3.x


Utilities
..........

.. function:: allocateBuffer(size)

   Returns a writable buffer object of *size* bytes.

.. function:: CFToObject

   Converts an object from the standard library :mod:`CF` module to a
   PyObjC wrapper for the same CoreFoundation object. Raises an exception
   when the conversion fails. 

   .. deprecated:: 2.4
      part of support for the CF module in the python 2 std. library, 
      will be removed in PyObjC 3.0.

   .. note::
      this function is not available for Python 3.


.. function:: ObjectToCF

   Converts a PyObjC wrapper for a CoreFoundation object to an object from the standard 
   library :mod:`CF` module for the same CoreFoundation object. Raises an exception
   when the conversion fails. 

   .. deprecated:: 2.4
      part of support for the CF module in the python 2 std. library, 
      will be removed in PyObjC 3.0.

   .. note::
      this function is not available for Python 3.



Accessing classes and protocols
...............................

.. function:: lookUpClass(classname)

   :param classname: the name of an Objective-C class
   :type classname: string
   :return: the named Objective-C class
   :raise: :exc:`objc.nosuchclass_error` when the class does not exist


.. function:: getClassList()

   :return: a list of a classes known to the Objective-C runtime


.. function:: protocolsForClass(cls)

   Returns a list of Protocol objects that the class claims to 
   implement directly. The *cls* object must a subclass of NSObject.

.. function:: protocolsForProcess

   Returns a list of all Protocol objects known to the Objective-C
   runtime.

.. function:: propertiesForClass(objcClass)

   :type objcClass: an Objective-C class or formal protocol
   :return: a list of properties from the Objective-C runtime

   The return value is a list with information about
   properties on this class or protocol from the Objective-C runtime. This
   does not include properties superclasses.

   Every entry in the list is dictionary with the following keys:

   ============= =============================================================
   Key           Description
   ============= =============================================================
   *name*        Name of the property (a string)
   ------------- -------------------------------------------------------------
   *raw_attr*    Raw value of the attribute string (a byte string)
   ------------- -------------------------------------------------------------
   *typestr*     The type string for this attribute (a byte string)
   ------------- -------------------------------------------------------------
   *classname*   When the type string is ``objc._C_ID`` this is the
                 name of the Objective-C class (a string).
   ------------- -------------------------------------------------------------
   *readonly*    True iff the property is read-only (bool)
   ------------- -------------------------------------------------------------
   *copy*        True iff the property is copying the value (bool)
   ------------- -------------------------------------------------------------
   *retain*      True iff the property is retaining the value (bool)
   ------------- -------------------------------------------------------------
   *nonatomic*   True iff the property is not atomic (bool)
   ------------- -------------------------------------------------------------
   *dynamic*     True iff the property is dynamic (bool)
   ------------- -------------------------------------------------------------
   *weak*        True iff the property is weak (bool)
   ------------- -------------------------------------------------------------
   *collectable* True iff the property is collectable (bool)
   ------------- -------------------------------------------------------------
   *getter*      Non-standard selector for the getter method (a byte string)
   ------------- -------------------------------------------------------------
   *setter*      Non-standard selector for the setter method (a byte string)
   ============= =============================================================

   All values but *name* and *raw_attr* are optional. The other attributes
   contain a decoded version of the *raw_attr* value. The boolean attributes
   should be interpreted as :data:`False` when the aren't present.

   The documentation for the Objective-C runtime contains more information about
   property definitions.

   This function only returns information about properties as they are defined
   in the Objective-C runtime, that is using ``@property`` definitions in an
   Objective-C interface. Not all properties as they are commonly used  in
   Objective-C are defined using that syntax, especially properties in classes
   that were introduced before MacOSX 10.5.

   This function always returns an empty list on MacOS X 10.4.

   .. versionadded:: 2.3

.. function:: listInstanceVariables(classOrInstance)

   Returns a list of information about all instance variables for
   a class or instance. *ClassOrInstance* must be a subclass of NSObject,
   or an instance of such a class.

   The elements of the list are tuples with two elements: a string with
   the name of the instance variable and a byte string with the type encoding
   of the instance variable.

.. function:: getInstanceVariable(object, name)

   Returns the value of the instance variable *name*. 

   .. warning:: 

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.

.. function:: setInstanceVariable(object, name, value[ ,updateRefCounts])

   Set the value of instance variable *name* to *value*. When the instance variable
   type encoding is :data:`objc._C_ID` *updateRefCounts* must be specified and tells
   whether or not the retainCount of the old and new values are updated.

   .. warning:: 

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.


.. function:: protocolNamed(name)

   Returns a Protocol object for the named protocol. Raises :exc:`ProtocolError`
   when the protocol does not exist.

   This is the equivalent of ``@protocol(name)`` in Objective-C.

.. exception:: ProtocolError

   Raised by :func:`protocolNamed` when looking up a protocol that does not
   exist.


Dynamic modification of classes
...............................

.. function:: classAddMethods(cls, methods)

   Add a sequence of methods to the given class. 
   
   The effect is simular to how categories work in Objective-C. If the class
   already implements a method that is defined in *methods* the existing
   implementation is replaced by the new one.

   The objects in *methods* should be one of:

   * :class:`selector` instances with a callable (that is, the first argument
     to :class:`selector` must not be :data:`None`).

   * :class:`classmethod` or :class:`staticmethod` instances that wrap a
     function object.

   * functions

   * unbound methods

   For the last two the method selector is calculated using the regular
   algoritm for this (e.g. as if ``selector(item)`` was called). The last
   two are instance methods by default, but automaticly made class methods
   when the class (or a superclass) has a class method with the same
   selector.

.. function:: classAddMethod(cls, name, method)

   Adds function *method* as selector *name* to the given class. When *method*
   is a selector the signature and class-method-ness are copied from the selector.

   .. note::

      Adding a selector that's defined in Objective-C to another class will raise
      an exception.

.. class:: Category

   A helper class for adding a category to an existing Objecive-C class (subclass
   of :c:type:`NSObject`).

   Usage::

       class NSObject (Category(NSObject)):
          def method(self):
              pass

   The metaclass uses :func:`classAddMethods` to add the methods in the category
   body to the base class.
   
   The name of the class must be the same as the argument to :class:`Category`.


Plugin bundles
..............


.. function:: currentBundle

   During module initialization this function returns an NSBundle object for
   the current bundle. This works for application as well as plug-ins created 
   using `py2app <http://packages.python.org/py2app>`_.

   After module initialization use ``NSBundle.bundleForClass_(ClassInYourBundle)``
   to get the bundle.

.. function:: registerPlugin(pluginName)

   .. deprecated:: 2.3
      use :func:`currentBundle` instead

   Register the current py2app plugin by named and return its bundle.

.. function:: pluginBundle(pluginName)

   .. deprecated:: 2.3
      use :func:`currentBundle` instead

   Return the main bundle for a named plugin. This should only be used
   after it has been register with :func:`registerPlugin`.



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

   :param typestring: an encoded method signature (byte string)
   :return: list of type signatures
   :type typestring: byte string
   :rtype: list of byte strings


.. function:: splitStructSignature(typestring)

   Returns (structname, fields). *Structname* is a string or :data:`None` and
   *fields* is a list of (name, typestr) values. The *name* is a string or
   :data:`None` and the *typestr* is a byte string.

   Raises :exc:`ValueError` when the type is not the type string for a struct
   type.


.. function:: repythonify(object [, type])

   Internal API for converting an object to a given Objetive-C type
   and converting it back again.


Framework wrappers
..................

.. function:: pyobjc_id(obj)

   Returns the address of the underlying object as an integer.

   .. note::

      This is basicly the same as :func:`id`, but for the Objective-C 
      object wrapped by PyObjC instead of python objects.

.. function:: loadBundle(module_name, module_globals [, bundle_path [, bundle_identifier[, scan_classes]]])

   Load the bundle specified by *bundle_path* or *bundle_identifier* and add the classes
   in the bundle to *module_globals*. The classes are not added to the *module_globals* when
   *scan_classes* is :data:`False` (it defaults to :data:`True`).

   If both a *bundle_path* and *bundle_identifier* are specified the function first tries
   to locate the bundle using the identifier and then using the path.

   When *bundle_identifier* is specified the bundle is located using ``[NSBundle +bundleWithIdentifier:]``,
   and when *bundle_path* is specified the bundle is located using ``[NSBundle +bundleWithPath:]``.

   .. note::

      *bundle_path* must be an absolute path.

   .. note::
      
      The current implementation loads *all* Objective-C classes into *module_globals*, as
      testing if a class is located in a specific bundle is fairly expensive and slowed down
      application initialization too much.

   
.. function:: registerCFSignature(name, encoding, typeId[, tollfreeName])

   Register a CoreFoundation based type with the bridge. If *tollfreeName* is specified
   the type is tollfree bridged to that Objective-C class. 

   The value of *typeId* is :data:`None` for tollfree bridged types, and the result
   of the "GetTypeID" function for the type for other types.

   Returns the class object for the registerd type.


.. function:: loadBundleVariables(bundle, module_globals, variableInfo[, skip_undefined])

   Loads a list of global variables (constants) from a bundle and adds proxy objects for
   them to the *module_globals* dictionary. If *skip_undefined* is :data:`True` (the default)
   the function will skip entries that don't refer to existing variables, otherwise it 
   raises an :exc:`error` exception for these variables.

   *variableInfo* is a sequence of variable descriptions. Every description is a tuple
   of two elements: the variable name (a string) and the type encoding for the variable
   (a byte string).


.. function:: loadSpecialVar(bundle, module_globals, typeid, name[, skip_undefined])

   This function loads a global variable from a bundle and adds it to the *module_globals*
   dictionary. The variable should be a CoreFoundation based type, with a value that 
   is not a valid pointer.

   If *skip_undefined* is :data:`True` (the default) the function won't raise and exception
   when the variable is not present. Otherwise the function will raise an :exc:`error` exception.


.. function:: loadBundleFunctions(bundle, module_globals, functionInfo[, skip_undefined])

   Loads a list of functions from a bundle and adds proxy objects for
   them to the *module_globals* dictionary. If *skip_undefined* is :data:`True` (the default)
   the function will skip entries that don't refer to existing functions, otherwise it 
   raises an :exc:`error` exception for these functions.

   *bundle* is either an *NSBundle* instance, or :data:`None`. When a bundle is specified
   the function is looked up in that bundle, otherwise the function is looked up in
   any bundle (including the main program and Python extensions).

   *functionInfo* is a sequence of function descriptions. Every description is a tuple
   of two or four elements: the function name (a string) and signature (a byte string) and 
   optionally a value for the "\__doc__" attribute and a metadata dictionary.


.. function:: loadFunctionList(list, module_globals, functionInfo[, skip_undefined])

   Simular to :func:`loadBundleFunctions`, but loads the functions from *list* instead
   of a bundle.

   *List* should be a capsule object with tag "objc.__inline__" and the value should
   be a pointer to an array of structs with the following definition:

   .. sourcecode:: objective-c

      struct function {
          char*  name;
          void   (*function)(void);
      };

   ..  x*

   The last item in the array must have a :c:data:`NULL` pointer in the name field.


.. function:: createOpaquePointerType(name, typestr, doc)

   Return a wrapper type for opaque pointers ("handles") of a given type. 
   The type will be registered with the bridge and will be used to wrap 
   values with the given type signature.

.. function:: createStructType(name, typestr, fieldnames, doc[, pack])

   Create a type to wrap structs with a given name and type signature, this
   type will be used by the bridge to convert values of this structure to Python.

   This also adds a class method named *name* to :class:`objc.ivar`. This class
   method creates a new instance variable with the struct type as its type.

   * *name* is a string with the name of the structure, for example "NSPoint".

   * *typestr* is the encoded type of the structure and can optionally 
     contain embedded field names

   * *fieldnames* is a list with the field names, the value can be :data:`None`
     when the *typestr* contains embedded field names.

   * *doc* is the value of \__doc__ for the new type

   * *pack* can be used to specify the value of "#pragma pack" for the structure
     (default is to use the default platform packing for structures).


   The created type behaves itself simular to a mutable :func:`namedtuple <collections.namedtuple>`,
   that is items can be accessed both using attribute access and using the sequence interface.

   An example::

      Point = objc.createStructType("Point", b"{Point=dd}", ["x", "y"])

      p = Point(3.0, 4.0)

      # Set the X field in two ways:
      p.x = 5
      p[0] = 6

   The generated type als has a number of methods:

   * *_asdict()*:  Returns a dict that maps from field names to attribute values

   * *_replace(**kwds)*: Return a copy of the struct and replace attribute values with values from the keyword arguments

   * *copy()*: Return a copy of the struct. If an attribute is another struct that attribute gets copied as well, other attributes
     are not copied. That is, struct types are deep copied other types are shallow copied.

   And the following attributes are present:

   * *_fields*: A list of field names

   * *__typestr__*: The Objective-C type encoding for the struct (without embedded field names)


   .. versionchanged:: 2.5
      The function creates a class method on :class:`objc.ivar`.

   .. versionchanged:: 2.5
      The type now implements the "_asdict" and "_replace" methods that
      are also present on :func:`collections.namedtuple` types. The
      attribute "_fields" was added as well.

.. function:: registerStructAlias(typestr, structType)

   Tell the brige that structures with encoding *typestr* should also be 
   coverted to Python using *structType* (a type created using :func:`createStructType`).

   .. deprecated:: 2.5
      Use :func:`createStructAlias` instead.

.. function:: createStructAlias(name, typestr, structType)

   Tell the brige that structures with encoding *typestr* should also be 
   coverted to Python using *structType* (a type created using 
   :func:`createStructType`).

   This also adds a class method named *name* to :class:`objc.ivar`. This class
   method creates a new instance variable with the struct type as its type.

   .. versionadded: 2.5

.. function:: registerMetaDataForSelector(class\_, selector, metadata)

   Register a metadata structure for the given selector.

   .. todo:: insert reference to metadata documentation

.. function:: registerListType(type)

   Register *type* as a list-like type that will be bridged to Objective-C as an NSArray subclass.


.. function:: registerMappingType(type)

   Register *type* as a dict-like type that will be bridged to Objective-C as an NSDictionary subclass.


.. function:: addConvenienceForSelector(selector, methods)

    Add a list of method to every class that has *selector* as a selector.
    These additional methods are not added to the Objective-C class, but are 
    only visibile in Python code.

    The *methods* argument is a list of tuples (methodname, function).

   .. deprecated:: 2.5

      This function is deprecated, future versions of PyObjC will use a different way
      to initialise classes that will require us to remove this function.


.. function:: addConvenienceForClass(classname, method)

    Add a list of method the named class when that class is initialized, the class
    need not be loaded at the time of this call. These additional methods are not
    added to the Objective-C class, but are only visibile in Python code.

    The *methods* argument is a list of tuples (methodname, function).


.. function:: _setClassSetUpHook

   This is a private hook that is called during the creation of a subclass.

   .. warning:: 
      This hook is not part of the stable API.  

   .. versionadded:: 2.3

.. function:: _setClassExtender

   This is a private hook that's called during the creation of the proxy for
   an Objective-C class.

   .. warning:: 
      This hook is not part of the stable API.
   
   .. versionadded:: 2.2

   .. versionchanged:: 2.3
      In version 2.2 the hook gets called any time the bridge rescans
      a class, in 2.3 the hook only gets called during initial construction
      and has less oportunity to change things.


Types
-----

.. class:: objc_class

   This class is the metatype for Objective-C classes and provides no user-visible
   behavior.

.. class:: objc_object

   This class is the root class for Objective-C classes, that is all wrappers for
   Objective-C classes are a subclass of this class. It is not possible to instantiate
   instances of Objective-C classes by using the class as a callable, instances are
   created using the standard Objective-C mechanisms instead.

   .. data:: pyobjc_ISA

      Read-only property that returns the current Objective-C classes of an object.

   .. data:: pyobjc_instanceMethods

      Read-only property that provides explicit access to just the instance methods
      of an object.

   .. data:: \__block_signature__

      Property with the type signature for calling a block, or :data:`None`.

   .. method:: __cobject__()

      Returns a capsule object with identifier "objc.__object__" and the a reference
      to the Objective-C object as the value.

   .. method:: __reduce__()

      This method ensures that Objective-C objects will not be pickled unless the subclass
      explictly implements the pickle protocol. This is needed because the pickle will
      write an incomplete serialization of Objective-C objects for protocol 2 or later.

   .. note::

      The wrapper classes for the :c:type:`NSString` class cluster aren't subclasses
      of :class:`objc_object`, but are subclasses of the builtin :class:`unicode` type
      (:class:`str:` in Python 3).

.. class:: pyobjc_unicode

   This class is used to wrap instances of the :c:type:`NSString` class cluster and is
   a subclass of the builtin Unicode type (:class:`unicode` for python 2 and :class:`str` 
   for Python 3).

   Methods of the underlying :c:type:`NSString` class can be accessed at as methods
   of the python type, unless they have the same name as a method of the built-in Unicode
   type.

   .. method:: nsstring

      Returns an instance of a subclass of :class:`objc_object` that represents the
      string. This provides full access to the Cocoa string API, but without easy
      interoperability with Python APIs.


   .. warning::

      Instances of :c:type:`NSString` can be mutable. Mutations to mutable Cocoa
      strings are not reflected in instances of :class:`pyobjc_unicode`, use
      :meth:`nsstring` and explict conversion to the built-in unicode type when
      you work with mutable :c:type:`NSString` values.

   .. note::

      Cocoa strings are wrapped using a subclass of the built-in unicode string
      to get better interaction between Python and Cocoa. Because Cocoa strings are
      instances of the built-in unicode type they can be passed to functions in
      extension modules that expect unicode arguments (in particular the file 
      system access APIs such as :func:`open`).


.. class:: selector(function[, selector[, signature[, isClassMethod[, returnType[, argumentTypes[, isRequired]]]]]])

   This type is used to represent an Objective-C method. 

   :param function:  The Python callable that is used for the method. Can be a :class:`classmethod` , but not a :class:`staticmethod`.
   :param selector:  The Objective-C selector for the method. The default is calculated from the \__name__ attribute for *function*
   :param signature: The type encoding for the method, the default signature assumes that all arguments and the result are objects
                     (or 'void' when the function does not contain a return statement with a value).
   :param isClassMethod: Used to specify if a method is a class method (default is :data:`True` if *function* is a :class:`classmethod`
                     and :data:`False` otherwise)
   :param returnType: Alternative method for specifying the method return type, using the syntax of :c:func:`Py_BuildValue`.
   :param argumentTypes: Alternative method for specifying argument types, using the syntax of :c:func:`Py_BuildValue`.
   :param isRequired:    Specify if the method is required (defaults to :data:`True`), used in the definition of protocols.

   The arguments *returnType* and *argumentTypes* are deprecated in PyObjC 2.5, they are confusing and can only specify
   a subset of types.

   .. data:: callable

      Read-only property with access to the underlying callable (the *function* argument to the constructor).

   .. data:: __doc__

      Documentation string for the selector

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector. 

      .. todo:: insert link to metadata description


.. class:: ivar([name[, type[, isOutlet]]])

   Creates a descriptor for accessing an Objective-C instance variable. This should only
   be used in the definition of an Objective-C subclass, the bridge will use this information
   to create an instance variable with the same name on the Objective-C class itself.

   :param name: Name of the instance variable. The name defaults to the name the instance
                variable is bound to in a class definition.

   :param type: Type encoding for the instance varialble. Defaults to :data:`_C_ID` (that is,
                an object)

   :param isOutlet: If :data:`True` the instance variable is used as an outlet, by default
                the instance variable is not an outlet.

   .. note::
      Sharing an ivar object between multiple class definitions is not supported.


   Instances of :class:`ivar` have a number of attributes that help with introspection:
   
   * *__typestr__*: The type encoding of the Objective-C type of the variable

   * *__name__*: The Objective-C name of the variable

   * *__isOutlet__*: :data:`True` if the variable is an :func:`IBOutlet`

   * *__isSlot__*: :data:`True` if the variable is a Python slot.

   .. note::

      You cannot access these attributes  through an Objective-C instance, you have to access
      them through the class object. That's because :class:`ivar` is a data descriptor.

   .. seealso::

      Function :func:`IBOutlet`
         Definition of outlets.


.. class:: informal_protocol(name, selector_list)

   This class is used to specify which methods are part of an informal protocol
   in Objective-C. Informal protocols are a documentation construct in Objective-C and
   as such are not present in the Objective-C runtime (as opposed to formal protocols).

   Informal protocols are used by the bridge to automaticly update method signatures when
   a class appears to implement an informal protocol. This makes it possible the define
   a large subset of Cocoa functionality without manually setting method signatures.

   :param name: Name of the protocol
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. data:: __name__

      Read-only property with the protocol name

   .. data:: selectors

      Read-only property with the sequence of selectors for this protocol


.. class:: formal_protocol(name, supers, selector_list)

   This class is used to represent formal protocols in Python, and is comparabile with the
   "@protocol" construct in Objective-C.

   :param name:     The name of the protocol
   :param supers:   A list of protocols this protocol inherits from
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. note::

      Constructing new protocols is supported on a subset of Mac OS X platforms:

      * All 32-bit programs

      * 64-bit programs starting from Mac OS X 10.7, but only when PyObjC was build with
        the 10.7 SDK (or later)

   .. data:: __name__

      Read-only property with the name of the protocol

   .. method:: name

      Returns the name of the protocol

   .. method:: conformsTo_(proto)

      Returns :data:`True` if this protocol conforms to protocol *proto*, returns :data:`False` otherwise.

   .. method:: descriptionForInstanceMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: descriptionForClassMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: instanceMethods()

      Returns a list of instance methods in this protocol.

   .. method:: classMethods()

      Returns a list of instance methods in this protocol.

   .. note::

      The interface of this class gives the impression that a protocol instance is an Objective-C
      object. That was true in earlier versions of Mac OS X, but not in more recent versions.


.. class:: varlist

   A C array of unspecified length. Instances of this type cannot be created in Python code.

   This type is used when the API does not specify the amount of items in an array in a way
   that is usable by the bridge.

   .. warning:: 

      Access through a :class:`varlist` object can easily read beyond the end of the
      wrapped C array.  Read the Apple documentation for APIs that return a varlist to
      determine how many elements you can safely access.

   .. method:: as_tuple(count)

      Returns a tuple containing the first *count* elements of the array.

   .. method:: __getitem__(index)
    
      Returns the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices.

   .. method:: __setitem__(index, value)

      Sets the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices (but assigning to a slice is only possible when
      that does not resize the array).


.. class:: function

   Instances of this class represent global functions from Cocoa frameworks. These
   objects are created using :func:`loadBundleFunctions` and :func:`loadFunctionList`.

   .. data:: __doc__

      Read-only property with the documentation string for the function.

   .. data:: __name__

      Read-only property with the name of the function

   .. data:: __module__

      Read-write property with the module that defined the function

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector. 

      .. todo:: insert link to metadata description


.. class:: IMP

   This class is used to represent the actual implementation of an Objective-C
   method (basicly a C function). Instances behave the same as unbound methods:
   you can call them but need to specify the "self" argument.

   .. data:: isAlloc

      Read-only attribute that specifies if the IMP is an allocator (that is,
      the implementation of "+alloc" or one of its variant)

   .. data:: isClassMethod

      Read-only attribute that specified if the IMP is for a class method.

   .. data:: signature

      Read-only attribute with the type encoding for the IMP.

   .. data:: selector

      Read-only attribute with the selector for the method that this IMP
      is associated with.

   .. data:: __name__

      Alias for :data:`selector`.

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector. 

      .. todo:: insert link to metadata description


.. class:: super

   This is a subclass of :class:`super <__builtin__.super>` that works
   properly for Objective-C classes as well as regular Python classes.

   .. note:: 
   
      The statement :samp:`from {Framework} import \*` will replace the 
      built-in :class:`super <__builtin__.super>` by this class.

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

   The value of :c:data:`MAC_OS_X_VERSION_MAX_ALLOWED` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_MIN_REQUIRED

   The value of :c:data:`MAC_OS_X_VERSION_MIN_REQUIRED` when PyObjC was
   compiled.

.. data:: MAC_OS_X_VERSION_10_N

   There are currently 6 constants of this form, for ``N`` from 1 to 6,
   and these have the same value as the Objective-C constant of the same
   name.
 
.. data:: platform

   This always has the value "MACOSX".



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
:const:`_C_ID`           :c:type:`id` (an Objective-C instance)
------------------------ ------------------------------------------------- 
:const:`_C_CLASS`        an Objective-C class
------------------------ -------------------------------------------------
:const:`_C_SEL`          a method selector
------------------------ -------------------------------------------------
:const:`_C_CHR`          :c:type:`char`
------------------------ -------------------------------------------------
:const:`_C_UCHR`         :c:type:`unsigned char`
------------------------ -------------------------------------------------
:const:`_C_SHT`          :c:type:`short`
------------------------ -------------------------------------------------
:const:`_C_USHT`         :c:type:`unsigned short`
------------------------ -------------------------------------------------
:const:`_C_BOOL`         :c:type:`bool`  (or :c:type:`_Bool`)
------------------------ -------------------------------------------------
:const:`_C_INT`          :c:type:`int`
------------------------ -------------------------------------------------
:const:`_C_UINT`         :c:type:`unsigned int`
------------------------ -------------------------------------------------
:const:`_C_LNG`          :c:type:`long`
------------------------ -------------------------------------------------
:const:`_C_ULNG`         :c:type:`unsigned long`
------------------------ -------------------------------------------------
:const:`_C_LNG_LNG`      :c:type:`long long`
------------------------ -------------------------------------------------
:const:`_C_ULNG_LNG`     :c:type:`unsigned long long`
------------------------ -------------------------------------------------
:const:`_C_FLT`          :c:type:`float`
------------------------ -------------------------------------------------
:const:`_C_DBL`          :c:type:`double`
------------------------ -------------------------------------------------
:const:`_C_VOID`         :c:type:`void`
------------------------ -------------------------------------------------
:const:`_C_UNDEF`        "other" (such a function)
------------------------ -------------------------------------------------
:const:`_C_CHARPTR`      C string (:c:type:`char*`)
------------------------ -------------------------------------------------
:const:`_C_NSBOOL`       :c:type:`BOOL`
------------------------ -------------------------------------------------
:const:`_C_UNICHAR`      :c:type:`UniChar`
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_TEXT` :c:type:`char` when uses as text or a byte array
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_INT`  :c:type:`int8_t` (or :c:type:`char` when 
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
  :c:type:`const char*` is represented as :const:`_C_CONST` + :const:`_C_CHARPTR`.

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
  :const:`_C_CFTYPEID`    :c:type:`CFTypeID`
  ----------------------- ------------------------------
  :const:`_C_NSInteger`   :c:type:`NSInteger`
  ----------------------- ------------------------------
  :const:`_C_NSUInteger`  :c:type:`NSUInteger`
  ----------------------- ------------------------------
  :const:`_C_CFIndex`     :c:type:`CFIndex`
  ----------------------- ------------------------------
  :const:`_C_CGFloat`     :c:type:`CGFloat`
  ----------------------- ------------------------------
  :const:`_sockaddr_type` :c:type:`struct sockaddr`
  ======================= ==============================


Context pointers
----------------

A number of Objective-C APIs have one argument that is a context pointer,
which is a :c:type:`void*`. In Objective-C your can pass a pointer to an
arbitrary value, in Python this must be an integer.

PyObjC provides a :data:`context` object that can be used to allocate
unique integers and map those to objects.

.. function:: context.register(value)

   Add a value to the context registry.

   :param value: An arbitrary object
   :return: A unique integer that's suitable to be used as a context pointer
            (the handle).

.. function:: context.unregister(value):

   Remove an object from the context registery, this object must be have
   been added to the registry before.

   :param value: An object in the context registry

.. function:: context.get(handle)

   Retrieve an object from the registry given the return value from
   :func:`context.register`.


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

   .. note::

      The IBOutlet function is recognized by Interface Builder when it
      reads Python code.

.. function:: IBAction(function)

   Mark an method as an action for use in Interface Builder.  Raises
   :exc:`TypeError` when the argument is not a function.
   
   Usage:

   .. code-block:: python

      class SomeObject (NSObject):

         @IBAction
         def saveDocument_(self, sender):
             pass

   .. note::

      The IBOutlet decorator is recognized by Interface Builder when it
      reads Python code. Beyond that the decoerator has no effect.

.. function:: instancemethod

   Explicitly mark a method as an instance method. Use this when
   PyObjC incorrectly deduced that a method should be a class method.

   Usage:

   .. code-block:: python

        class SomeObject (NSObject):

           @instancemethod
           def alloc(self): 
               pass

   .. note::

      There is no function named *objc.classmethod*, use 
      :func:`classmethod <__builtin__.classmethod>` to explictly mark a function
      as a class method.


.. function:: accessor

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The conventions for accessor names that can be used with Key-Value Coding
   is described in the `Apple documentation for Key-Value Coding`_

   The table below describes the convention for methods for a property named '<property>',
   with a short description and notes. The `Apple documentation for Key-Value Coding`_ 
   contains more information.

   ============================================== =================================== =========================================
   Name                                           Description                         Notes
   ============================================== =================================== =========================================
   <property>                                     Getter for a basic property. 
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   is<Property>                                   Likewise, for a boolean             PyObjC won't automaticly set the
                                                  property.                           correct property type, use
                                                                                      :func:`typeAccessor` instead of
                                                                                      :func:`accessor`.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   set<Property>_                                 Setter for a basic property
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   countOf<Property>                              Returns the number of
                                                  items in a indexed 
                                                  property, or unordered
                                                  property
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   objectIn<Property>AtIndex\_                    Returns the object at a specific 
                                                  index for an indexed property
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   <property>AtIndexes\_                          Returns an array of                 Don't use this with
                                                  object values at specific           :func:`typedAccessor`.
                                                  indexes for an indexed    
                                                  property. The argument    
                                                  is an :c:type`NSIndexSet`.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   get<Property>_range_                           Optimized accessor                  Not supported by PyObjC, don't use
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   insertObject_in<Property>AtIndex\_             Add an object to an indexed 
                                                  property at a specific index.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   insert<Property>_atIndexes_                    Insert the values from a list of    Don't use this with 
                                                  at specific indices. The            :func:`typedAccessor`.
                                                  arguments are an :c:type:`NSArray` 
                                                  and an :c:type:`NSIndexSet`.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   removeObjectFrom<Property>AtIndex\_            Remove the value
                                                  at a specific index of an
                                                  indexed property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   remove<Property>AtIndexes\_                    Remove the values at specific
                                                  indices of an indexed property. The 
                                                  argument is an :c:type`NSIndexSet`.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   replaceObjectIn<Property>AtIndex_withObject\_  Replace the value at a specific
                                                  index of an indexed property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   replace<Property>AtIndexes_with<Property>_     Replace the values at specific      Don't use with :func:`typedAccessor`
                                                  indices of an indexed property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   enumeratorOf<Property>                         Returns an :c:type:`NSEnumerator`
                                                  for an unordered property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   memberOf<Property>_                            Returns True if the value is
                                                  a member of an unordered property
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   add<Property>Object\_                          Insert a specific object in
                                                  an unordered property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   add<Property>_                                 Add a set of new values
                                                  to an unordered property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   remove<Property>Object\_                       Remove an object
                                                  from an unordered property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   remove<Property>_                              Remove a set of objects
                                                  from an unordered property.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   intersect<Property>_                           Remove all objects from
                                                  an unorderd property that
                                                  are not in the set argument.
   ---------------------------------------------- ----------------------------------- -----------------------------------------
   validate<Property>_error_                      Validate the new value of a         For typed accessor's the value 
                                                  property                            is wrapped in an :c:type:`NSValue`
                                                                                      (but numbers and booleans are automaticly 
                                                                                      unwrapped by the bridge)
   ============================================== =================================== =========================================

   PyObjC provides another mechanism for defining properties: :class:`object_property`.

   .. versionchanged:: 2.5
      Added support for unordered properties. Also fixed some issues for 64-bit
      builds.

.. _`Apple documentation for Key-Value Coding`: http://developer.apple.com/library/ios/#documentation/cocoa/conceptual/KeyValueCoding/Articles/AccessorConventions.html

.. function:: typedAccessor(valueType)

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The *valueType* is the encoded string for a single value.

   .. note:: 

      When you use a typed accessor you must also implement "setNilValueForKey\_",
      as described in the `Apple documentation for Key-Value Coding`_

.. function:: typedSelector(signature)

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

.. function:: callbackFor(callable[, argIndex=])

   Use this decorator to tell that this function is the callback for
   an (Objective-C) API that stores a reference to the callback
   function.

   You only *have* to use this API when the Objective-C API can store
   the callback function for later usage. For other functions the
   bridge can create a temporary callback stub.

   Using this decorator for methods is not supported

   Usage:

   .. code-block:: python

       @objc.callbackFor(NSArray.sortedArrayUsingFunction_context\_)
       def compare(left, right, context):
           return 1

   This tells the bridge that 'compare' is used as the sort function
   for NSArray, and ensures that the function will get the correct
   Objective-C signature.

   .. note::

      The example will also work without the decorator because 
      NSArray won't store a reference to the compare function that
      is used after 'sortedArrayUsingFunction_context\_' returns.

.. function:: selectorFor(callable[, argIndex])

   Decorator to tell that this is the "callback" selector for another 
   API.

   Usage:

   .. code-block:: python

      @objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_) 
      def sheetDidEnd_returnCode_contextInfo_(self, sheet, returnCode, info): 
          pass 
      
   This will tell the bridge that this method is used as the end method
   for a sheet API, and will ensure that the method is registered with
   the correct Objective-C signature.


.. function:: synthesize(name[, copy[, readwrite[, type[, ivarName]]]])

   :param name:  name of the property
   :param copy:  if false (default) values are stored as is, otherwise
                 new values are copied.
   :param readwrite: If true (default) the property is read-write
   :param type:  an encoded type for the property, defaults to 
                 :data:`_C_ID`.
   :param iVarName: Name of the instance variable used to store
                    the value. Default to the name of the property
                    prefixed by and underscore.

   This synthensizes a getter, and if necessary, setter method with
   the correct signature. The getter and setter provide access to
   an instance variable.

   This can be used when specific semantics are required (such as
   copying values before storing them).

   The class :class:`object_property` provides simular features with
   a nicer python interface: with that calss the property behaves
   itself like a property for python code, with this function you
   still have to call accessor methods in your code.

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
the :mod:`pickle` module in Python and the :c:type:`NSCoding` protocol in Objective-C.

It is possible to use an :c:type:`NSKeyedArchiver` to store any Python object that
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
   :param dynamic: If this argument is :data:`True` the property will not generate default accessor, 
     but will rely on some external process to create them.
   :param ivar: Name of the instance variable that's used to store the value. When this value is :data:`None`
     the name will be calculated from the property name. If it is :data:`NULL` there will be no instance variable.
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
   you will get an object that implements the :class:`MutableSequence` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: set_property

   This property implements a set-like property. When you access the property
   you will get an object that implements the :class:`MutableSet` ABC, and
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
