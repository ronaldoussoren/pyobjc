from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize >= 2 ** 32:
    import SceneKit

    class TestSCNAction(TestCase):
        def testConstants(self):
            self.assertEqual(SceneKit.SCNHitTestSearchModeClosest, 0)
            self.assertEqual(SceneKit.SCNHitTestSearchModeAll, 1)
            self.assertEqual(SceneKit.SCNHitTestSearchModeAny, 2)

        @min_os_level("10.13")
        def testConstants10_13(self):
            self.assertIsInstance(SceneKit.SCNHitTestOptionSearchMode, unicode)

        @min_os_level("10.15")
        def testConstants10_15(self):
            self.assertIsInstance(SceneKit.SCNHitTestOptionIgnoreLightArea, unicode)


if __name__ == "__main__":
    main()
