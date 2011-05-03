More About PyObjC
=================

What is PyObjC?
---------------

The PyObjC project aims to provide a bridge between the Python and Objective-C programming languages.  The bridge is 
intended to be fully bidirectional, allowing the Objective-C programmer transparent access to Python based functionality 
and the Python programmer to take full advantage of the power provided by various Objective-C based toolkits.

Currently, development of the bridge is primarily focused upon the `Mac OS X`_ platform. Within this environment, PyObjC 
can be used to entirely replace Objective-C in the development of Cocoa based applications and Foundation based command 
line tools.

For the Python developer: Why use PyObjC?
-----------------------------------------

PyObjC offers the python developer full access to the Objective-C APIs available on `Mac OS X`_ including Foundation, 
AppKit, Address Book, CoreData, and Quartz.  The Python developer can also take advantage of any ANSI-C or C++ 
based API by simply wrapping said API in an Objective-C wrapper and using the PyObjC to access the wrapper.  This is 
often considerably less work than is required to make the same API available directly via the Python embedding API.

For the Objective-C developer: Why use PyObjC?
----------------------------------------------

PyObjC can be pretty much used anywhere the developer might normally implement something in Objective-C.   This includes 
everything from a simple subclass of NSObject through to a custom window controller that acts as a NIB file's owner and 
contains all of the logic for a user interface (including acting as a data source for a table view or combo box).

This provides two distinct advantages to the developer. First, the combination of Python and Cocoa (or for Foundation 
tools) offers an incredible degree of productivity.   The 'compile' part of the edit-compile-run loop can be nearly 
eliminated (currently, the 'run' part still exists, but reloading of classes on the fly is in the works).  Also, many 
common idioms can be expressed in Python with many fewer lines of code than the Objective-C coounterpart.

Secondly, Objective-C based applications can take advantage of the vast selection of Python modules both included with 
the `standard python distribution`_ or `by third parties`_.

.. _`Mac OS X`: http://www.apple.com/macosx/

..   _`standard python distribution`: http://ww.python.org/

..   _`by third parties`: http://pypi.python.org/
