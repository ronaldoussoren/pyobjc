
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTTrack (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTTrackBoundsAttribute, unicode)
        self.assertIsInstance(QTTrackCreationTimeAttribute, unicode)
        self.assertIsInstance(QTTrackDimensionsAttribute, unicode)
        self.assertIsInstance(QTTrackDisplayNameAttribute, unicode)
        self.assertIsInstance(QTTrackEnabledAttribute, unicode)
        self.assertIsInstance(QTTrackFormatSummaryAttribute, unicode)
        self.assertIsInstance(QTTrackIsChapterTrackAttribute, unicode)
        self.assertIsInstance(QTTrackHasApertureModeDimensionsAttribute, unicode)
        self.assertIsInstance(QTTrackIDAttribute, unicode)
        self.assertIsInstance(QTTrackLayerAttribute, unicode)
        self.assertIsInstance(QTTrackMediaTypeAttribute, unicode)
        self.assertIsInstance(QTTrackModificationTimeAttribute, unicode)
        self.assertIsInstance(QTTrackRangeAttribute, unicode)
        self.assertIsInstance(QTTrackTimeScaleAttribute, unicode)
        self.assertIsInstance(QTTrackUsageInMovieAttribute, unicode)
        self.assertIsInstance(QTTrackUsageInPosterAttribute, unicode)
        self.assertIsInstance(QTTrackUsageInPreviewAttribute, unicode)
        self.assertIsInstance(QTTrackVolumeAttribute, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTTrack.isEnabled)
        self.assertArgIsBOOL(QTTrack.setEnabled_, 0)

if __name__ == "__main__":
    main()
