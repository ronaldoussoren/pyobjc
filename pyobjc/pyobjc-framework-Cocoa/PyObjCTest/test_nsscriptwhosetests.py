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
        self.failUnlessEqual(NSEqualToComparison, 0)
        self.failUnlessEqual(NSLessThanOrEqualToComparison, 1)
        self.failUnlessEqual(NSLessThanComparison, 2)
        self.failUnlessEqual(NSGreaterThanOrEqualToComparison, 3)
        self.failUnlessEqual(NSGreaterThanComparison, 4)
        self.failUnlessEqual(NSBeginsWithComparison, 5)
        self.failUnlessEqual(NSEndsWithComparison, 6)
        self.failUnlessEqual(NSContainsComparison, 7)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSScriptWhoseTest.isTrue)

        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isLessThanOrEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isLessThan_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isGreaterThanOrEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isGreaterThan_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isNotEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.doesContain_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isLike_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.isCaseInsensitiveLike_)

        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsLessThanOrEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsLessThan_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsGreaterThanOrEqualTo_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingIsGreaterThan_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingBeginsWith_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingEndsWith_)
        self.failUnlessResultIsBOOL(TestNSScriptWhoseTestsHelper.scriptingContains_)

if __name__ == "__main__":
    main()

