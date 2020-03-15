import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLResponse(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSURLResponseUnknownLength, -1)
