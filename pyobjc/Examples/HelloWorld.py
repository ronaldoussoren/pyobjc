# HelloWorld.py
#
# You have to run this script from the command line with 
# the full pathname for python:
#    /usr/local/bin/python HelloWorld.py 
#
# or else run from DropShell or gdb. Anything else and you will get a:
# 	Error 1011 in _sendFinishLaunchingNotification 
# and it wont work.
#
# -- Steve Majewski <sdm7g@Virginia.EDU>
#

# You can look up these classes and methods in the Cocoa docs.
# A quick guide to runtime name mangling:
#
#      ObjC 		becomes 	  Python
#    [ obj method ]   			obj.method()
#    [ obj method: arg ]  		obj.method_(arg)
#    [ obj method: arg1 withOtherArgs: arg2 ] 
#				obj.method_withOtherArgs_( arg1, arg2 )

import objc

# We should import AppKit and Foundation, but don't do that
# here to show we're using just the basic objective-C bindings.
NSBundle = objc.lookup_class('NSBundle')
NSAutoreleasePool = objc.lookup_class('NSAutoreleasePool')
NSApplication = objc.lookup_class('NSApplication')
NSWindow = objc.lookup_class('NSWindow')
NSButton = objc.lookup_class('NSButton')
NSSound = objc.lookup_class('NSSound')
NSObject = objc.lookup_class('NSObject')

class AppDelegate (NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        print "Hello, World!"

def main():

    # Load Application Framework:
    NSBundle.bundleWithPath_(
	'/System/Library/Frameworks/AppKit.framework').load()

    NSApp = NSApplication.sharedApplication()

    NSApp.setDelegate_( AppDelegate.alloc().init() )

    win = NSWindow.alloc()
    frame = ((200.0, 300.0), (250.0, 100.0))
    win.initWithContentRect_styleMask_backing_defer_ (frame, 15, 2, 0)
    win.setTitle_ ('HelloWorld')
    win.setLevel_ (3)			# floating window

    hel = NSButton.alloc().initWithFrame_ (((10.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_ (hel)
    hel.setBezelStyle_( 4 )
    hel.setTitle_( 'Hello!' )

    beep = NSSound.alloc()
    beep.initWithContentsOfFile_byReference_( 
	'/System/Library/Sounds/tink.aiff', 1 )
    hel.setSound_( beep )

    bye = NSButton.alloc().initWithFrame_ (((100.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_ (bye)
    bye.setBezelStyle_( 4 )
    bye.setTarget_ (NSApp)
    bye.setAction_ ('stop:')
    bye.setEnabled_ ( 1 )
    bye.setTitle_( 'Goodbye!' )

    adios = NSSound.alloc()
    adios.initWithContentsOfFile_byReference_( 
	'/System/Library/Sounds/Basso.aiff', 1 )
    bye.setSound_( adios )
    
    win.display()
#    win.makeKeyAndOrderFront_ (NSApp)	## This doesn't seem to  work 
    win.orderFrontRegardless()		## but this one does

    NSApp.run()    


if __name__ == '__main__' : main()


