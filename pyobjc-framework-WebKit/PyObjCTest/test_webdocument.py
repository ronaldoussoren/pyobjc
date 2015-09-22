
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebDocumentHelper (NSObject):
    def setNeedsLayout_(self, v): pass

    def searchFor_direction_caseSensitive_wrap_(self, a, b, c, d): return 1

    def supportsTextEncoding(self): return 1
    def canProvideDocumentSource(self): return 1


class TestWebDocument (TestCase):
    def testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("WebDocumentView"), objc.formal_protocol)
        self.assertIsInstance(objc.protocolNamed("WebDocumentSearching"), objc.formal_protocol)
        self.assertIsInstance(objc.protocolNamed("WebDocumentText"), objc.formal_protocol)
        self.assertIsInstance(objc.protocolNamed("WebDocumentRepresentation"), objc.formal_protocol)

    def testMethods(self):
        self.assertArgIsBOOL(TestWebDocumentHelper.setNeedsLayout_, 0)

        self.assertResultIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_)
        self.assertArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 1)
        self.assertArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 2)
        self.assertArgIsBOOL(TestWebDocumentHelper.searchFor_direction_caseSensitive_wrap_, 3)

        self.assertResultIsBOOL(TestWebDocumentHelper.supportsTextEncoding)
        self.assertResultIsBOOL(TestWebDocumentHelper.canProvideDocumentSource)

if __name__ == "__main__":
    main()
