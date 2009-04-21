
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebDocumentHelper (NSObject):
    def setNeedsLayout_(self, v): pass

    def searchFor_direction_caseSensitive_wrap_(self, a, b, c, d): return 1

    def supportsTextEncoding(self): return 1
    def canProvideDocumentSource(self): return 1


class TestWebDocument (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(TestWebDocumentHelper.setNeedsLayout_, 0)

        self.failUnlessResultIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_)
        self.failUnlessArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 1)
        self.failUnlessArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 2)
        self.failUnlessArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 3)

        self.failUnlessResultIsBOOL(TestWebDocumentHelper.supportsTextEncoding)
        self.failUnlessResultIsBOOL(TestWebDocumentHelper.canProvideDocumentSource)

if __name__ == "__main__":
    main()
