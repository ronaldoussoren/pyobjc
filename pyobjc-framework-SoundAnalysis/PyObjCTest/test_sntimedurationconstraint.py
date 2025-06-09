import SoundAnalysis
import CoreMedia
from PyObjCTools.TestSupport import TestCase


class TestSNTimeDurationConstraint(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SoundAnalysis.SNTimeDurationConstraintType)

    def test_constants(self):
        self.assertEqual(SoundAnalysis.SNTimeDurationConstraintTypeEnumerated, 1)
        self.assertEqual(SoundAnalysis.SNTimeDurationConstraintTypeRange, 2)

    def test_methods(self):
        self.assertResultHasType(
            SoundAnalysis.SNTimeDurationConstraint.durationRange,
            CoreMedia.CMTimeRange.__typestr__,
        )
        self.assertArgHasType(
            SoundAnalysis.SNTimeDurationConstraint.initWithDurationRange_,
            0,
            CoreMedia.CMTimeRange.__typestr__,
        )
