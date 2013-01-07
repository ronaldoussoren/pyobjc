Manual metadata loading
=======================

.. py:currentmodule:: objc

Introduction
------------

When the other two metadata systems aren't suitable it
is also possible to load metadata through code. The other
two systems use the functionality described in this section
to actually load the metadata.

.. seealso::

   :doc:`bridgesupport`
     Loading metadata from XML files

   :doc:`compiled`
     Loading metadata using compiled files


Metadata dictionaries
---------------------

One or the arguments for :func:`loadBundleFunctions`, :func:`loadFunctionList` and :func:`registerMetaDataForSelector`
contains (or "is" for :func:`registerMetaDataForSelector`) a metadata dictionary containing information about function 
and method interfaces that cannot be extract from a basic type signature for that function or method.

Copies of these structures can be also retrieved at runtime using the *__metadata__()* method on both :class:`function` 
and :class:`selector` objects, which makes it possible to introspect the metadata information when needed.

The metadata is a Python dictionary with a particular structure (all keys are optional):

* *arguments*: A dictionary containing more information on arguments. The keys of this dictionary are integers
  with the argument offset (for methods index 0 is the first implicit argument, index 2 is the first argument that is
  visible in a prototype). The values are metadata dictionaries for the arguments and are decribed 
  :ref:`later on <manual-metadata-argument-metadata>`.

  In metadata that is returned the *__metadata__()* method of :class:`function` and :class:`selector` objects the
  *arguments* value is a tuple with items for all arguments.


* *retval*: A metadata dictionary with more information on the return value. The contents of this dictionary
  is described :ref:`later on <manual-metadata-argument-metadata>`.

* *suggestion*: For methods only: the method should not be called from Python, and calling it will raise and exception
  with the *suggestion* value in the exception message.

* *variadic*: If present and the value is :data:`True` the function or method takes a variable number of arguments. PyObjC
  can only call such functions when either on of the arguments is a *printf_format*, or the dictionary contains information
  on the argument array (as described by keys further on in this list).

* *c_array_delimited_by_null*: If present and the value is :data:`True`, and the function is a variadic function, the
  variable part of the function argument list is a list of values where the last item of the list is a null value. All elements
  of the list are the same type, that of the last type that is present in the prototype. 

  In python the function is called with the additional arguments after the fixed arguments (just like in C), but without
  a null value at the end of the argument array.
  
  An example of such a function is `execlp(3) <http://www.manpages.info/macosx/execl.3.html>`_

* *c_array_length_in_arg*: If present and the value is an integer, and the function is a variadic function, the 
  variable part of the function argument list is a list of values and the value for this key indicates which function
  argument contains the length of that list. All elements of the list are the same type, that of the last type that 
  is present in the prototype.

  In python the function is called with the additional arguments after the fixed arguments (just like in C).

Keys not listed above will be ignored by the bridge.

.. note::
   
   The bridge currently does not copy the metadata when you register it with the functions listed above. Don't rely
   on that behavior, it might change in a future release and changes to metadata dictionaries may or may not affect
   bridge behavior (basicly depending on if the change occurs before or after the bridge first uses the metadata)

*c_array_lenght_in...* interpretation
.....................................

The keys *c_array_length_in_arg* (function, argument and return value metadata) and *c_array_length_in_result* (argument
metadata) describe the index of an argument that contains the size of a C array. This section describes how the bridge
determines the value to use for the array.

For :data:`_C_INOUT` argument the value to use for converting to C and back from C is calculated both before and
after the function call, which means that the length of the array passed to the function can have a different length
than the array returned from the function.  This is used for function where a buffer is passed into the function and
the function indicates the useable size of that buffer by modifiying a pass-by-reference argument.

How the size of the C array is calculated depends on the *type* of the argument:

* When the type is a pointer type the value is calculated by dereferencing the pointer.

* When the type is a integer (for example, :c:type:`int`, :c:type:`unsigned long` or :c:type:`NSInteger`) the length
  is the value of the C argument.

* When the type is :c:type:`NSRange` or :c:type:`CFRange` the length of the C array is the lenght of the range.

* When the type is :c:type:`id` and the Objective-C instance responds to the "-count" selector the length
  of the C array is the result of calling that selector.
 
