"""AppKit helpers.

Exported functions:
* runEventLoop - run NSApplicationMain in a safer way
* runConsoleEventLoop - run NSRunLoop.run() in a stoppable manner
* stopEventLoop - stops the event loop or terminates the application
* endSheetMethod - set correct signature for NSSheet callbacks
* callAfter - call a function on the main thread (async)
* callLater - call a function on the main thread after a delay (async)
"""

__all__ = ( 'runEventLoop', 'runConsoleEventLoop', 'stopEventLoop', 'endSheetMethod', 'callAfter', 'callLater' )

from AppKit import (NSApp, NSRunAlertPanel, NSApplicationMain,
                    NSApplicationDidFinishLaunchingNotification)
from Foundation import (NSObject, NSRunLoop, NSTimer, NSDefaultRunLoopMode,
                        NSNotificationCenter, NSLog, NSAutoreleasePool)

import os
import sys
import traceback
import objc

class PyObjCAppHelperCaller(NSObject):

    def initWithArgs_(self, args):
        self = self.init()
        self.args = args
        return self

    def callAfter_(self, sender):
        self.performSelectorOnMainThread_withObject_waitUntilDone_(
            self.call_, self.args, False)

    def callLater_(self, delay):
        self.performSelector_withObject_afterDelay_(
            self.callAfter_, None, delay)

    def call_(self, func_args_kwargs):
        (func, args, kwargs) = func_args_kwargs
        func(*args, **kwargs)


def callAfter(func, *args, **kwargs):
    """call a function on the main thread (async)"""
    pool = NSAutoreleasePool.alloc().init()
    obj = PyObjCAppHelperCaller.alloc().initWithArgs_((func, args, kwargs))
    obj.callAfter_(None)
    del obj
    del pool

def callLater(delay, func, *args, **kwargs):
    """call a function on the main thread after a delay (async)"""
    pool = NSAutoreleasePool.alloc().init()
    obj = PyObjCAppHelperCaller.alloc().initWithArgs_((func, args, kwargs))
    obj.callLater_(delay)
    del obj
    del pool

class PyObjCAppHelperApplicationActivator(NSObject):

    def activateNow_(self, aNotification):
        NSApp().activateIgnoringOtherApps_(True)


class PyObjCAppHelperRunLoopStopper(NSObject):
    singletons = {}

    def currentRunLoopStopper(cls):
        runLoop = NSRunLoop.currentRunLoop()
        return cls.singletons.get(runLoop)
    currentRunLoopStopper = classmethod(currentRunLoopStopper)

    def init(self):
        self = super(PyObjCAppHelperRunLoopStopper, self).init()
        self.shouldStop = False
        return self

    def shouldRun(self):
        return not self.shouldStop

    def addRunLoopStopper_toRunLoop_(cls, runLoopStopper, runLoop):
        if runLoop in cls.singletons:
            raise ValueError("Stopper already registered for this runLoop")
        cls.singletons[runLoop] = runLoopStopper
    addRunLoopStopper_toRunLoop_ = classmethod(addRunLoopStopper_toRunLoop_)

    def removeRunLoopStopperFromRunLoop_(cls, runLoop):
        if runLoop not in cls.singletons:
            raise ValueError("Stopper not registered for this runLoop")
        del cls.singletons[runLoop]
    removeRunLoopStopperFromRunLoop_ = classmethod(removeRunLoopStopperFromRunLoop_)

    def stop(self):
        self.shouldStop = True
        # this should go away when/if runEventLoop uses
        # runLoop iteration
        if NSApp() is not None:
            NSApp().terminate_(self)

    def performStop_(self, sender):
        self.stop()


def stopEventLoop():
    """
    Stop the current event loop if possible
    returns True if it expects that it was successful, False otherwise
    """
    stopper = PyObjCAppHelperRunLoopStopper.currentRunLoopStopper()
    if stopper is None:
        if NSApp() is not None:
            NSApp().terminate_(None)
            return True
        return False
    NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
        0.0,
        stopper,
        'performStop:',
        None,
        False)
    return True


def endSheetMethod(meth):
    """
    Return a selector that can be used as the delegate callback for
    sheet methods
    """
    return objc.selector(meth, signature=b'v@:@ii')


