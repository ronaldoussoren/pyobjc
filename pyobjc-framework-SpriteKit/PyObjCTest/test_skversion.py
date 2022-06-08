from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKVersion(TestCase):
    def testConstants(self):
        self.assertFalse(hasattr(SpriteKit, "SK_VERSION"))
