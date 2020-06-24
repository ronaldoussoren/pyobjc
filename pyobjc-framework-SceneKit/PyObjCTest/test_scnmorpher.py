import sys

from PyObjCTools.TestSupport import TestCase, min_os_level, os_release, os_level_key

if os_level_key(os_release()) < os_level_key("10.12") or sys.maxsize >= 2 ** 32:

    import SceneKit

    class TestSCNMorpher(TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNMorpherCalculationModeNormalized, 0)
            self.assertEqual(SceneKit.SCNMorpherCalculationModeAdditive, 1)

        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertResultIsBOOL(SceneKit.SCNMorpher.unifiesNormals)
            self.assertArgIsBOOL(SceneKit.SCNMorpher.setUnifiesNormals_, 0)
