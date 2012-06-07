
from PyObjCTools.TestSupport import *
from QTKit import *

try:
    unicode
except NameError:
    unicode = str

class TestQTMovieView (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTMovieViewMovieBinding, unicode)
        self.assertIsInstance(QTMovieViewControllerVisibleBinding, unicode)
        self.assertIsInstance(QTMovieViewPreservesAspectRatioBinding, unicode)
        self.assertIsInstance(QTMovieViewFillColorBinding, unicode)

    def testProtocols(self):
        self.assertIsInstance(protocols.QTMovieView_Delegate, objc.informal_protocol)


    def testMethods(self):
        self.assertResultIsBOOL(QTMovieView.isControllerVisible)
        self.assertResultIsBOOL(QTMovieView.isEditable)
        self.assertResultIsBOOL(QTMovieView.preservesAspectRatio)
        self.assertArgIsBOOL(QTMovieView.setControllerVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setPreservesAspectRatio_, 0)
        self.assertArgIsBOOL(QTMovieView.setEditable_, 0)
        self.assertArgIsBOOL(QTMovieView.setShowsResizeIndicator_, 0)

        self.assertArgIsBOOL(QTMovieView.setBackButtonVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setCustomButtonVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setHotSpotButtonVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setStepButtonsVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setTranslateButtonVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setVolumeButtonVisible_, 0)
        self.assertArgIsBOOL(QTMovieView.setZoomButtonsVisible_, 0)

        self.assertResultIsBOOL(QTMovieView.isBackButtonVisible)
        self.assertResultIsBOOL(QTMovieView.isCustomButtonVisible)
        self.assertResultIsBOOL(QTMovieView.isHotSpotButtonVisible)
        self.assertResultIsBOOL(QTMovieView.areStepButtonsVisible)
        self.assertResultIsBOOL(QTMovieView.isTranslateButtonVisible)
        self.assertResultIsBOOL(QTMovieView.isVolumeButtonVisible)
        self.assertResultIsBOOL(QTMovieView.areZoomButtonsVisible)

if __name__ == "__main__":
    main()
