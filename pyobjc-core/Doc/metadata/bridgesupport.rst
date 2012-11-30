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
supported child nodes and attributes.

The document can contain other nodes, attributes, and extra whitespace and those will be ignored by
the bridgesupport parser.

Bridgesupport elements are processed in an undefined order, the side effects of alle elements that have
the same name will take place but it is undefined which definition will be bound to a name in the module
globals dictionary.

.. seealso::

   `BridgeSupport(5)`_ 
     Apple manual page describing the metadata format

Type signatures
...............

A number of nodes have a "type" attribute that contains an Objective-C runtime type encoding. Most contain
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

<cftype>
.........

Nodes of this type define a CoreFoundation type, such :c:type:`CFURLRef`. These nodes are used to 
define a Python proxy for the CoreFoundation type and to register that type with the bridge. The proxy
type is a subclass of :class:`objc_object`.

These nodes do not have child nodes, all information is encoded in attributes:

 * *name*:           the name of the Objetive-C type (such as :c:type:`CFURLRef`
 * *type*, *type64*: the type encoding for the Objective-C type, *type64* contains the encoding for use 
   in 64-bit mode when that encoding is different from the encoding used in 32-bit mode.
 * *gettypeid_func*: (optional) the name of a C function for retrieving the type ID of the type, the default is derived
   from the name.
 * *tollfree*:       (optional) the name of an Objective-C class that is tollfree bridged to this type
   For tollfree bridged types the bridge does not create a new proxy type, but reuses the proxy type for the
   Objective-C class. That is, in Python the CoreFoundation and Objective-C interfaces can be used without
   any form of casting.


<class>
.......

<constant>
..........

<enum>
......

<function>
..........

<function_pointer>
..................

<informal_protocol>
...................

<null_const>
............

<opaque>
........

<string_constant>
.................

<struct>
........


.. _`BridgeSupport(5)`: http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`

.. _`Apple's manual page for BridgeSupport`: http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`


API description
---------------

.. function:: parseBridgeSupport(xmldata, globals, frameworkName[, dylib_path[, inlineTab[, bundle]]])

   Load a `BridgeSupport XML file <http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`_
   with metadata for a framework.

   The definitions from the framework will be added to the *globals* dictionary. *Dylib_path* is an optional path to a shared library
   "dylib") with additional definitions, *inlineTab* is an optional capsule object with function definitions (see :func:`loadFunctionList` for
   more information on the capsule). The *bundle* argument is used to load global variables.
                  
   .. note::

      This function is primarily present for backward compatibility and for users that need an easy way to wrap their own Objective-C code.
      PyObjC itself uses a different metadata mechanism that's better tuned to the needs of PyObjC.

   .. versionchanged:: 2.4
      This function is not present in PyObjC 2.4

   .. versionchanged:: 2.5
      The function is available again in PyObjC 2.5, and adds the *bundle* argument.



.. function:: initFrameworkWrapper(frameworkName, frameworkPath, frameworkIdentifier, globals[, inlineTab [, scan_classes[, frameworkResourceName]]])

   Load the named framework using the identifier if that has result otherwise
   using the path. Also loads the information in the bridgesupport file (
   either one embedded in the framework or one next to the module that
   called :func:`initFrameworkWrapper`).

   See `Basic structure and use`_ for more information on the way this
   function loads for bridgesupport files.


.. rubric:: Footnotes

.. [1] Technically, deprecation started in PyObjC 2.5, the bridgesupport 
       system was temporarily removed in PyObjC 2.4.

.. _`Apple's Objective-C Runtime Programming Guide`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100-SW1
