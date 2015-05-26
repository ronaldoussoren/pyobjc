import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKScene (TestCase):
        @min_os_level('10.9')
        def testConstants(self):
            self.assertEqual(SpriteKit.SKSceneScaleModeFill, 0)
            self.assertEqual(SpriteKit.SKSceneScaleModeAspectFill, 1)
            self.assertEqual(SpriteKit.SKSceneScaleModeAspectFit, 2)
            self.assertEqual(SpriteKit.SKSceneScaleModeResizeFill, 3)

        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('SKSceneDelegate')

if __name__ == "__main__":
    main()