def unexpectedErrorAlertPanel():
    exceptionInfo = traceback.format_exception_only(
        *sys.exc_info()[:2])[0].strip()
    return NSRunAlertPanel("An unexpected error has occurred",
            "%@",
            "Continue", "Quit", None, "(%s)" % exceptionInfo)


def unexpectedErrorAlertPdb():
    import pdb
    traceback.print_exc()
    pdb.post_mortem(sys.exc_info()[2])
    return True


def machInterrupt(signum):
    stopper = PyObjCAppHelperRunLoopStopper.currentRunLoopStopper()
    if stopper is not None:
        stopper.stop()
    elif NSApp() is not None:
        NSApp().terminate_(None)
    else:
        import os
        os._exit(1)


def installMachInterrupt():
    try:
        import signal
        from PyObjCTools import MachSignals
    except:
        return
    MachSignals.signal(signal.SIGINT, machInterrupt)


def runConsoleEventLoop(argv=None, installInterrupt=False, mode=NSDefaultRunLoopMode):
    if argv is None:
        argv = sys.argv
    if installInterrupt:
        installMachInterrupt()
    runLoop = NSRunLoop.currentRunLoop()
    stopper = PyObjCAppHelperRunLoopStopper.alloc().init()
    PyObjCAppHelperRunLoopStopper.addRunLoopStopper_toRunLoop_(stopper, runLoop)
    try:

        while stopper.shouldRun():
            nextfire = runLoop.limitDateForMode_(mode)
            if not stopper.shouldRun():
                break
            if not runLoop.runMode_beforeDate_(mode, nextfire):
                stopper.stop()

    finally:
        PyObjCAppHelperRunLoopStopper.removeRunLoopStopperFromRunLoop_(runLoop)


RAISETHESE = (SystemExit, MemoryError, KeyboardInterrupt)


def runEventLoop(argv=None, unexpectedErrorAlert=None, installInterrupt=None, pdb=None, main=NSApplicationMain):
    """Run the event loop, ask the user if we should continue if an
    exception is caught. Use this function instead of NSApplicationMain().
    """
    if argv is None:
        argv = sys.argv

    if pdb is None:
        pdb = 'USE_PDB' in os.environ

    if pdb:
        from PyObjCTools import Debugging
        Debugging.installVerboseExceptionHandler()
        # bring it to the front, starting from terminal
        # often won't
        activator = PyObjCAppHelperApplicationActivator.alloc().init()
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            activator,
            'activateNow:',
            NSApplicationDidFinishLaunchingNotification,
            None,
        )
    else:
        Debugging = None

    if installInterrupt is None and pdb:
        installInterrupt = True

    if unexpectedErrorAlert is None:
        if pdb:
            unexpectedErrorAlert = unexpectedErrorAlertPdb
        else:
            unexpectedErrorAlert = unexpectedErrorAlertPanel

    runLoop = NSRunLoop.currentRunLoop()
    stopper = PyObjCAppHelperRunLoopStopper.alloc().init()
    PyObjCAppHelperRunLoopStopper.addRunLoopStopper_toRunLoop_(stopper, runLoop)

    firstRun = NSApp() is None
    try:

        while stopper.shouldRun():
            try:
                if firstRun:
                    firstRun = False
                    if installInterrupt:
                        installMachInterrupt()
                    main(argv)
                else:
                    NSApp().run()
            except RAISETHESE:
                traceback.print_exc()
                break
            except:
                exctype, e, tb = sys.exc_info()
                objc_exception = False
                if isinstance(e, objc.error):
                    NSLog("%@", unicode(str(e), 'utf-8', 'replace'))
                elif not unexpectedErrorAlert():
                    NSLog("%@", "An exception has occured:")
                    traceback.print_exc()
                    sys.exit(0)
                else:
                    NSLog("%@", "An exception has occured:")
                    traceback.print_exc()
            else:
                break

    finally:
        if Debugging is not None:
            Debugging.removeExceptionHandler()
        PyObjCAppHelperRunLoopStopper.removeRunLoopStopperFromRunLoop_(runLoop)
