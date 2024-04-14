"""
Check if NSModalSessions are properly wrapped.

NOTE: This is not a proper unittest, it requires human eyes to check if the
output is correct.
"""

import time

from Cocoa import (
    NSApplication,
    NSGetInformationalAlertPanel,
    NSReleaseAlertPanel,
    NSObject,
    NSApp,
    NSWindow,
)


def doTest():
    alertPanel = None
    modalSession = None
    app = NSApplication.sharedApplication()
    try:
        alertPanel = NSGetInformationalAlertPanel(
            "Please wait", "Bla bla bla", None, None, None
        )
        modalSession = app.beginModalSessionForWindow_(alertPanel)

        print(modalSession, modalSession.__pointer__)
        time.sleep(1)
    finally:
        if modalSession is not None:
            app.endModalSession_(modalSession)
            modalSession = None

        if alertPanel is not None:
            NSReleaseAlertPanel(alertPanel)
            alertPanel = None


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        doTest()
        aNotification.object().terminate_(None)


def main():
    app = NSApplication.sharedApplication()

    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)

    win = NSWindow.alloc()
    frame = ((200.0, 300.0), (250.0, 100.0))
    win.initWithContentRect_styleMask_backing_defer_(frame, 15, 2, 0)
    win.setTitle_("HelloWorld")

    app.run()


if __name__ == "__main__":
    main()
