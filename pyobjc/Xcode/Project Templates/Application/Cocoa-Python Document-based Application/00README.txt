================================
Cocoa-Python Application Project
================================

:Author: Bill Bumgarner
:Contact: bbum@codefab.com

.. contents::

This project is analagous in construction to a regular 
'Cocoa Document-based Application'
Project.  The *only* difference is that the primary language of implementation
is Python.   Once control is passed to the AppKit, a Cocoa-Python application
should behave just like a pure-ObjC Cocoa or Cocoa-Java application.

Application startup
-------------------

The startup sequence is a bit different from a *regular* Cocoa or Coco-Java
application in that control must be passed to the Python interpreter, the
PyObjC bridge must be initialized, and the developer must load any classes
defined in Python that are required to start the application.

The startup sequence::

1. Application is launched from Project Builder, the command line or by
   double clicking.

2. The `pyobjc_main` function in `bin-python-main.m` is invoked.

   This function bootstraps into the command line python interpreter.   For a
   Cocoa application to work correctly, the main executable must reside in
   the app wrapper.   Furthermore, the executable sets up various bits of
   environment prior to passing control to python to fine-tune the execution
   of the application.

   By adding the path to the app wrapper's Resources directory to the
   **PYTHONPATH** environment variable, the pyobjc module can easily be included
   in the app wrapper in an isolated fashion.  This makes it easy to
   distribute a standalone application that uses PyObjC (and other third
   party Python modules) without further cluttering the `Resources` directory.

   By setting the **DYLD_FRAMEWORK_PATH** and **DYLD_LIBRARY_PATH**
   environment variables, embedded frameworks within the app wrapper will
   still link correctly even when dynamcially loaded into the python
   interpreter.

   a) check to see if **PYTHONPATH** environment variable is already set.

      1) if not, define **PYTHONPATH** to contain the path to the `pyobjc`
         directory within the app wrapper's Resources directory.
      2) if so, prepend the path to the `pyobjc` directory
   b) If the **DYLD_FRAMEWORK_PATH** environment variable is not defined, define
         it and **DYLD_LIBRARY_PATH** to include both the shared and private
         frameworks directories within the app wrapper.  If
         **DYLD_FRAMEWORK_PATH**, nothing is defined or redefined[#]_.
   c) Set the environment variable **PYOBJCFRAMEWORKS** to be a colon separated
      list of all of the frameworks linked into the application.
   d) Check the **PythonBinPath** user default to see if something other than
         `/usr/bin/python` should be used as the command line entry point to
         the python interpreter.
   e) Identify the main python script file to execute.   It can be one of
      `__main__.py`, `__realmain__.py` or `Main.py`.  Also searched are the
         same names with `.pyc` or `.pyo` extensions.  Regardless of name, the
         script file should be in the app wrapper's `Resources` directory.
   f) Set up the command line for the python interpreter.   Preserve original
      arguments.
   g) If the SHOWPID environment variable is set, print a command line that
      can be used to attach gdb to the application after it has been launched[#]_.
   h) Pass control to the command line python intepreter using `execve()`.

3. Execute the Main python file

   At this point, control has been passed to the python interpreter (either
   `/usr/bin/python` or some other interpreter executable as specified by the
   **PythonBinPath** user default.

   Care should be taken to ensure that your application behaves appropriately
   if invoked with the "wrong" Python interpreter.

   What follows is a description of the `__main__.py` file as it appears in
   the *Cocoa-Python Application* project template.   Feel free to modify it
   as needed.

   a) Import the the three packages associated with PyObjC;  `objc`,
      `Foundation`, and `AppKit`.

   b) Import any classes that need to be defined before control is passed to
      Cocoa.

      In Python, there is no concept of 'linking' an application.  Any
      classes defined in Python must be imported before they can be used.  As
      such, any classes-- such as `MyAppDelegate` in the project template--
      that are required by the application as it is launched must be
      explicitly imported before control is passed to Cocoa::

      import MyAppDelegate

  c) Pass control to Cocoa by using the `NSApplicationMain()` function.

     Note that this last step is the single step found in `main.m` in a
     regular Cocoa application project.

Classes & NIB files
-------------------


     
.. [#] Project Builder uses these variables to enable linking against
   frameworks in the development environment without requiring that the
   developer install frameworks first.

.. [#] Because control is passed to the python interpreter using `execve()`,
   gdb won't work directly with the application for anything other than
   debugging the code up until the point `execve()` is called.   `Execve()`
   replaces the existing process with the process-- the python interpreter--
   that resides on the path passed as the first argument.  That includes
   replacing all symbol tables which greatly confuses gdb.



