"""
Application helpers.

Currently only a single function is exported: runEventloop
"""
from AppKit import NSApplicationMain, NSApp, NSRunAlertPanel

def unexpectedErrorAlert():
    exceptionInfo = traceback.format_exception_only(
        *sys.exc_info()[:2])[0].strip()
    return NSRunAlertPanel("An unexpected error has occurred",
            "(%s)" % exceptionInfo,
            "Continue", "Quit", None)


def runEventloop(argv, unexpectedErrorAlert = unexpectedErrorAlert):
    """
    Run the eventloop, ask the user if we should continue when 
    catching exceptions. Use this function instead of NSApplicationMain
    """
    mainFunc = NSApplicationMain
    args = (argv,)
    while 1:
        try:
            mainFunc(*args)
        except:
            if not unexpectedErrorAlert():
                raise
            mainFunc = NSApp().run
            args = ()
        else:
            break
