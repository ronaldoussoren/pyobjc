
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMovieView (TestCase):
    @onlyOn32Bit
    def testConstants(self):
        self.assertEqual(NSQTMovieNormalPlayback, 0)
        self.assertEqual(NSQTMovieLoopingPlayback, 1)
        self.assertEqual(NSQTMovieLoopingBackAndForthPlayback, 2)

    @onlyOn32Bit
    def testMethods(self):
        self.assertResultIsBOOL(NSMovieView.isPlaying)
        self.assertResultIsBOOL(NSMovieView.isMuted)
        self.assertArgIsBOOL(NSMovieView.setMuted_, 0)
        self.assertResultIsBOOL(NSMovieView.playsSelectionOnly)
        self.assertArgIsBOOL(NSMovieView.setPlaysSelectionOnly_, 0)
        self.assertResultIsBOOL(NSMovieView.playsEveryFrame)
        self.assertResultIsBOOL(NSMovieView.isControllerVisible)
        self.assertArgIsBOOL(NSMovieView.showController_adjustingSize_, 0)
        self.assertArgIsBOOL(NSMovieView.showController_adjustingSize_, 1)
        self.assertArgIsBOOL(NSMovieView.setEditable_, 0)
        self.assertResultIsBOOL(NSMovieView.isEditable)




if __name__ == "__main__":
    main()
