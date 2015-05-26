import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKMutableTexture (TestCase):

        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBlock(SpriteKit.SKMutableTexture.modifyPixelDataWithBlock_, 0,
                    b'vN^v' + objc._C_NSUInteger )

if __name__ == "__main__":
    main()
