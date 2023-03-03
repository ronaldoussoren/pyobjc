#!/usr/bin/env python3
"""
This is an evil undocumented SPI hack that shows how to enable GUI operation
from a console application.

BUNDLES ARE RECOMMENDED, USE THIS AT YOUR OWN RISK!!
"""
import os
import sys

import objc
from Foundation import NSBundle, NSObject


def S(*args):
    return b"".join(args)


OSErr = objc._C_SHT
OUTPSN = b"o^{ProcessSerialNumber=LL}"
INPSN = b"n^{ProcessSerialNumber=LL}"

FUNCTIONS = [
    # These two are public API
    ("GetCurrentProcess", S(OSErr, OUTPSN)),
    ("SetFrontProcess", S(OSErr, INPSN)),
    # This is undocumented SPI
    ("CPSSetProcessName", S(OSErr, INPSN, objc._C_CHARPTR)),
    ("CPSEnableForegroundOperation", S(OSErr, INPSN)),
]


def WMEnable(name="Python"):
    if not isinstance(name, bytes):
        name = name.encode("utf8")
    mainBundle = NSBundle.mainBundle()
    bPath = os.path.split(os.path.split(os.path.split(sys.executable)[0])[0])[0]
    if mainBundle.bundlePath() == bPath:
        return True
    bndl = NSBundle.bundleWithPath_(
        objc.pathForFramework(
            "/System/Library/Frameworks/ApplicationServices.framework"
        )
    )
    if bndl is None:
        print("ApplicationServices missing", file=sys.stderr)
        return False
    d = {}
    objc.loadBundleFunctions(bndl, d, FUNCTIONS)
    for fn, _sig in FUNCTIONS:
        if fn not in d:
            print("Missing", fn, file=sys.stderr)
            return False
    err, psn = d["GetCurrentProcess"](None)
    if err:
        print("GetCurrentProcess", (err, psn), file=sys.stderr)
        return False
    err = d["CPSSetProcessName"](psn, name)
    if err:
        print("CPSSetProcessName", (err, psn), file=sys.stderr)
        return False
    err = d["CPSEnableForegroundOperation"](psn)
    if err:
        print("CPSEnableForegroundOperation", (err, psn), file=sys.stderr)
        return False
    err = d["SetFrontProcess"](psn)
    if err:
        print("SetFrontProcess", (err, psn), file=sys.stderr)
        return False
    return True


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        AppKit.NSRunAlertPanel("WM Enabled", "WM was enabled!", None, None, None)
        AppKit.NSApp().terminate_(self)


if __name__ == "__main__":
    if WMEnable(os.path.basename(os.path.splitext(sys.argv[0])[0])):
        import AppKit

        app = AppKit.NSApplication.sharedApplication()
        delegate = AppDelegate.alloc().init()
        app.setDelegate_(delegate)
        app.run()
    else:
        print("WM was not enabled")
