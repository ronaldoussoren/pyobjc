This directory contains a number of examples for using the pyobjc module.

A number of simple scripts that demo the core module.

- subclassing-objective-c.py

  Create a subclass of an objective-C class

- super-call.py

  Likewise, but call super-class implementation of a method

- dictionary.py

  Use a NS*Dictionary object.

- rendezvous.py

  Use an NSNetService class to look for servers using rendezvous.

And a number of Cocoa applications. These use the 'AppKit' package.

- ClassBrowser

  A simple class browser, demonstrating the use of NSBrowser (a "column view"
  hierarchical widget) and NSTableView.

- CurrencyConverter

  A simple NIB based application. Start with this one. Also see the PyObjC
  tutorial.

- DotView

  A simple one-window demo showing how to custom drawing in a custom
  NSView. Additionally shows how easy it is to embed a view in an
  NSScrollView, as well as how to use an NSColorWell.

- iClass

  A more elaborate class browser; demonstrates NSOutlineView and NSTableView.

- PrefPane

  Demonstrates how to write an NSPreferencePane, for use in the
  System Preferences application. Requires a framework build of Python.

- PythonBrowser

  A reusable Python object browser, demonstrating the use of NSOutlineView
  as well as how to use an NSWindowController subclass to create a window
  from a menu action.

- TableModel

  Basic demo that shows how to use a NSTableView.

- Todo

  A more complex NIB based applications. This is a document-based application.
  The code is a translation into pyton of an example project in 
  'Learning Cocoa' from O'Reilly

- WebServicesTool

  Another Project Builder Cocoa project.  Quiries an XML-RPC enabled web
  server for the methods that it implements.  Demonstrates a more advanced
  use of an NSTableView, how to make a toolbar as well as how to use
  multi-threading.

- FieldGraph
  
  Another Project Builder Cocoa project, it also includes a ``buildapp.py`` 
  script. This shows an simple example of an MVC based application, that also
  makes use of NSBezierPaths.

  The application calculates the field pattern and RMS field of an antenna 
  array with up to three elements.
