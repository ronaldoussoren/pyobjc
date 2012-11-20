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


Detailed file structure
-----------------------

.. todo:: fully describe the metadata supported by PyObjC

.. seealso::

   `BridgeSupport(5) <http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man5/BridgeSupport.5.html>`__
     Apple manual page describing the metadata format


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
