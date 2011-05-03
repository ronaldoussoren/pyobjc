"""HotKey.py

An example that shows how to use Carbon HotKeys from a PyObjC application,
and how to use an NSApplication subclass.

To build the demo program, run this line in Terminal.app:

    $ python setup.py py2app -A

This creates a directory "dist" containing HotKey.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)
"""

from AppKit import *
from PyObjCTools import AppHelper
from Carbon.CarbonEvt import RegisterEventHotKey, GetApplicationEventTarget
from Carbon.Events import cmdKey, controlKey
import struct

kEventHotKeyPressedSubtype = 6
kEventHotKeyReleasedSubtype = 9

class HotKeyApp(NSApplication):

    def finishLaunching(self):
        super(HotKeyApp, self).finishLaunching()
        # register cmd-control-J
        self.hotKeyRef = RegisterEventHotKey(38, cmdKey | controlKey, (0, 0),
                                             GetApplicationEventTarget(), 0)

    def sendEvent_(self, theEvent):
        if theEvent.type() == NSSystemDefined and \
               theEvent.subtype() == kEventHotKeyPressedSubtype:
            self.activateIgnoringOtherApps_(True)
            NSRunAlertPanel(u'Hot Key Pressed', u'Hot Key Pressed',
                None, None, None)
        super(HotKeyApp, self).sendEvent_(theEvent)

if __name__ == "__main__":
    AppHelper.runEventLoop()
