from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit


class TestSCNMorpher(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SceneKit.SCNMorpherCalculationMode)
        self.assertEqual(SceneKit.SCNMorpherCalculationModeNormalized, 0)
        self.assertEqual(SceneKit.SCNMorpherCalculationModeAdditive, 1)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNMorpher.unifiesNormals)
        self.assertArgIsBOOL(SceneKit.SCNMorpher.setUnifiesNormals_, 0)
