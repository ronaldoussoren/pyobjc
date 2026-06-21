import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSPortCoder(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSPortCoder.isBycopy)
        self.assertResultIsBOOL(Foundation.NSPortCoder.isByref)
