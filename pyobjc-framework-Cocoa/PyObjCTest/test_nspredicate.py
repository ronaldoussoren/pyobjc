import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPredicate(TestCase):
    def test_simple(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == 42")
        self.assertEqual(pred.predicateFormat(), "a == 42")

    def test_format(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == %d", 99)
        self.assertEqual(pred.predicateFormat(), "a == 99")

    def test_bad_format(self):
        self.assertRaises(
            ValueError, Foundation.NSPredicate.predicateWithFormat_, "a == %d"
        )

    def test_methods(self):
        self.assertArgIsBOOL(Foundation.NSPredicate.predicateWithValue_, 0)
        self.assertResultIsBOOL(Foundation.NSPredicate.evaluateWithObject_)
        self.assertResultIsBOOL(
            Foundation.NSPredicate.evaluateWithObject_substitutionVariables_
        )

    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSPredicate.predicateWithBlock_, 0, objc._C_NSBOOL + b"@@"
        )

    @min_os_level("26.4")
    def test_methods26_4(self):
        self.assertResultIsBOOL(
            Foundation.NSPredicate.allowEvaluationWithValidator_error_
        )
        self.assertArgIsOut(
            Foundation.NSPredicate.allowEvaluationWithValidator_error_, 1
        )
