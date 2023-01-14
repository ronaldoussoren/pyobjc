from PyObjCTools.TestSupport import TestCase, fourcc

import PHASE


class TestPHASEMaterial(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PHASE.PHASEMaterialPreset)
        self.assertEqual(PHASE.PHASEMaterialPresetCardboard, fourcc(b"mCrd"))
        self.assertEqual(PHASE.PHASEMaterialPresetGlass, fourcc(b"mGls"))
        self.assertEqual(PHASE.PHASEMaterialPresetBrick, fourcc(b"mBrk"))
        self.assertEqual(PHASE.PHASEMaterialPresetConcrete, fourcc(b"mCcr"))
        self.assertEqual(PHASE.PHASEMaterialPresetDrywall, fourcc(b"mDrw"))
        self.assertEqual(PHASE.PHASEMaterialPresetWood, fourcc(b"mWud"))
