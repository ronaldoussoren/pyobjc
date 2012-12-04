BridgeSupport XML files
=======================

.. py:currentmodule:: objc


Introduction
------------

PyObjC 2.0 introduced a way to load enhanced API descriptions 
from XML "bridgesupport" files. The format of this file is shared
between a number of bridges, although later releases of PyObjC added
more capabilities that aren't in the official format.

As of PyObjC 2.4 [1]_ use of bridgesupport files is deprecated, the 
:doc:`compiled metadata system <compiled>` allows for faster and lazy loading.

Basic structure and use
-----------------------

Bridgesupport files are XML files with a root element "signatures" 
that has child elements for various kind of API descriptions. The API
descriptions contain information that cannot be extracted at runtime,
such as the names and types of global variables (constants), enum labels,
function prototypes and additional information about method signatures.

PyObjC supports loading bridgesupport files when initializing a module
using :func:`initFrameworkWrapper`, as well as parsing the contents of
bridgesupport files using :func:`parseBridgeSupport`.

The function :func:`initFrameworkWrapper` is basicly a one-step 
solution for wrapping a framework: it loads the framework bundle
and bridgesupport file and then initializes the contents of the wrapper
module.   Bridgesupport files are located using a search path:

 1. "PyObjC.brigesupport" next to the module calling
    :func:`initFrameworkWrapper`. 

 2. A resource file inside the framework itself (with suffix
    ".bridgesupport" and the same basename as the framework,
    located in subdirectory "BridgeSupport").

 3. A resource name with the same basename as the framework
    and suffix ".bridgesupport" in "/System/Library/BridgeSupport"

    .. note::

       PyObjC will not load bridgesupport files from
       "/Library/BridgeSupport" or "~/Library/BridgeSupport"
       to avoid depending on system-specif files that could
       make a bundled PyObjC application non-portable.

When a bridgesupport is loaded from the last two location
the function also looks for "PyObjCOverrides.bridgesupport" next
to the module that called :func:`initFrameworkWrapper`.


Creating a library wrapper
--------------------------

The easiest way to create a framework wrapper using 
bridgesupport files is to use a python package where
the "__init__.py" contains a call of :func:`initFrameworkWrapper`

.. sourcecode:: python

   import objc as _objc

   __bundle__ = _objc.initFrameworkWrapper("FrameworkName",
                        frameworkIdentifier="com.apple.Framework",
                        frameworkPath=_objc.pathForFramework("/System/Library/Frameworks/FrameworkName.framework")
                        globals=globals())

The framework name, identifier and path should be replaced by the
information for the framework you are wrapping.

The :func:`initFrameworkWrapper`  will load bridgesupport files from 
a file named "PyObjC.bridgesupport" next to the "__init__.py" when
such a file exist, and otherwise from the default location in the
framework itself.

.. note::

   The call to :func:`objc.pathForFramework` ensures that the wrapper does the right thing
   when DYLD environment variables are 
   set (see `dyld(1) <http://developer.apple.com/library/mac/#documentation/Darwin/Reference/Manpages/man1/dyld.1.html>`_ for
   more information on those).


Detailed file structure
-----------------------

This section describes the BridgeSupport file as supported by PyObjC. PyObjC supports a slightly different dialect of those files
than what is described in `Apple's manual page for BridgeSupport`_.

The file is an XML document with a toplevel element named "signatures". The standard proscribes an attribute named version, that 
attribute is ignored by PyObjC. A minimal BridgeSupport file is:

.. sourcecode:: xml

   <signature version='1.0'>
   </signatures>

The document root has children that contain the metadata for various types of objects. 

* *<cftype>*:   Describes a Core Foundation type

* *<class>*:    Describes additional information for an Objective-C class, this does not contain
  all information about the class, only those bits that cannot be extracted from the Objective-C runtime.

* *<constant>*: Describes a (constant) external variable
 
* *<enum>*: A numeric constant, used for enum labels and #define's that expand into an integer or
  float literal.

* *<function>*: Describes a C function

* *<function_pointer>*: An alias for a *<function>* node.

* *<informal_protocol>*: Describes the interface of an Objective-C informal protocol (that is, a protocol
  that is only described in documentation and not as a language construct)