* In all other cases the length cannot be calculated and the bridge raises an exception.

  .. _manual-metadata-argument-metadata:

Argument and return value metadata
..................................

The argument and return value metadata is also a dictionary with a specific structure. As with the complete metadata
dictionary all keys are optional unless the description mentions otherwise.

* *type*: A byte string with the type encoding for the value. The default is extracted from the type encoding for
  the entire prototype (for methods this is extracted from the Objective-C runtime, for functions this is passed as
  one of the items in the function info tuple).

  This key is always present in the metadata returned by the *__metadata__()* method.

* *type_override*: A byte string with value :data:`_C_IN`, :data:`_C_OUT` or :data:`_C_INOUT` to indicate that the 
  argument is an input, output or input/output argument. Ignored unless the *type* is a pointer type that isn't a
  CoreFoundation instance.

  The value is assumed to be a single value (a pass-by-reference argument), unless there are keys in the dictionary that
  say otherwise (see further on in this list).

  This key is not used for return value metadata.

* *printf_format*: If present and the value is :data:`True` the argument value is a printf(3) style format string for
  a variadic function or method. Ignored unless the function or method actually is variadic.

* *sel_of_type*: A byte string that describes the expected selector prototype for arguments of the :data:`_C_SEL`. 

  Used by the decorator :func:`selectorFor` to calculate the signature of the decorated method.

* *already_retained*: Value :data:`True` indicates that the return value, or a pass-by-reference output parameter, is 
  returned to the caller with an increased reference count. An Objective-C caller will have to call "-retain" on the value 
  when the value is no longer used.

  Used by the bridge to correctly maintain the Objective-C reference count. Python users do not have to maintain the
  reference count themselfes.

* *already_cfretained*: Value :data:`True` indicates that the return value, or a pass-by-reference output parameter, is 
  returned to the caller with an increased reference count. An Objective-C caller will have to call "CFRelease" on the value 
  when the value is no longer used.

  Used by the bridge to correctly maintain the Objective-C reference count. Python users do not have to maintain the
  reference count themselfes.

  .. note:: 

     Use either *already_retained*, or *already_cfretained* but not both. 

     The two different keys are present to be able to support Objective-C Garbage Collection: in process with GC enabled
     the CoreFoundation and Cocoa retain count APIs behave differently. Because GC is on the way out and PyObjC doesn't
     properly support GC anyway it is better to use *already_retained* where approprate and not use *already_cfretained*.


* *c_array_delimited_by_null*: When :data:`True`, and the argument or return value *type* is a pointer type, the value 
  is a C array with a null value at the end. Python users do not have to supply the null value on calls, and the bridge 
  will strip the null value in return values.

  When the *type_override* is :data:`_C_IN` or :data:`_C_INOUT` the input value must be a sequence of values (list, tuple,
  ...). The bridge allocates a buffer of the right size, converts all values and appends the approprate null value. The
  value can also be a buffer (such as an :class:`array.array` of the approprate structure), which then must contain a null
  value at the end.

  When the *type_override* is :data:`_C_OUT` the argument must be either :data:`NULL` to indicate that a :c:data:`NULL`
  pointer should be passed to the Objective-C function or a buffer object of the appropriate structure, and with enough
  room to store the function output including the null delimiter.

