
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTrack (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTTrackBoundsAttribute, unicode)
        self.failUnlessIsInstance(QTTrackCreationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTTrackDimensionsAttribute, unicode)
        self.failUnlessIsInstance(QTTrackDisplayNameAttribute, unicode)
        self.failUnlessIsInstance(QTTrackEnabledAttribute, unicode)
        self.failUnlessIsInstance(QTTrackFormatSummaryAttribute, unicode)
        self.failUnlessIsInstance(QTTrackIsChapterTrackAttribute, unicode)
        self.failUnlessIsInstance(QTTrackHasApertureModeDimensionsAttribute, unicode)
        self.failUnlessIsInstance(QTTrackIDAttribute, unicode)
        self.failUnlessIsInstance(QTTrackLayerAttribute, unicode)
        self.failUnlessIsInstance(QTTrackMediaTypeAttribute, unicode)
        self.failUnlessIsInstance(QTTrackModificationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTTrackRangeAttribute, unicode)
        self.failUnlessIsInstance(QTTrackTimeScaleAttribute, unicode)
        self.failUnlessIsInstance(QTTrackUsageInMovieAttribute, unicode)
        self.failUnlessIsInstance(QTTrackUsageInPosterAttribute, unicode)
        self.failUnlessIsInstance(QTTrackUsageInPreviewAttribute, unicode)
        self.failUnlessIsInstance(QTTrackVolumeAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTTrack.isEnabled)
        self.failUnlessArgIsBOOL(QTTrack.setEnabled_, 0)

if __name__ == "__main__":
    main()
