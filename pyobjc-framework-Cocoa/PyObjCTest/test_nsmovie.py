import AppKit
from PyObjCTools.TestSupport import TestCase, onlyOn32Bit


class TestNSMovie(TestCase):
    @onlyOn32Bit
    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSMovie.initWithURL_byReference_, 1)
        self.assertResultIsBOOL(AppKit.NSMovie.canInitWithPasteboard_)
