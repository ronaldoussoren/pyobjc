import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLResponse(TestCase):
    def test_constants(self):
        self.assertEqual(Foundation.NSURLResponseUnknownLength, -1)