* *<null_const>*: Describes a constant value that evaluates to C's NULL pointer

* *<opaque>*: A pointer type that refers to an opaque blob (a "handle").

* *<string_constant>*: Describes a #define that expands into a C or Objective-C string literal

* *<struct>*:   Describes a typedef-ed C structure (for example :c:type:`NSPoint`)


The sections below contain more information about all types, with details about their semantics,
supported child elements and attributes.

The document can contain other elements, attributes, and extra whitespace and those will be ignored by
the bridgesupport parser.

Bridgesupport elements are processed in an undefined order, the side effects of alle elements that have
the same name will take place but it is undefined which definition will be bound to a name in the module
globals dictionary.

.. seealso::

   `BridgeSupport(5)`_ 
     Apple manual page describing the metadata format

Type encodings
..............

A number of elements have a "type" attribute that contains an Objective-C runtime type encoding. Most contain
the type encoding for a single type, the signature for methods in informal protocol contains the type signatures
of the return value and all arguments (included the implicit ones).

The type signatures are described in `Apple's Objective-C Runtime Programming Guide`_, and the format of
the BridgeSupport file uses that format with one small change: the BridgeSupport file can contain some
type encoding that aren't presesnt in Apple's runtime and redefines one type encoding.

  +--------------+---------------------------------------------------------------------------------------+
  | **Typecode** | **Description**                                                                       |
  +==============+=======================================================================================+
  | *B*          | used for type :c:type:`BOOL`, is used for :c:type:`bool` in the Objective-C runtime   |
  +--------------+---------------------------------------------------------------------------------------+
  | *Z*          | used for type :c:type:`bool`                                                          |
  +--------------+---------------------------------------------------------------------------------------+
  | *T*          | used for type :c:type:`UniChar`                                                       |
  +--------------+---------------------------------------------------------------------------------------+
  | *t*          | used for type :c:type:`char` in the role of a single character                        |
  +--------------+---------------------------------------------------------------------------------------+
  | *z*          | used for type :c:type:`char` in the role of a small integer                           |
  +--------------+---------------------------------------------------------------------------------------+

The bridge uses the information provided by these ehnanced type encodings and translates them to regular
type encodings when communicating with the Objective-C runtime (or other Objective-C code).

Boolean attributes
..................

A number of elements that are described below have attributes that are booleans. When the documentation 
says that an attribute is a boolean attribute the value of the attribute is either *true* or *false*:

.. sourcecode:: xml

   <function name='func1' variadic='true' />
   <function name='func1' variadic='false' />

The values *true* and *false* correspond to the Python values :data:`True` and :data:`False` (the obvious
interpretation).

<cftype>
.........

Nodes of this type define a CoreFoundation type, such :c:type:`CFURLRef`. These elements are used to 
define a Python proxy for the CoreFoundation type and to register that type with the bridge. The proxy
type is a subclass of :class:`objc_object`.

.. sourcecode:: xml

   <cftype name='CFURLRef' type='^{CFURLRef}' gettypeid_func='CFURLGetTypeID' />

