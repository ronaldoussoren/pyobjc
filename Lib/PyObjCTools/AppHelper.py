"""AppKit helpers.

Exported functions:
* runEventLoop - run NSApplicationMain in a safer way
* endSheetMethod - set correct signature for NSSheet callbacks
"""

__all__ = ( 'runEventLoop', 'runConsoleEventLoop', 'endSheetMethod' )

from AppKit import NSApplicationMain, NSApp, NSRunAlertPanel
from Foundation import NSLog, NSRunLoop
import sys
import traceback
import objc as _objc


def endSheetMethod(meth):
    """
    Return a selector that can be used as the delegate callback for
    sheet methods
    """
    return _objc.selector(meth, signature='v@:@ii')



def unexpectedErrorAlert():
    exceptionInfo = traceback.format_exception_only(
        *sys.exc_info()[:2])[0].strip()
    return NSRunAlertPanel("An unexpected error has occurred",
            "(%s)" % exceptionInfo,
            "Continue", "Quit", None)


def machInterrupt(signum):
    app = NSApp()
    if app:
        app.terminate_(None)
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

def runConsoleEventLoop(argv=None, installInterrupt=False):
    if argv is None:
        argv = sys.argv
    if installInterrupt:
        installMachInterrupt()
    NSRunLoop.currentRunLoop().run()

def runEventLoop(argv=None, unexpectedErrorAlert=unexpectedErrorAlert, installInterrupt=False):
    """Run the event loop, ask the user if we should continue if an
    exception is caught. Use this function instead of NSApplicationMain().
    """
    if argv is None:
        argv = sys.argv

    firstRun = 1
    while 1:
        try:
            if firstRun:
                firstRun = 0
                if installInterrupt:
                    installMachInterrupt()
                NSApplicationMain(argv)
            else:
                NSApp().run()
        except:
            if not unexpectedErrorAlert():
                NSLog("An exception has occured:")
                raise
            else:
                NSLog("An exception has occured:")
                traceback.print_exc()
        else:
            break
