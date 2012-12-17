#!/usr/bin/env
"""
This is a simple tool that exercises the some callback functions in the
SystemConfiguration framework.

In an ideal world this would be a nice GUI.

Usage:
    python callbacks.py
"""
from Cocoa import *
from SystemConfiguration import *

import signal

def sigint(*args):
    print "SIGINT: bailing out"
    loop = CFRunLoopGetCurrent()
    CFRunLoopStop(loop)


def dynamicStoreChanged(store, changedKeys, info):
    print "Dynamic Store: keys changed", changedKeys

def prefsChanged(prefs, notificationType, info):
    print "Prefs changed, type:", notificationType



def main():

    # Setup a dynamic store controller that monitors all keys:
    store = SCDynamicStoreCreate(None, "demo.controller",
                dynamicStoreChanged, None)
    SCDynamicStoreSetNotificationKeys(store, None, [ '.*' ])
    source = SCDynamicStoreCreateRunLoopSource(None, store, 0)

    # Setup a preferences controller
    prefs = SCPreferencesCreate(None, "demo.prefs", None)
    SCPreferencesSetCallback(prefs, prefsChanged, None)


    # Set up a run loop and add all controllers to that.
    loop = CFRunLoopGetCurrent()
    CFRunLoopAddSource(loop, source, kCFRunLoopCommonModes)
    SCPreferencesScheduleWithRunLoop(prefs, loop, kCFRunLoopCommonModes)

    signal.signal(signal.SIGINT, sigint)
    CFRunLoopRun()


if __name__ == "__main__":
    main()