These elements do not have child elements, all information is encoded in attributes:

 * *name*:           the name of the Objetive-C type (such as :c:type:`CFURLRef`
 * *type*, *type64*: the type encoding for the Objective-C type, *type64* contains the encoding for use 
   in 64-bit mode when that encoding is different from the encoding used in 32-bit mode.
 * *gettypeid_func*: (optional) the name of a C function for retrieving the type ID of the type, the default is derived
   from the name (strip "Ref" from the end of *name*, then add "GetTypeID")
 * *tollfree*:       (optional) the name of an Objective-C class that is tollfree bridged to this type
   For tollfree bridged types the bridge does not create a new proxy type, but reuses the proxy type for the
   Objective-C class. That is, in Python the CoreFoundation and Objective-C interfaces can be used without
   any form of casting.

<class>
.......

Describes additional metadata for Objective-C classes.

.. sourcecode:: xml

   <class name='NSObject'>
     <method selector='description'>
       <retval type='@' />
     </method>
   </class>

The element has a single attribute *name* with the name of the Objective-C class. When that class is not present
in the runtime the metadata is stored for later use (a later class definition or bundle loading action might make
the class known to the runtime later on).

The element has 0 or more children with method definitions, the tag for those children is *<method>* and other
children are ignored.

A *<method>* element has the following attributes:

* *selector*: The selector for this method

* *class_method*: A boolean attribute that indicates if this method is a class method (default: *false*). 

* *variadic*: Boolean attribute that tells if the method has a variable number of
  arguments (default: *false*)

* *c_array_delimited_by_null*: Boolean attribute that tells if a variadic function
  has an argument list that is ended by a null value (default: *false*). 

* *c_array_length_in_arg*: For a variadic function the argument with this index contains
  the number of variadic arguments. 

* *suggestion*: Indicates that this method should not be used from Python code. The value contains
  a message to add to the Python exception that's raised when trying to use the method.

Method's have 0 or more *<arg>* and *<retval>* child elements that describe additional
information about the method prototype (information that cannot be extracted from
the Objective-C runtime).  The structure of *<arg>* and *<retval>* elements is described 
in the section `describing function and method prototypes`_.

<constant>
..........

This element defines a C constant/variable definition. 

.. sourcecode:: xml

    <constant name="NSZeroPoint" type="{_NSPoint=ff}" type64="{_CGPoint=dd}" />

This element does not have children, all information is encoded in attributes.

* *name*: The name of the variable. This name is bound to the proxied value 
  in the globals dictionary.

* *type*, *type64*: The type encoding of the variable. The attribute
  *type64* is used to describe the type encoding for the 64-bit runtime when
  that encoding is different from the encoding for the 32-bit runtime.

* *magic_cookie*: Boolean attribute. When the value is true and the type
  is an Objective-C or CoreFoundation class the value is assumed to be a
  magic cookie that cannot be accessed like a normal object.

The bridge will ignore constants that have a type that is a struct type with
embedded function pointers. 

.. note::

   Due to the way these values are exposed to Python they will behave like constants
   in Python, the Python representation will not change when the value of the C
   variable would change. This means that *<constant>* definitions aren't useful to
   expose variable definitions that aren't effectively constant (such as the 
   :c:data:`NSApp` variable).

<enum>
......

This element defines a numeric constant such as an :c:type:`enum` label or C a macro that expands into an integer or float
literal.

.. sourcecode:: xml

   <enum name='NSCompareEqual' value='0' />

This element does not have children, all information is encoded in attributes.

* *name*: The name of the constant

* *value*, *value64*: The value of the constant. The attribute *value64* contains the value for 64-bit code
  when that value is different from *value*.

* *le_value*, *be_value*: When the *value* and *value64* attributes are not present, these two attributes
  encode the value of the constant for little endian (*le_value*) and big endian (*be_value*) systems.

The value attribute can contain a numeric constant in a number of formats:

* An integer with or without a sign, in the format of a decimal integer C constant without a size 
  suffix (such as 'L'). Examples are *42*, *-32*. These are converted to a Python integral type (:class:`int`
  or :class:`long`).

* A C floating point constant in a decimal representation, without a size suffix. Examples
  are *1.0*, *-1.5e30*. These are converted to a Python floating point type (:class:`float`).

* A C floating point constant in a hexadecimal representation, without a size suffix. An 
  example is *0x1.77p+10*. These are converted to a Python floating point type (:class:`float`).

When the value cannot be parsed the definition is ignored.

<function>
..........

This element defines a global C function.

.. sourcecode:: xml

   <function name="NSCreateObject">
      <retval type="@" />
      <arg type="#" />
   </function>'

Information about the function itself is encoded in attributes of the *<function>* elements,
information about the return value is encoded as the child element *<retval>* and information
about arguments is encoded using *<arg>* elements.

* *name*: The name of the function

* *variadic*: Boolean attribute that tells if the function has a variable number of
  arguments (default: *false*)

* *c_array_delimited_by_null*: Boolean attribute that tells if a variadic function
  has an argument list that is ended by a null value (default: *false*). When the 
  function is variadic and this attribute is true the last *<arg>* child contains information
  about all variadic arguments (that is, there can be 0 or more instances of the 
  argument described by that node present in the actual argument list).

