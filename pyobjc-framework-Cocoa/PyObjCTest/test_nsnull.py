import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSNull(TestCase):
    def testBool(self):
        v = Foundation.NSNull.null()
        self.assertFalse(v)
        self.assertIsNot(v, None)
