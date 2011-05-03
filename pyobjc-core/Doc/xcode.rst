============================
PyObjC with InterfaceBuilder
============================

PyObjC can be used with InterfaceBuilder, the best way to use Interface Builder
depends on the version of Xcode you are using.

XCode 3 on MacOSX 10.5
----------------------

When you're running MacOSX 10.5, with Xcode 3 or later, Interface Builder has
builtin support for Python and can extract class, action and outlet definitions
from Python source code. 

To define a class that will be picked up by Inteface Builder:

 .. sourcecode:: python

     class MyModel (NSObject):

          window = objc.IBOutlet()

	  @objc.IBAction
	  def doSomething_(self, sender):
	      pass

Inteface Builder obviously has to know about the source files that contain
your Python classes. There are two ways to accomplisch this, depending on 
whether or not you use Xcode. If you use Xcode Interface Builder will 
automaticly pick up all source code that's added to your project and it will
also automaticly detect changes to those sources. 

If you do not use Xcode you can add new source files to Interface Builder using
the "File -> Read Class Files ..." menu. This will scan the sources, but will
not automaticly detect changes to those sources, use the menu 
"File -> Reload All Class Files" to reload the class definitions.

XCode 2 on MacOSX 10.4
----------------------

*This section is fairly minimal because I've stopped using Xcode 2 and do all 
my development on OSX 10.5*

The version of Xcode that ships with Xcode 2 does not support Python code,
which means that you will have to define your classes twice: one times in 
actual (Python) code, and then again in Interface Builder.

Deprecation note: ``PyObjCTools.NibClassBuilder``
.................................................

The module ``PyObjCTools.NibClassBuilder`` allows you to remove some of the
duplication in class definitions between Python and Interface Builder. This
module was used a lot before Xcode 3 was released, but is now deprecated and
doesn't work with NIB files created in Xcode 3.

Please migrate to manual class definitions (as described in the section about
Xcode 3) as soon as possible. This is slightly more work, but ensures that your
code will work with later versions of Xcode and PyObjC.
