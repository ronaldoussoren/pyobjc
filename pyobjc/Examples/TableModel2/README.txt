TableModel2
bbum@codefab.com

This is a conversion of Ronald's TableModel example into a standalone Cocoa project.   This project also provides a basic recipe for creating any standalone Cocoa applications (or multiple document applications) that are implemented in Python using the Obj-C bridge.

Projects of this style allow for freely mixing python and objective-c source.  Simply add the python source to the project as you would any other source file.  Project Builder will automatically copy all python source files into the Resources/ directory of the resulting application product.

Because the PyObjC module-- the Cocoa support piece, specifically-- automatically adds the 'Contents/Resources/' directory of the application wrapper to Python's sys.path attribute, any python scripts added to the project will both be automatically copied into the Resources/ directory and automatically found by Python.

Of course, if you localize the python scripts, they won't be automatically found.   However, this would be easy to fix by calling NSBundle's -preferredLocalizations method and adding the associated localization directories to sys.path.

To create a new PyCocoa project in Project Builder, do the following.  Of course, this assumes that pyobjc is correctly installed.   This has been tested with python built via Fink -- it should work fine with any build of python.  Unfortunately, it will not work with the Python shipped with OS X as that distribution is incomplete -- it lacks a library to link against (either dynamic or static).

1. Create a new Cocoa Application or Cocoa Document-based Application

2. Add libpython2.2.a to project (or Python.framework, if using the framework build).  For a standard Fink installation, the library will be in /sw/lib/python2.2/config/.

3. If not using the framework build, add the python include path to the project's search path (/sw/include/python2.2/ for Fink).

4. Replace the main.m in the project with the main.m from this example.

5. Add the key 'PrincipalPythonFile' to the Info.plist.  The value is the name of the Python file that you want to be loaded first as the application starts up.  Whatever Python file is chosen, it should take care of loading any other Python files necessary to define the various classes necessary for application startup.   If this key is not defined, the main() function will try to load the file 'Main.py'.   If that file is not found, the application will raise an exception and exit.

6. Add '-undefined suppress -force_flat_namespace' to the linker flags for the project.  You can also turn off the prebinding feature as it doesn't work anyway.

NOTE:  See the Web Services Tool example as it implements an application that is intended to actually do something useful (beyond the very useful task of testing the PyObjC module).  Also -- step 5 should likely be skipped.  Instead, add a Main.py file to your project that imports all of the python files that define classes necessary for App startup -- see the Web Services Example...

