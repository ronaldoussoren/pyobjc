#!/usr/bin/env python
"""
This script shows how to use PyObjCTools.Debugging to show a dump of all
(Cocoa) exceptions (handled and unhandled).
"""
from Foundation import NSArray, NSObject, NSTimer
from PyObjCTools import AppHelper, Debugging


class FooTester(NSObject):
    def doCBad_(self, aTimer):
        NSArray([1])[5]

    def doBadThingsNow_(self, aTimer):
        AppHelper.stopEventLoop()
        raise ValueError("doing bad things")


foo = FooTester.alloc().init()
NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
    0.5, foo, "doBadThingsNow:", None, False
)
NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
    0.0, foo, "doCBad:", None, False
)
# we need to catch everything, because NSTimer handles this one
Debugging.installVerboseExceptionHandler()
AppHelper.runConsoleEventLoop()