* *c_array_length_in_arg*: The argument or return value is a C array where the length of the array is specified in 
  another argument. Ignored when the *type* is not a pointer type. The value for this key is either a single integer, or
  two integers (for :data:`_C_INOUT` arguments).

  When the *type_override* is :data:`_C_IN` or :data:`_C_INOUT` the input value must be a sequence of values of the correct
  lenght (at least the length that's expected by the function, additional items in the sequence are ignored).

  When the *type_override* is :data:`_C_OUT` the value can be :data:`NULL` (:c:data:`NULL` pointer passed to the function) or
  :data:`None` (PyObjC allocates a C array of the right size and writes nul bytes in the entire buffer).

  When the value of the key is a single integer this argument index for the argument that contains the expected size
  of the array. When the value of the key is a tuple of two integers these are the indexes for the argument that contains
  the size that should be used when calling the function and the argument that contains the size of the array that is useable
  after the call.

* *c_array_of_fixed_length*: When the *type* is a pointer type the actual argument (or result) is an C array of a fixed length. The value
  for this key is an integer that is the length of the C array.

* *c_array_of_variable_length*: When the *type* is a pointer type the actual argument (or result) is a C array, but the
  lenght of the array is unknown or cannot be described in metadata.

  For results the bridge will return a value of :class:`varlist`.

  For arguments with *type_override* value :data:`_C_IN` or :data:`_C_INOUT` the value for the arugment must be a Python sequence 
  and the bridge will allocate a C array that is long enough to contain all items of that sequence; alternatively the argument
  can be a Python buffer object (simular to :data:`_C_OUT` arugments).  For :data:`_C_OUT` arguments the value for the argument 
  must be either :data:`NULL` or a Python buffer object that will be passed to the function. 

* *c_array_length_in_result*: Only valid for argument metadata. When the argument *type* is a pointer type and the 
  *type_override* is :data:`_C_INOUT` or :data:`_C_OUT` the usuable length of the array is calculated from the return value.

  The size of the buffer that needs to be allocated is determined using one of the other *c_array...* keys in the metadata
  dictionary.

* *null_accepted*: If :data:`True` and the argument is a pointer it is safe to pass a :data:`NULL` as the value. 
  Defaults to :data:`True`.

  This key is not used in return value metadata.

  .. note:: 
     The metadata that is currently shipped with PyObjC does not contain *null_accepted* data. This means that the bridge
     won't check if it safe to pass :data:`NULL` as a value for pointer arguments, read the Cocoa documentation to check
     if passing :data:`NULL` is safe.

* *callable*: When type argument or return value has type "^?" or "@?" the method or function takes a function or block
  as the argument. In Python an arbitrary callable can be passed (but see *callable_retained* for some limitations).

  The value of this attribute contains the metadata describing the callable. It is a metadata structure as described in
  this section, with some additional limitations: the *arguments* key of the dictionary must describe all arguments of the
  callable (that is all keys in range(len(*arguments*)) must be present), the *type* key of the argument and return value
  metadata must be present (although it is allowed to leave out the return value metadata when the function has return
  type :c:type:`void`).

  For blocks the argument array *must* include the first implicit argument at index 0 or the *arguments* array, and with
  type b"^v".

* *callable_retained*: Then :data:`True` and *callable* is present and the argument type is b"^?" the callable argument
  will be retained by the Objective-C funtion or method beyond the call.

  This key is not used in return value metadata.

  When this value is :data:`True` the argument must be a global object that is annotated with the decorator
  :func:`callbackFor`. That decorator ensures that the C representation of the function is always present to ensure that
  it is safe to store a reference on the Objective-C side of the bridge. 

API description
---------------

Loading frameworks and other bundles
....................................

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

Creating and registering types
..............................
   
.. function:: registerCFSignature(name, encoding, typeId[, tollfreeName])

   Register a CoreFoundation based type with the bridge. If *tollfreeName* is specified
   the type is tollfree bridged to that Objective-C class. 

   The value of *typeId* is :data:`None` for tollfree bridged types, and the result
   of the "GetTypeID" function for the type for other types.

   Returns the class object for the registerd type.

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


Loading variable/constants
..........................

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


Loading functions
.................

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

   The structure of the metadata dictionary is descripted in the section `Metadata dictionaries`_.


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


Metadata for Objective-C methods and classes
............................................

.. function:: registerMetaDataForSelector(class\_, selector, metadata)

   Register a metadata structure for the given selector. The metadata is a dictionary,
   and the structure of that dictionary is described in the section `Metadata dictionaries`_.


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
      to initialize classes that will require us to remove this function.


.. function:: addConvenienceForClass(classname, method)

    Add a list of method the named class when that class is initialized, the class
    need not be loaded at the time of this call. These additional methods are not
    added to the Objective-C class, but are only visibile in Python code.

    The *methods* argument is a list of tuples (methodname, function).


.. function:: setSignatureForSelector(class_name, selector, signature)

   .. deprecated:: 2.3

   Use the metadata system instead

   Register a replacement signature for a specific selector. This can
   be used to provide a more exact signature for a method.


