#!/usr/bin/env python
"""
This script shows how to use PyObjCTools.Debugging to show a dump of all
(Cocoa) exceptions (handled and unhandled).
"""
from PyObjCTools import AppHelper
from PyObjCTools import Debugging
from Foundation import NSTimer, NSObject, NSInvocation

class FooTester(NSObject):
    def doBadThingsNow_(self, aTimer):
        raise ValueError, "doing bad things"

foo = FooTester.alloc().init()
NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
    1.0, foo, 'doBadThingsNow:', None, False
)
# we need to catch everything, because NSTimer handles this one
Debugging.installVerboseExceptionHandler()
AppHelper.runConsoleEventLoop()
