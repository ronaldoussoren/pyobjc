"""HotKey.py

An example that shows how to use Carbon HotKeys from a PyObjC application,
and how to use an NSApplication subclass.

To build the demo program, run this line in Terminal.app:

    $ python setup.py py2app -A

This creates a directory "dist" containing HotKey.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)

NOTE: This example requires Python 2 because it uses the "Carbon"
      module that was removed in Python 3.
"""
from Carbon.CarbonEvt import GetApplicationEventTarget, RegisterEventHotKey
from Carbon.Events import cmdKey, controlKey

import Cocoa
from objc import super
from PyObjCTools import AppHelper

kEventHotKeyPressedSubtype = 6
kEventHotKeyReleasedSubtype = 9


class HotKeyApp(Cocoa.NSApplication):
    def finishLaunching(self):
        super().finishLaunching()
        # register cmd-control-J
        self.hotKeyRef = RegisterEventHotKey(
            38, cmdKey | controlKey, (0, 0), GetApplicationEventTarget(), 0
        )

    def sendEvent_(self, theEvent):
        if (
            theEvent.type() == Cocoa.NSSystemDefined
            and theEvent.subtype() == kEventHotKeyPressedSubtype
        ):
            self.activateIgnoringOtherApps_(True)
            Cocoa.NSRunAlertPanel(
                "Hot Key Pressed", "Hot Key Pressed", None, None, None
            )
        super().sendEvent_(theEvent)


if __name__ == "__main__":
    AppHelper.runEventLoop()
