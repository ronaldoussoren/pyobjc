
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTMovieView (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTMovieViewMovieBinding, unicode)
        self.failUnlessIsInstance(QTMovieViewControllerVisibleBinding, unicode)
        self.failUnlessIsInstance(QTMovieViewPreservesAspectRatioBinding, unicode)
        self.failUnlessIsInstance(QTMovieViewFillColorBinding, unicode)

    def testProtocols(self):
        self.failUnlessIsInstance(protocols.QTMovieViewDelegate, objc.informal_protocol)


    def testMethods(self):
        self.failUnlessResultIsBOOL(QTMovieView.isControllerVisible)
        self.failUnlessResultIsBOOL(QTMovieView.isEditable)
        self.failUnlessResultIsBOOL(QTMovieView.preservesAspectRatio)
        self.failUnlessArgIsBOOL(QTMovieView.setControllerVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setPreservesAspectRatio_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setEditable_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setShowsResizeIndicator_, 0)

        self.failUnlessArgIsBOOL(QTMovieView.setBackButtonVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setCustomButtonVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setHotSpotButtonVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setStepButtonsVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setTranslateButtonVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setVolumeButtonVisible_, 0)
        self.failUnlessArgIsBOOL(QTMovieView.setZoomButtonsVisible_, 0)

        self.failUnlessResultIsBOOL(QTMovieView.isBackButtonVisible)
        self.failUnlessResultIsBOOL(QTMovieView.isCustomButtonVisible)
        self.failUnlessResultIsBOOL(QTMovieView.isHotSpotButtonVisible)
        self.failUnlessResultIsBOOL(QTMovieView.areStepButtonsVisible)
        self.failUnlessResultIsBOOL(QTMovieView.isTranslateButtonVisible)
        self.failUnlessResultIsBOOL(QTMovieView.isVolumeButtonVisible)
        self.failUnlessResultIsBOOL(QTMovieView.areZoomButtonsVisible)

if __name__ == "__main__":
    main()
