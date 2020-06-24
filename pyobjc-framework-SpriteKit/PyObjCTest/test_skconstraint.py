from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKConstraint(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBOOL(SpriteKit.SKConstraint.setEnabled_, 0)
        self.assertResultIsBOOL(SpriteKit.SKConstraint.enabled)
