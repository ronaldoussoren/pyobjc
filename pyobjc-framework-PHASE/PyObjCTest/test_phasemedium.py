from PyObjCTools.TestSupport import TestCase, fourcc

import PHASE


class TestPHASEMedium(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PHASE.PHASEMediumPreset)
        self.assertEqual(PHASE.PHASEMediumPresetAir, fourcc(b"mdAr"))
