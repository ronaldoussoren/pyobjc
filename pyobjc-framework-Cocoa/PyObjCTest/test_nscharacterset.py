import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSCharacterSet(TestCase):
    def test_constants(self):
        self.assertEqual(Foundation.NSOpenStepUnicodeReservedBase, 0xF400)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSCharacterSet.characterIsMember_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.longCharacterIsMember_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.isSupersetOfSet_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.hasMemberInPlane_)
