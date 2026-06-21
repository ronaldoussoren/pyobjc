from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit
import objc


class TestSKMutableTexture(TestCase):
    @min_os_level("10.10")
    def test_methods(self):
        self.assertArgIsBlock(
            SpriteKit.SKMutableTexture.modifyPixelDataWithBlock_,
            0,
            b"vN^v" + objc._C_NSUInteger,
        )
