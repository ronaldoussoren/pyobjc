===============
PyObjC Examples
===============

XXX - UPDATE THIS BEFORE 1.2

Simple scripts that demo the core modules
-----------------------------------------

The directory `Scripts`__ contains a number of simple command-line scripts that make use
of Cocoa features.

.. __: Scripts

* `exportBook.py`__

  An example of using the AddressBook framework, this script exports some of the information
  about people in your addressbook to a CSV file.

.. __: Scripts/exportBook.py

* `autoreadme.py`__

  This script implements an autorun feature for Mac OS X: it will open the ReadMe file in
  the root of every removable medium that is inserted when this script is running.

.. __: Scripts/autoreadme.py 

* subclassing-objective-c.py

  Create a subclass of an objective-C class

* super-call.py

  Likewise, but call super-class implementation of a method

* dictionary.py

  Use a NS*Dictionary object.

* rendezvous.py

  Use an NSNetService class to look for servers using rendezvous.

Cocoa applications
------------------

Most of the following examples contain a ``buildapp.py`` script that can
build an application. See `Building applications`_ for details how to invoke
these scripts. Some examples contain a ``Project Builder`` project file;
simply double-click it and choose ``Build and Run``.

.. _`Building applications`: ../Doc/intro.html#building-applications

* `ClassBrowser`_

  A simple class browser, demonstrating the use of NSBrowser (a "column view"
  hierarchical widget) and NSTableView.

* CocoaBindings

  This directory contains a number of examples that make use of Key-Value Coding and
  Cocoa Bindings. These scripts require Mac OS X 10.3 or later.


  - TableModel

    Shows how to fill an NSTableView using Key-Value Coding. 
  
  - TableModelWithSearch

    A more advanced example of Key-Value Coding. This uses a custom 
    ``NSArrayController``.

* `CurrencyConverter`_

  A simple NIB based application. Start with this one. Also see the PyObjC
  tutorial.

* `DotView`_

  A simple one-window demo showing how to custom drawing in a custom
  NSView. Additionally shows how easy it is to embed a view in an
  NSScrollView, as well as how to use an NSColorWell.

* `EnvironmentPrefs`_

  Another NSPreferencePane. This one can be used to edit the default environment
  for the current user. It also is a simple example of a localized application.

* `FieldGraph`_
  
  Another Project Builder Cocoa project, it also includes a ``buildapp.py`` 
  script. This shows an simple example of an MVC based application, that also
  makes use of NSBezierPaths.

  The application calculates the field pattern and RMS field of an antenna 
  array with up to three elements.

* `iClass`_

  A more elaborate class browser; demonstrates NSOutlineView and NSTableView.

* `PrefPane`_

  Demonstrates how to write an NSPreferencePane, for use in the
  System Preferences application. Requires a framework build of Python.

* `OpenGLDemo`_

  A simple program that shows how to use OpenGL in a Cocoa program.  It is a 
  port of Apple's "CocoaGL" example.  Note that this requires `PyOpenGL`_ to 
  be installed.

* `PackageManager`_
  
  An implementation of the MacPython PackageManager application using
  Cocoa.

* `PyDocURLProtocol`_

  This example implements a subclass of ``NSURLProtocol`` that can be used
  to load the pydoc documentation of a module.

  It also includes a simple documentation browser using ``WebKit`` and the 
  ``PyDocURLProtocol`` class.
  
* `PyInterpreter`_

  A full featured embedded Python interpreter.  This demonstrates
  more complicated uses of NSTextView, manual event dispatching,
  and the new text completion feature of OS X 10.3.

* `PythonBrowser`_

  A reusable Python object browser, demonstrating the use of NSOutlineView
  as well as how to use an NSWindowController subclass to create a window
  from a menu action.

* `SillyBallsSaver`_

  A simple screensaver written in Python. This example requires a framework
  install of Python, that is either Mac OS X 10.3 or a MacPython 2.3 
  installation.

* `SimpleService`_

  Shows how to implement entries for the Services menu.

* `TableModel`_

  Basic demo that shows how to use a NSTableView.

* `TinyTinyEdit`_

  A minimal Document-based text editor application.

* `Todo`_

  A more complex NIB based applications. This is a document-based application.
  The code is a translation into Python of an example project in 
  'Learning Cocoa' from O'Reilly

* `Twisted`_

  This directory contains a number of examples that use `Twisted (1.1 or later)`__ with
  Cocoa.

.. __: http://www.twistedmatrix.com

  - WebServicesTool

    This is a refactor of the WebServicesTool example that is made much simpler
    by using Twisted.

  - WebServicesTool-ControllerLayer

    This is a refactor of the WebServicesTool example that is made much simpler
    by using Twisted as it does not need threads. This version also uses
    NSController and therefore requires Mac OS X 10.3.

* `WebServicesTool`_

  Another Project Builder Cocoa project.  Queries an XML-RPC enabled web
  server for the methods that it implements.  Demonstrates a more advanced
  use of an NSTableView, how to make a toolbar as well as how to use
  multi-threading.

Some work-in-progress examples
------------------------------

The directory ``NonFunctional`` contains a number of examples that are not working
for one reason or another. The most likely reason is that example relies on features
that have not yet been implemented.


* `ProgressViewPalette`_

  An example of a palette for Interface Builder. It is a straight port of an Apple
  example with the same name.

  This example does not work at the moment, due to an incompatibility between
  PyObjC and the way IB looks for classes.


.. _`PyOpenGL`:  http://pyopengl.sourceforge.net/
.. _`ClassBrowser`: ClassBrowser
.. _`CurrencyConverter`: CurrencyConverter
.. _`DotView`: DotView
.. _`iClass`: iClass
.. _`PrefPane`: PrefPane
.. _`EnvironmentPrefs`: EnvironmentPrefs
.. _`PythonBrowser`: PythonBrowser
.. _`TableModel`: TableModel
.. _`TinyTinyEdit`: TinyTinyEdit
.. _`Todo`: Todo
.. _`WebServicesTool`: WebServicesTool
.. _`FieldGraph`: FieldGraph
.. _`PyInterpreter`: PyInterpreter
.. _`OpenGLDemo`: OpenGLDemo
.. _`SillyBallsSaver`: SillyBallsSaver
.. _`PackageManager`: PackageManager
.. _`SimpleService`: SimpleService
.. _`ProgressViewPalette`: NonFunctional/ProgressViewPalette
.. _`PyDocURLProtocol`: PyDocURLProtocol
.. _`Twisted`: Twisted
