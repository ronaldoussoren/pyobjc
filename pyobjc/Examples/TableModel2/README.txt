TableModel2
bbum@codefab.com

This is a conversion of Ronald's TableModel example into a standalone Cocoa project.   This project also provides a basic recipe for creating any standalone Cocoa applications (or multiple document applications) that are implemented in Python using the Obj-C bridge.

Projects of this style allow for freely mixing python and objective-c source.  Simply add the python source to the project as you would any other source file.  Project Builder will automatically copy all python source files into the Resources/ directory of the resulting application product.

Because the PyObjC module-- the Cocoa support piece, specifically-- automatically adds the 'Contents/Resources/' directory of the application wrapper to Python's sys.path attribute, any python scripts added to the project will both be automatically copied into the Resources/ directory and automatically found by Python.

Of course, if you localize the python scripts, they won't be automatically found.   However, this would be easy to fix by calling NSBundle's -preferredLocalizations method and adding the associated localization directories to sys.path.

To create a new PyCocoa project in Project Builder, do the following.  Of course, this assumes that pyobjc is correctly installed.  This has been tested both with the Fink build of Python and with the Apple supplied version of Python.

1. Create a new Cocoa Application or Cocoa Document-based Application

2. Replace the main.m in the project with the main.m from this example.

3. Add the key 'PrincipalPythonFile' to the Info.plist.  The value is the name of the Python file that you want to be loaded first as the application starts up.  Whatever Python file is chosen, it should take care of loading any other Python files necessary to define the various classes necessary for application startup.   If this key is not defined, the main() function will try to load the file 'Main.py'.   If that file is not found, the application will raise an exception and exit.

If you want to create a project that will create a standalone Cocoa application that contains all the resources necessary to run the application, perform the following additional steps:

4. [optionally] Create a new group called 'pyobjc'.   This is merely cosmetic.

5. Add a Copy Files phase to the project.

6. Drag in the AppKit, Foundation, and objc directories from /sw/lib/python2.2/site-packages/ and create absolute path references (you can copy the folders into the project, but it isn't a requirement unless there will be developers contributing to the project that do not have pyobjc installed). 

7. Add the AppKit, Foundation, and objc to the Copy Files phase. 

8. Set Copy Files phase to copy the three directories into the Resources area of the wrapper.

9. Set the Copy Files phase to copy the three files into a subdirectory named 'pyobjc' [optional, but keeps the Resources directory more organized].

If you want to mix in compiled Objective-C classes, add a bundle or framework target to your project.   Then, in the Main.py (or equivalent), load the framework or bundle using the NSBundle API as normal.  Because the main class passes control entirely to the python command-line executable, classes linked into the binary in the traditional fashion (by simply adding the source files to the project) will not be available at runtime.

