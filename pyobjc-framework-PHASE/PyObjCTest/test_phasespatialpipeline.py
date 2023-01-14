from PyObjCTools.TestSupport import TestCase

import PHASE


class TestPHASESpatialPipeline(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(PHASE.PHASESpatialCategory, str)
        self.assertIsInstance(PHASE.PHASESpatialCategoryDirectPathTransmission, str)
        self.assertIsInstance(PHASE.PHASESpatialCategoryEarlyReflections, str)
        self.assertIsInstance(PHASE.PHASESpatialCategoryLateReverb, str)

        self.assertIsEnumType(PHASE.PHASESpatialPipelineFlags)
        self.assertEqual(PHASE.PHASESpatialPipelineFlagDirectPathTransmission, 1 << 0)
        self.assertEqual(PHASE.PHASESpatialPipelineFlagEarlyReflections, 1 << 1)
        self.assertEqual(PHASE.PHASESpatialPipelineFlagLateReverb, 1 << 2)
