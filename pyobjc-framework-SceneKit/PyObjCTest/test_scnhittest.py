from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNAction(TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNHitTestSearchModeClosest, 0)
        self.assertEqual(SceneKit.SCNHitTestSearchModeAll, 1)
        self.assertEqual(SceneKit.SCNHitTestSearchModeAny, 2)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(SceneKit.SCNHitTestOptionSearchMode, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(SceneKit.SCNHitTestOptionIgnoreLightArea, str)
