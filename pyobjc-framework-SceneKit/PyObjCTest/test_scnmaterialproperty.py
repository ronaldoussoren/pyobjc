from PyObjCTools.TestSupport import TestCase


import SceneKit


class TestSCNMaterialProperty(TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNFilterModeNone, 0)
        self.assertEqual(SceneKit.SCNFilterModeNearest, 1)
        self.assertEqual(SceneKit.SCNFilterModeLinear, 2)

        self.assertEqual(SceneKit.SCNWrapModeClamp, 1)
        self.assertEqual(SceneKit.SCNWrapModeRepeat, 2)
        self.assertEqual(SceneKit.SCNWrapModeClampToBorder, 3)
        self.assertEqual(SceneKit.SCNWrapModeMirror, 4)
