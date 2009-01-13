from PyObjCTools.TestSupport import *
import Foundation

class TestNSPredicate (TestCase):
    def testSimple(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == 42")
        self.assertEquals(pred.predicateFormat(), "a == 42")

    def testFormat(self):
        pred = Foundation.NSPredicate.predicateWithFormat_("a == %d", 99)
        self.assertEquals(pred.predicateFormat(), "a == 99")

    def testBadFormat(self):
        self.assertRaises(ValueError, Foundation.NSPredicate.predicateWithFormat_, "a == %d")

if __name__ == "__main__":
    main()
