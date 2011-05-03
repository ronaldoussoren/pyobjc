a module and/or demo program implementing a Python object browser
=================================================================

It can be used in two ways:
1) as a standalone demo app that shows how to use the NSOutlineView class
2) as a module to add an object browser to your app.

For the latter usage, include PythonBrowser.nib in your app bundle,
make sure that PythonBrowser.py and PythonBrowserModel.py can be found
on sys.path, and call

.. ::

    PythonBrowser.PythonBrowserWindowController(aBrowsableObject)

from your app. The object to be browsed can't be a number, a string or
None, any other kind of object is fine.

To build the demo program, run this line in Terminal.app::

   $ python setup.py py2app -A

This creates a directory "dist" containing PythonBrowser.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)

