
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSoundHelper (NSObject):
    def sound_didFinishPlaying_(self, s, p): pass


class TestNSSound (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSSoundPboardType, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(NSSound.initWithContentsOfURL_byReference_, 1)
        self.assertArgIsBOOL(NSSound.initWithContentsOfFile_byReference_, 1)
        self.assertResultIsBOOL(NSSound.setName_)
        self.assertResultIsBOOL(NSSound.canInitWithPasteboard_)
        self.assertResultIsBOOL(NSSound.play)
        self.assertResultIsBOOL(NSSound.pause)
        self.assertResultIsBOOL(NSSound.resume)
        self.assertResultIsBOOL(NSSound.stop)
        self.assertResultIsBOOL(NSSound.isPlaying)
        self.assertResultIsBOOL(NSSound.loops)
        self.assertArgIsBOOL(NSSound.setLoops_, 0)

    def testProtocols(self):
        self.assertArgIsBOOL(TestNSSoundHelper.sound_didFinishPlaying_, 1)

if __name__ == "__main__":
    main()
