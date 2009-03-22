
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSoundHelper (NSObject):
    def sound_didFinishPlaying_(self, s, p): pass


class TestNSSound (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSSoundPboardType, unicode)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSSound.initWithContentsOfURL_byReference_, 1)
        self.failUnlessArgIsBOOL(NSSound.initWithContentsOfFile_byReference_, 1)
        self.failUnlessResultIsBOOL(NSSound.setName_)
        self.failUnlessResultIsBOOL(NSSound.canInitWithPasteboard_)
        self.failUnlessResultIsBOOL(NSSound.play)
        self.failUnlessResultIsBOOL(NSSound.pause)
        self.failUnlessResultIsBOOL(NSSound.resume)
        self.failUnlessResultIsBOOL(NSSound.stop)
        self.failUnlessResultIsBOOL(NSSound.isPlaying)
        self.failUnlessResultIsBOOL(NSSound.loops)
        self.failUnlessArgIsBOOL(NSSound.setLoops_, 0)

    def testProtocols(self):
        self.failUnlessArgIsBOOL(TestNSSoundHelper.sound_didFinishPlaying_, 1)

if __name__ == "__main__":
    main()
