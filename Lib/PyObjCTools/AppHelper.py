"""AppKit helpers.

Exported functions:
* runEventLoop - run NSApplicationMain in a safer way
* sheetEndMethod - set correct signature for NSSheet callbacks
"""

from AppKit import NSApplicationMain, NSApp, NSRunAlertPanel
from Foundation import NSLog
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
            if not unexpectedErrorAlert():
                NSLog("An exception has occured:")
                raise
            else:
                NSLog("An exception has occured:")
                traceback.print_exc()
        else:
            break