* *c_array_length_in_arg*: For a variadic function the argument with this index contains
  the number of variadic arguments. The last *<arg>* child contains the type information
  for those arguments.

The structure of *<arg>* and *<retval>* elements is described in the section
`describing function and method prototypes`_.

.. note::
   
   Variadic functions are only supported when the bridge has enough information to
   construct a valid argument list using one of the arguments described above or a
   *printf_format* attribute on one of the *<arg>* children.


<function_pointer>
..................

This element is intended to be used to define function aliases, that is an alternative name for a *<function>* element. 
Due to the way PyObjC is implemented the element can also be used to define an alias for other elements (for example
*<enum>* or *<constant>* elements).

.. sourcecode:: xml

   <function_pointer name='AlternateName' original='BasicName' />

This element does not have children, all information is encoded in attributes.

* *name*: the name that will be added to the globals dictionary

* *orginal*: the name from the globals dictionary that will be aliased. When
  this object does not exist the *<function_pointer>* element will be ignored.


<informal_protocol>
...................

This element is used to describe an Objective-C informal protocol, that is a set of methods expected by an API that are described
in the documentation but are not a formal ``@protocol`` definition. The information in informal protocol definitions are
used by the bridge to automaticly adjust the method signatures of method that are defined in Python.

.. sourcecode:: xml

   <informal_protocol name="NSTableViewDataSource">
      <method selector="numberOfRowsInTableView:" type="i@:@" type64="q@:@" />
   </informal_protocol>

The *<informal_protocol>* element has a single attribute, *name*, with the name of the protocol. Child elements with tag
*<method>* contain more information about methods in the protocol. Other child elements are ignored.

