"""Application helpers.

Currently only a single function is exported: runEventLoop().
"""

from AppKit import NSApplicationMain, NSApp, NSRunAlertPanel
from Foundation import NSLog
import sys
import traceback


def unexpectedErrorAlert():
    exceptionInfo = traceback.format_exception_only(
        *sys.exc_info()[:2])[0].strip()
    return NSRunAlertPanel("An unexpected error has occurred",
            "(%s)" % exceptionInfo,
            "Continue", "Quit", None)


def runEventLoop(argv=None, unexpectedErrorAlert=unexpectedErrorAlert):
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
                NSApplicationMain(argv)
            else:
                NSApp().run()
        except:
            NSLog("An exception has occured:")
            if not unexpectedErrorAlert():
                raise
            else:
                traceback.print_exc()
        else:
            break
