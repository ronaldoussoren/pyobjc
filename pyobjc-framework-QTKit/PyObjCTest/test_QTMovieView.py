from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTMovieView(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTMovieViewMovieBinding, str)
        self.assertIsInstance(QTKit.QTMovieViewControllerVisibleBinding, str)
        self.assertIsInstance(QTKit.QTMovieViewPreservesAspectRatioBinding, str)
        self.assertIsInstance(QTKit.QTMovieViewFillColorBinding, str)

    # def testProtocols(self):
    # self.assertIsInstance(protocols.QTMovieView_Delegate, objc.informal_protocol)

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTMovieView.isControllerVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.isEditable)
        self.assertResultIsBOOL(QTKit.QTMovieView.preservesAspectRatio)
        self.assertArgIsBOOL(QTKit.QTMovieView.setControllerVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setPreservesAspectRatio_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setEditable_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setShowsResizeIndicator_, 0)

        self.assertArgIsBOOL(QTKit.QTMovieView.setBackButtonVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setCustomButtonVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setHotSpotButtonVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setStepButtonsVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setTranslateButtonVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setVolumeButtonVisible_, 0)
        self.assertArgIsBOOL(QTKit.QTMovieView.setZoomButtonsVisible_, 0)

        self.assertResultIsBOOL(QTKit.QTMovieView.isBackButtonVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.isCustomButtonVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.isHotSpotButtonVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.areStepButtonsVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.isTranslateButtonVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.isVolumeButtonVisible)
        self.assertResultIsBOOL(QTKit.QTMovieView.areZoomButtonsVisible)
