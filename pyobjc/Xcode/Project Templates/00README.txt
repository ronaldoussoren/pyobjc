========================
Python Project Templates
========================

:Author: Bill Bumgarner
:Contact: bbum@mac.com

To use the project templates, simply copy (or link) them into the Project
Templates directory used by Project Builder.  The project templates are also
included in the PyObjC installer package.

.. contents::

Notes
-----

- In all cases that involve loading frameworks or bundles, all of the classes
  in that framework or bundle can be made available by using the
  ``loadBundle()`` function in the ``objc`` module::

    objc.loadBundle("MyFramework", globals(), bundle_path="/path/to/MyFramework.framework")

  This has the effect of importing all of the classes in the bundle or
  framework into the current python scope's globals.  For all intents and
  purposes, it is similar to::

    from Foundation import *

- There is risk that the pyobjc modules compiled for one version of python
  will not work with another.  Where this may be a problem is if the a
  standalone application is packaged with the pyobjc modules compiled
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
application projects.  Be sure and pick the correct project type for your
needs.

Cocoa-Python Application
------------------------

A project created from this template is designed to implement standalone,
pure-Python, applications that are compatible with Apple's build of Python as
well as all other builds of python that support PyObjC.

When building the 'install' target, the resulting application wrapper will
included the PyObjC module and can be launched on any stock OS X 10.3 system
without requiring PyObjC to be preinstalled.

