from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    class TestSCNMaterialProperty (TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNFilterModeNone, 0)
            self.assertEqual(SceneKit.SCNFilterModeNearest, 1)
            self.assertEqual(SceneKit.SCNFilterModeLinear, 2)

            self.assertEqual(SceneKit.SCNWrapModeClamp, 1)
            self.assertEqual(SceneKit.SCNWrapModeRepeat, 2)
            self.assertEqual(SceneKit.SCNWrapModeClampToBorder, 3)
            self.assertEqual(SceneKit.SCNWrapModeMirror, 4)


if __name__ == "__main__":
    main()
