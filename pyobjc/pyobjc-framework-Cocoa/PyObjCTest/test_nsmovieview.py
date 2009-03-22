
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovieView (TestCase):
    @onlyOn32Bit
    def testConstants(self):
        self.failUnlessEqual(NSQTMovieNormalPlayback, 0)
        self.failUnlessEqual(NSQTMovieLoopingPlayback, 1)
        self.failUnlessEqual(NSQTMovieLoopingBackAndForthPlayback, 2)

    @onlyOn32Bit
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMovieView.isPlaying)
        self.failUnlessResultIsBOOL(NSMovieView.isMuted)
        self.failUnlessArgIsBOOL(NSMovieView.setMuted_, 0)
        self.failUnlessResultIsBOOL(NSMovieView.playsSelectionOnly)
        self.failUnlessArgIsBOOL(NSMovieView.setPlaysSelectionOnly_, 0)
        self.failUnlessResultIsBOOL(NSMovieView.playsEveryFrame)
        self.failUnlessResultIsBOOL(NSMovieView.isControllerVisible)
        self.failUnlessArgIsBOOL(NSMovieView.showController_adjustingSize_, 0)
        self.failUnlessArgIsBOOL(NSMovieView.showController_adjustingSize_, 1)
        self.failUnlessArgIsBOOL(NSMovieView.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSMovieView.isEditable)




if __name__ == "__main__":
    main()
