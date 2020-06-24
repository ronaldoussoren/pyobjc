from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTTrack(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTTrackBoundsAttribute, str)
        self.assertIsInstance(QTKit.QTTrackCreationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTTrackDimensionsAttribute, str)
        self.assertIsInstance(QTKit.QTTrackDisplayNameAttribute, str)
        self.assertIsInstance(QTKit.QTTrackEnabledAttribute, str)
        self.assertIsInstance(QTKit.QTTrackFormatSummaryAttribute, str)
        self.assertIsInstance(QTKit.QTTrackIsChapterTrackAttribute, str)
        self.assertIsInstance(QTKit.QTTrackHasApertureModeDimensionsAttribute, str)
        self.assertIsInstance(QTKit.QTTrackIDAttribute, str)
        self.assertIsInstance(QTKit.QTTrackLayerAttribute, str)
        self.assertIsInstance(QTKit.QTTrackMediaTypeAttribute, str)
        self.assertIsInstance(QTKit.QTTrackModificationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTTrackRangeAttribute, str)
        self.assertIsInstance(QTKit.QTTrackTimeScaleAttribute, str)
        self.assertIsInstance(QTKit.QTTrackUsageInMovieAttribute, str)
        self.assertIsInstance(QTKit.QTTrackUsageInPosterAttribute, str)
        self.assertIsInstance(QTKit.QTTrackUsageInPreviewAttribute, str)
        self.assertIsInstance(QTKit.QTTrackVolumeAttribute, str)

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTTrack.isEnabled)
        self.assertArgIsBOOL(QTKit.QTTrack.setEnabled_, 0)
