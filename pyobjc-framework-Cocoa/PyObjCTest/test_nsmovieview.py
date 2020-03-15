import AppKit
from PyObjCTools.TestSupport import TestCase, onlyOn32Bit


class TestNSMovieView(TestCase):
    @onlyOn32Bit
    def testConstants(self):
        self.assertEqual(AppKit.NSQTMovieNormalPlayback, 0)
        self.assertEqual(AppKit.NSQTMovieLoopingPlayback, 1)
        self.assertEqual(AppKit.NSQTMovieLoopingBackAndForthPlayback, 2)

    @onlyOn32Bit
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMovieView.isPlaying)
        self.assertResultIsBOOL(AppKit.NSMovieView.isMuted)
        self.assertArgIsBOOL(AppKit.NSMovieView.setMuted_, 0)
        self.assertResultIsBOOL(AppKit.NSMovieView.playsSelectionOnly)
        self.assertArgIsBOOL(AppKit.NSMovieView.setPlaysSelectionOnly_, 0)
        self.assertResultIsBOOL(AppKit.NSMovieView.playsEveryFrame)
        self.assertResultIsBOOL(AppKit.NSMovieView.isControllerVisible)
        self.assertArgIsBOOL(AppKit.NSMovieView.showController_adjustingSize_, 0)
        self.assertArgIsBOOL(AppKit.NSMovieView.showController_adjustingSize_, 1)
        self.assertArgIsBOOL(AppKit.NSMovieView.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSMovieView.isEditable)
