from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKRegion(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(SpriteKit.SKRegion.containsPoint_)
