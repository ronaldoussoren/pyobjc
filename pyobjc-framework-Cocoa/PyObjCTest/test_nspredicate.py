from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPredicate (TestCase):
    def testSimple(self):
        pred = NSPredicate.predicateWithFormat_("a == 42")
        self.assertEqual(pred.predicateFormat(), "a == 42")

    def testFormat(self):
        pred = NSPredicate.predicateWithFormat_("a == %d", 99)
        self.assertEqual(pred.predicateFormat(), "a == 99")

    def testBadFormat(self):
        self.assertRaises(ValueError, NSPredicate.predicateWithFormat_, "a == %d")

    def testMethods(self):
        self.assertArgIsBOOL(NSPredicate.predicateWithValue_, 0)
        self.assertResultIsBOOL(NSPredicate.evaluateWithObject_)
        self.assertResultIsBOOL(NSPredicate.evaluateWithObject_substitutionVariables_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSPredicate.predicateWithBlock_, 0, objc._C_NSBOOL + b'@@')


if __name__ == "__main__":
    main()
