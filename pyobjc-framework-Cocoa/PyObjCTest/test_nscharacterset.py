import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSCharacterSet(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSOpenStepUnicodeReservedBase, 0xF400)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSCharacterSet.characterIsMember_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.longCharacterIsMember_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.isSupersetOfSet_)
        self.assertResultIsBOOL(Foundation.NSCharacterSet.hasMemberInPlane_)
