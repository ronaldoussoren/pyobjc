from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSScriptWhoseTestsHelper (NSObject):
    def isEqualTo_(self, o): return 1
    def isLessThanOrEqualTo_(self, o): return 1
    def isLessThan_(self, o): return 1
    def isGreaterThanOrEqualTo_(self, o): return 1
    def isGreaterThan_(self, o): return 1
    def isNotEqualTo_(self, o): return 1
    def doesContain_(self, o): return 1
    def isLike_(self, o): return 1
    def isCaseInsensitiveLike_(self, o): return 1

    def scriptingIsEqualTo_(self, o): return 1
    def scriptingIsLessThanOrEqualTo_(self, o): return 1
    def scriptingIsLessThan_(self, o): return 1
    def scriptingIsGreaterThanOrEqualTo_(self, o): return 1
    def scriptingIsGreaterThan_(self, o): return 1
    def scriptingBeginsWith_(self, o): return 1
    def scriptingEndsWith_(self, o): return 1
    def scriptingContains_(self, o): return 1

class TestNSScriptWhoseTests (TestCase):

    def testConstants(self):
        self.assertEqual(NSEqualToComparison, 0)
        self.assertEqual(NSLessThanOrEqualToComparison, 1)
        self.assertEqual(NSLessThanComparison, 2)
        self.assertEqual(NSGreaterThanOrEqualToComparison, 3)
        self.assertEqual(NSGreaterThanComparison, 4)
        self.assertEqual(NSBeginsWithComparison, 5)
        self.assertEqual(NSEndsWithComparison, 6)
        self.assertEqual(NSContainsComparison, 7)


    def testMethods(self):
        self.assertResultIsBOOL(NSScriptWhoseTest.isTrue)

        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isLessThanOrEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isLessThan_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isGreaterThanOrEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isGreaterThan_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isNotEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.doesContain_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isLike_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.isCaseInsensitiveLike_)

        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsLessThanOrEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsLessThan_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsGreaterThanOrEqualTo_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsGreaterThan_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingBeginsWith_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingEndsWith_)
        self.assertResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingContains_)

if __name__ == "__main__":
    main()
