import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKAttribute (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(SpriteKit.SKAttributeTypeNone, 0)
            self.assertEqual(SpriteKit.SKAttributeTypeFloat, 1)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat2, 2)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat3, 3)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat4, 4)
            self.assertEqual(SpriteKit.SKAttributeTypeHalfFloat, 5)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat2, 6)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat3, 7)
            self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat4, 8)


if __name__ == "__main__":
    main()