All information for *<method>* elements is provided through attributes, the element does not have child elements (and does
not contain the same kind of information as *<method>* elements in *<class>* definitions.

The following attributes can be used for *<method>* elements:

* *selector*: The selector for the method

* *type*, *type64*: The Objective-C type encoding of the method prototype: the return value followed by all arguments
  (including the two implicit arguments).

.. deprecated 2.5
   The bridgesupport system creates a namespace "protocols" in the module globals with all formal and informal protocols. Use
   of this namespace is deprecated. You can use :func:`protocolNamed` to access formal protocols, and shouldn't require
   access to informal protocol objects.

.. note::
   The *<method>* elelments in an informal protocol cannot be used to describe complicated method signatures, such
   as variadic methods or pointer arguments that refer to arrays. This can be worked around by describing such methods
   using *<method>* notes of a *<class>* definition for class :c:data:`NSObject` as well.


<null_const>
............

This element defines a name that expands into a C :c:data:`NULL` pointer, and that is
represented as :data:`None` in Python.

.. sourcecode:: xml

   <null_const name='nil' />

This element does not have children, all information is encoded in attributes.

* *name*: The name of a :c:data:`NULL` constant. This name will be bound
  to :data:`None` in the globals dictionary.

<opaque>
........

This element describes pointer types that are used as handles.

.. sourcecode:: xml

   <opaque name='NSOpaqueType' type='^{opaque}' />

These elements do not have child elements, all information is encoded in attributes:

* *name*: The name of the type

* *type*, *type64*: The Objective-C type encoding of the pointer type. The *type64* attribute can be used
    to describe the type for the 64-bit runtime when that type is different from the type for the 32-bit runtime.


<string_constant>
.................

This element describes C constants that are string literals, for example C macros.

.. sourcecode:: xml

     <string_constant name="NSLabel"  value="label text" />

These elements do not have child elements, all information is encoded in attributes:

* *name*: Name of the constant

* *value*, *value64*: The value of the constant. The attribute *value64* can be used when the 
  value for the 64-bit runtime is different from the value for the 32-bit runtime.

* *nsstring*: Boolean attribute, defaults to :data:`False`. When this value is :data:`True`
  the Python representation is a unicode string (:class:`unicode`), otherwise the Python 
  representation is a byte string (:class:`bytes`).


<struct>
........

This element describes a C structure type and is used to create a Python type with
a simular interface (see :func:`createStructType`).

.. sourcecode:: xml

   <struct name='NSPoint' type='{_NSPoint="x"f"y"f}' type64='{_CGPoint="x"d"y"d}' />

These elements do not have child elements, all information is encoded in attributes:

* *name*: The name of the structure type, this is usually the typedef name in C

* *type*, *type64*: The Objective-C type encoding of the type. Use *type64* when the
  encoding for the 64-bit runtime is different from the encoding for the 32-bit runtime.

  The encoding should be for a structure type and must include embedded field names,
  when the field names are not present the definition is ignored. A structure type
  contains embedded field names with the encoding contains a (double-)quoted field 
  name just before the type encoding of that field. In the example above the field
  names are *x* and *y*.

* *alias*: Name of a Python type that should be used for the Python representation
  of this structure. That type should be created using :func:`createStructType` 
  (or a *<struct>* element in a bridgesupport file). The value of the attribute is
  a fully qualified name.

  One example for using this is to map the Objective-C types :c:type:`NSPoint` and
  :c:type:`CGPoint` to the same Python type. 


Describing function and method prototypes
.........................................

The elements *<function>* and *<method>* (in *<class>* definitions) can have child elements that are used
to describe the full prototype (for functions) or additional information about the prototype (for methods).

For functions the *<arg>* children contain information about all arguments, in order (and without using the
attribute *index* described below). The *<retval>* child element can contain information about the function
return value, when that element is not present the function has return type :c:type:`void`.

For methods the *<arg>* children can contain more information about some arguments, these children have
an *index* attribute that tells which argument is described. Likewise the *<retval>* element can optionally
provide more information about the return value of a method.

It is undefined which *<retval>* element is used when more then one of them is present, and the bridge may
also ignore definitions with multiple *<retval>* elements.

The following attributes can be used with *<arg>* and *<retval>* elements:

* *index*: For *<arg>* children of *<method>* elements only. Contains the argument index, where index 0 is
  the first explicit method argument (that is, the two implicit arguments cannot not present in the 
  bridgesupport file).

* *type*, *type64*: Type of the argument or return value. Required for children of *<function>*, and optional for children
  of *<method>* (the default type is extracted from the Objective-C runtime). The *type64* attribute can be used
  to describe the type for the 64-bit runtime when that type is different from the type for the 32-bit runtime.

* *type_modifier*: A modifier for pointer arguments. Use value 'n' to specify that a value is passed into the function,
  'o' to specify that a value is passed out of the function and 'N' to specify that a value is passed both ways.

  When none of the *c_array_...* attributes are used the argument is a pass-by-reference argument (single value), otherwise
  the argument is a buffer (C array).

* *already_cfretained*: Boolean attribute (default :data:`False`). When :data:`True`, the return value, or pass-by-reference 
  output parameter, is an object that is returned with an increased retain count (that is, the Objective-C caller must call 
  :c:func:`CFRelease` when it no longer needs to access the value).

* *already_retained*: Boolean attribute (default :data:`False`). When :data:`True`, the return value, or pass-by-reference 
  output parameter, is an object that is returned with an increased retain count (that is, the Objective-C caller must call 
  the retain method when it no longer needs to access the value).

  Metadata where both *already_retained* and *already_cfretained* are true is invalid and will be ignored.

* *c_array_length_in_result*: Boolean attribute (default :data:`False`). When true the *<arg>* is a pointer argument that 
  points to a buffer of values where the number of values is in the return value of the function or method. This is commonly
  used with output parameters (see *type_modifier*), and with an argument that is used to specify the size of the buffer that
  needs to be allocated before calling the function or method.

* *c_array_delimited_by_null*: Boolean attribute (default :data:`False`). When true the value is a pointer to a null-terminated
  buffer of values.

* *c_array_of_variable_length*: Boolean attribute (default :data:`False`). When true the value is a pointer to a buffer where
  the bridge has no information about the expected size. For arguments the bridge assumes that the size of the sequence that
  the caller passes is sufficient (for input parameters), for return values the bridge creates a special sequence type that doesn't
  limit the indexes you can use.

* *printf_format*: Boolean attribute (default :data:`False`). When true the argument is a printf-style format string, used when
  the function or method is a variadic callable to convert the additional arguments.

* *function_pointer*: Boolean attribute (default :data:`False`). When true the argument is a function pointer, the function interface
  is described by child elements of this element.

* *block*: Boolean attribute (default :data:`False`). When true the argument is a block, the block interface
  is described by child elements of this element.

* *function_pointer_retained*: Boolean attribute (default :data:`False`). When true and either *function_pointer* or *block* is true,
  the function pointer argument will be stored by the called function. The bridge cannot create a temporary C bridge for the 
  function that's cleaned up after the call.

* *free_result*: The return value in C is a buffer that should be freed using the function :c:func:`free`.

* *sel_of_type*, *sel_of_type64*: Used when the argument has type :c:type:`SEL`: the value of the attribute describes the type
  signature of a selector. This data is used by the decorator :func:`selectorFor` to adjust the method signature of a newly
  defined python method.

* *c_array_of_fixed_length*: The argument or return value is a C array of a fixed length. The attribute value is the (integer)
  value of that length.

* *c_array_length_in_arg*: The argument or return value is an array whose length is passed in another argument. The value is the
  index of that argument (for methods index 0 is the first explicit argument). For *<arg>* nodes the value can also be two integers
  separated by a comma, in those cases the first value is the argument that contains the array length that should be passed to the
  function while the second value the argument that contains the usuable length of the array when the function returns.

.. _`BridgeSupport(5)`: http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`

.. _`Apple's manual page for BridgeSupport`: http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`


API description
---------------

.. function:: parseBridgeSupport(xmldata, globals, frameworkName[, dylib_path[, inlineTab]])

   :param xmldata: A string with the bridgesupport XML document
   :param globals:  Globals dictionary for the wrapper module, usually 
                    the result of :func:`globals <__builtins__.globals>`.
   :param frameworkName: Name of the framework, it is assumed that the Python
                         module for the wrapper has the same name.
   :param dylib_path: (Optional) filesystem path for a shared library with
                      additional function definitions. Used by the system
                      bridgesupport files to provide access to inline 
                      functions.
   :param inlineTab: (Optional) A capsule object with function pointers,
                     see :func:`loadFunctionList` for more information on
                     this parameter.

   Load a `BridgeSupport XML file <http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`_
   with metadata for a framework.

   The definitions from the framework will be added to the *globals* dictionary.
                  
   .. note::

      This function is primarily present for backward compatibility and for users that need an easy way to wrap their own Objective-C code.
      PyObjC itself uses a different metadata mechanism that's better tuned to the needs of PyObjC.

   .. versionchanged:: 2.4
      This function is not present.

   .. versionchanged:: 2.5
      The function is available again.



.. function:: initFrameworkWrapper(frameworkName, frameworkPath, frameworkIdentifier, globals[, inlineTab [, scan_classes[, frameworkResourceName]]])

   :param frameworkName: Name of the framework, it is assumed that the Python
                         module for the wrapper has the same name.
   :param frameworkPath: Filesystem path for the framework bundle
   :param frameworkIdentifier: Bundle identifier for the framework
   :param globals:  Globals dictionary for the wrapper module, usually 
                    the result of :func:`globals <__builtins__.globals>`.
   :param inlineTab: (Optional) A capsule object with function pointers,
                     see :func:`loadFunctionList` for more information on
                     this parameter.
   :param scan_classes: (Optional) If this option is :data:`True` (the default)
                     all Objective-C classes in the runtime are added to
                     *globals*.
   :param frameworkResourceName: (Optional) the first argument for
                     `pkg_resources.resource_string()`_, defaults to
                     *frameworkName*.

   Load the named framework using the identifier if that has result otherwise
   using the path. Also loads the information in the bridgesupport file (
   either one embedded in the framework or one next to the module that
   called :func:`initFrameworkWrapper`).

   See `Basic structure and use`_ for more information on the way this
   function loads for bridgesupport files.

   .. versionchanged:: 2.4
      This function is not present.

   .. versionchanged:: 2.5
      The function is available again.

.. _`pkg_resources.resource_string()`: http://packages.python.org/distribute/pkg_resources.html#resourcemanager-api

.. rubric:: Footnotes

.. [1] Technically, deprecation started in PyObjC 2.5, the bridgesupport 
       system was temporarily removed in PyObjC 2.4.

.. _`Apple's Objective-C Runtime Programming Guide`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100-SW1
