========================
Python Project Templates
========================

:Author: Bill Bumgarner
:Contact: bbum@codefab.com

To use the project templates, simply copy (or link) them into the Project
Templates directory used by Project Builder.  The project templates are also
included in the PyObjC installer package.

.. contents::

Notes
-----

- PyObjC's Project Builder support is unmaintained and its use for new projects
  is not recommended.

- In all cases that involve loading frameworks or bundles, all of the classes
  in that framework or bundle can be made available by using the
  ``loadBundle()`` function in the ``objc`` module::

    objc.loadBundle("MyFramework", globals(), bundle_path="/path/to/MyFramework.framework")

  This has the effect of importing all of the classes in the bundle or
  framework into the current python scope's globals.  For all intents and
  purposes, it is similar to::

    from Foundation import *

- There is risk that the PyObjC modules compiled for one version of python
  will not work with another.  Where this may be a problem is if the a
  standalone application is packaged with the PyObjC modules compiled
  against, say, the Fink or Framework builds of Python, but is then executed
  using the Apple supplied python binary.

 - The *Project Templates* directory includes a **clean.py** script that
   removes noise files from the project templates.   When working on project
   templates, it is recommended that this script be invoked before creating a
   test project from one of the templates.   For example, the presence of
   user specific project builder settings will cause any projects created
   from a template to be incorrect.
    
Cocoa-Python Templates
----------------------

The Cocoa-Python templates all create various different kinds of Cocoa
application projects.   Some of the resulting projects are incompatible with
Apple's build of Python[#].  Be sure and pick the correct project type for your
needs.

Cocoa-Python Application
------------------------

A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.

When building the 'install' target, the resulting application wrapper will
included the PyObjC module and can be launched on any stock OS X 10.2 system
without requiring PyObjC to be preinstalled.

Cocoa-Python-ObjC Application
-----------------------------

A project created from this template includes an embedded framework project
into which all compiled code can be placed.  Upon launch, the application
automatically dynamically loads the embedded framework containing the
compiled code.

Each Framework's Resources directory is automatically added to sys.path.

.. Cocoa-Python Application (Embedded Interpreter)
   -----------------------------------------------

.. This project template uses an embedded Python interpreter.  As such,
   Objective-C classes can be freely mixed into the project along with Python
   classes.   However, because it uses an embedded interpreter, this project
   must be built and run after some version of Python is installed that can
   support an embedded interpreter.  Alternatively, an application based on this
   template must include a build of Python within its app wrapper.

.. This type of project is not compatible with Apple's build of Python.

Cocoa-Python Document-based Application
---------------------------------------

This template works like the `Cocoa-Python Application`_ template in that it
is compatible with the Apple build of Python.   It creates an application
that uses Cocoa's Multiple Document Architecture in the same fashion as the
default Cocoa Document-based Application supplied with Project Builder.

Cocoa-Python-ObjC Document-based Application
--------------------------------------------

A project created from this template includes an embedded framework project
into which all compiled code can be placed.  Upon launch, the application
automatically dynamically loads the embedded framework containing the
compiled code. It is based on the `Cocoa-Python Document-based Application`_
template.  It creates an application that uses Cocoa's Multiple Document 
Architecture in the same fashion as the default Cocoa Document-based 
Application supplied with Project Builder.

Each Framework's Resources directory is automatically added to sys.path.

.. Cocoa-Python Document-based Application (Embedded Interpreter)
   --------------------------------------------------------------

.. This template works like the `Cocoa-Python Application (Embedded
   Interpreter)`_ template in that it is incompatible with the Apple build of
   Python.   It creates an application that uses Cocoa's Multiple Document
   Architecture in the same fashion as the default Cocoa Document-based
   Application supplied with Project Builder.

.. [#] Apple's build of python lacks a shared or static library to which an
       application can be linked.  As such, it is impossible to embed the
       Python interpreter into an application.  Because of this, it is
       impossible to directly link compiled objective-c directly into an
       application project.  Hence, the "Apple Python compatible" projects are
       labeled as 100% pure Python.  Since bundles and frameworks can be
       loaded into such applications, it is still possible to use compiled
       classes.
