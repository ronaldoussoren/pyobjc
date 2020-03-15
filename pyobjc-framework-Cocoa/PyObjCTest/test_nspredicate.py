import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPredicate(TestCase):
    def testSimple(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == 42")
        self.assertEqual(pred.predicateFormat(), "a == 42")

    def testFormat(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == %d", 99)
        self.assertEqual(pred.predicateFormat(), "a == 99")

    def testBadFormat(self):
        self.assertRaises(
            ValueError, Foundation.NSPredicate.predicateWithFormat_, "a == %d"
        )

    def testMethods(self):
        self.assertArgIsBOOL(Foundation.NSPredicate.predicateWithValue_, 0)
        self.assertResultIsBOOL(Foundation.NSPredicate.evaluateWithObject_)
        self.assertResultIsBOOL(
            Foundation.NSPredicate.evaluateWithObject_substitutionVariables_
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSPredicate.predicateWithBlock_, 0, objc._C_NSBOOL + b"@@"
        )
