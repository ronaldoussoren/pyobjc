from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPredicate (TestCase):
    def testSimple(self):
        pred = NSPredicate.predicateWithFormat_("a == 42")
        self.assertEquals(pred.predicateFormat(), "a == 42")

    def testFormat(self):
        pred = NSPredicate.predicateWithFormat_("a == %d", 99)
        self.assertEquals(pred.predicateFormat(), "a == 99")

    def testBadFormat(self):
        self.assertRaises(ValueError, NSPredicate.predicateWithFormat_, "a == %d")

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSPredicate.predicateWithValue_, 0)
        self.failUnlessResultIsBOOL(NSPredicate.evaluateWithObject_)
        self.failUnlessResultIsBOOL(NSPredicate.evaluateWithObject_substitutionVariables_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBlock(NSPredicate.predicateWithBlock_, 0, objc._C_NSBOOL + '@@')


if __name__ == "__main__":
    main()
