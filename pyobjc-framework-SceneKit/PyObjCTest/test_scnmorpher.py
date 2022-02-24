from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit


class TestSCNMorpher(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNMorpherCalculationMode)

    def testConstants(self):
        self.assertEqual(SceneKit.SCNMorpherCalculationModeNormalized, 0)
        self.assertEqual(SceneKit.SCNMorpherCalculationModeAdditive, 1)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNMorpher.unifiesNormals)
        self.assertArgIsBOOL(SceneKit.SCNMorpher.setUnifiesNormals_, 0)
