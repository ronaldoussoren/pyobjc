import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSoundHelper(AppKit.NSObject):
    def sound_didFinishPlaying_(self, s, p):
        pass


class TestNSSound(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSSoundPboardType, str)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSSound.initWithContentsOfURL_byReference_, 1)
        self.assertArgIsBOOL(AppKit.NSSound.initWithContentsOfFile_byReference_, 1)
        self.assertResultIsBOOL(AppKit.NSSound.setName_)
        self.assertResultIsBOOL(AppKit.NSSound.canInitWithPasteboard_)
        self.assertResultIsBOOL(AppKit.NSSound.play)
        self.assertResultIsBOOL(AppKit.NSSound.pause)
        self.assertResultIsBOOL(AppKit.NSSound.resume)
        self.assertResultIsBOOL(AppKit.NSSound.stop)
        self.assertResultIsBOOL(AppKit.NSSound.isPlaying)
        self.assertResultIsBOOL(AppKit.NSSound.loops)
        self.assertArgIsBOOL(AppKit.NSSound.setLoops_, 0)

    @min_os_level("10.10")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSSoundDelegate")

    def testProtocols(self):
        self.assertArgIsBOOL(TestNSSoundHelper.sound_didFinishPlaying_, 1)
