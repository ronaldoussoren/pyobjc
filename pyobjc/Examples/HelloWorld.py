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

import pyobjc
rt = pyobjc.runtime	# shorthand -- runtime gets used a lot!

def main():

    pool = rt.NSAutoreleasePool()

    # Load Application Framework:
    rt.NSBundle.bundleWithPath_( 
	'/System/Library/Frameworks/AppKit.framework').load()

    NSApp = rt.NSApplication.sharedApplication()

    win = rt.NSWindow.alloc()
    frame = ((200.0, 300.0), (250.0, 100.0))
    win.initWithContentRect_styleMask_backing_defer_ (frame, 15, 2, 0)
    win.setTitle_ ('HelloWorld')
    win.setLevel_ (3)			# floating window

    hel = rt.NSButton.alloc().initWithFrame_ (((10.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_ (hel)
    hel.setBezelStyle_( 4 )
    hel.setTitle_( 'Hello!' )

    beep = rt.NSSound.alloc()
    beep.initWithContentsOfFile_byReference_( 
	'/System/Library/Sounds/tink.aiff', 1 )
    hel.setSound_( beep )

    bye = rt.NSButton.alloc().initWithFrame_ (((100.0, 10.0), (80.0, 80.0)))
    win.contentView().addSubview_ (bye)
    bye.setBezelStyle_( 4 )
    bye.setTarget_ (NSApp)
    bye.setAction_ ('stop:')
    bye.setEnabled_ ( 1 )
    bye.setTitle_( 'Goobye!' )

    adios = rt.NSSound.alloc()
    adios.initWithContentsOfFile_byReference_( 
	'/System/Library/Sounds/Basso.aiff', 1 )
    bye.setSound_( adios )
    
    win.display()
#    win.makeKeyAndOrderFront_ (NSApp)	## This doesn't seem to  work 
    win.orderFrontRegardless()		## but this one does

    NSApp.run()    


if __name__ == '__main__' : main()


