If you are reading this from the PyObjC disk image that contains the Installer
package, simply Install the package and look in /Developer/Examples/PyObjC.

Documentation is pretty imcomplete at the moment, look in 
/Developer/Documentation/PyObjC for the documentation we have.

The PyObjC package provides the glue needed to interface the Python interpreter with the Objective-C language. The 'objc' module makes Objective-C objects and classes available as first-class Python citizens, it is not only possible to use Objective-C objects but you can also subclass Objective-C classes.

If you are installing from the Installer package, it also installs a Project Builder template for building Python based Cocoa applications.  Once installed, create a new "Cocoa-Python Application" project in Project Builder.  The newly created project includes an application delegate implementation and a simple set of Cocoa controls-- i.e. it provides a complete example of how to build a Cocoa application using Python and the PyObjC bridge.

The latest information can always be found at:

    http://pyobjc.sourceforge.net/

b.bum
bbum@codefab.com
12-Oct-2002

History:

Ronald Oussoren <oussoren@cistron.nl> rewrote most of the module in 2002.  Ronald made it possible to subclass Objective-C classes from Python and added nearly complete support for the Foundation, the AppKit and the AddressBook frameworks.

In the fall of 2002, Bill Bumgarner<bbum@codefab.com> added support for non-Framework builds of python.  Ronald and Bill subsequently added support for the Apple supplied build of Python.   Bill created the Project Builder template that allows for building standalone Cocoa applications that are implemented in Project Builder.

Steve Majewski <sdm7g@minsky.med.virginia.edu> and Bill Bumgarner <bbum@codefab.com> picked up Lele's work in early November, 2000. Steve significanlty improved compatibility with OS X.

Lele Gaifax built the original module which dates back to September 1996.  Lele's original list of contributors/motivators was as follows:

I should say "Grazie" to many persons that made this possible, but to some in particular:

Guido van Rossum <guido@CNRI.Reston.VA.US>:
  Long list of motivation omitted ;-)

Thomas Breuel <tmb@best.com>:
  He first inspired me with good ideas.

Ted Horst <ted_horst@il.us.swissbank.com>:
  His own ObjC module and kind comments helped me a lot.

Bill Bumgarner <bbum@friday.com>:
        He contribuited the standalone packaging setup, good comments and his own implementation of the Streams and Pasteboards support. He  maintained also several Python-related packages for NeXTSTEP: see <ftp://ftp.thoughtport.net/pub/next/lang> [long gone;  see http://www.friday.com/software/python/]

...and of course to the entire ObjC-SIG community.

