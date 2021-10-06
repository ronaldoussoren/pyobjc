============================
PyObjC with InterfaceBuilder
============================

.. warning:: This file is out of date

PyObjC can be used with InterfaceBuilder, the best way to use Interface Builder
depends on the version of Xcode you are using.

XCode 3 on MacOSX 10.5
----------------------

When you're running MacOSX 10.5, with Xcode 3 or later, Interface Builder has
builtin support for Python and can extract class, action and outlet definitions
from Python source code.

To define a class that will be picked up by Interface Builder:

 .. sourcecode:: python

     class MyModel (NSObject):

          window = objc.IBOutlet()

	  @objc.IBAction
	  def doSomething_(self, sender):
	      pass

Interface Builder obviously has to know about the source files that contain
your Python classes. There are two ways to accomplisch this, depending on
whether or not you use Xcode. If you use Xcode Interface Builder will
automatically pick up all source code that's added to your project and it will
also automatically detect changes to those sources.

If you do not use Xcode you can add new source files to Interface Builder using
the "File -> Read Class Files ..." menu. This will scan the sources, but will
not automatically detect changes to those sources, use the menu
"File -> Reload All Class Files" to reload the class definitions.

XCode 2 on MacOSX 10.4
----------------------

*This section is fairly minimal because I've stopped using Xcode 2 and do all
my development on OSX 10.5*

The version of Xcode that ships with Xcode 2 does not support Python code,
which means that you will have to define your classes twice: one times in
