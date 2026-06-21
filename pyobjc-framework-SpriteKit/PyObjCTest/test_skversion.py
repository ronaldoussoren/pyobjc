from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKVersion(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(SpriteKit, "SK_VERSION"))
