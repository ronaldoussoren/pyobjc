
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMNodeFilterHelper (NSObject):
    def acceptNode_(self, n): return 1

class TestDOMNodeFilter (TestCase):
    def testMethods(self):
        self.failUnlessResultHasType(TestDOMNodeFilterHelper.acceptNode_, objc._C_SHT)

    def testConstants(self):
        self.failUnlessEqual(DOM_FILTER_ACCEPT, 1)
        self.failUnlessEqual(DOM_FILTER_REJECT, 2)
        self.failUnlessEqual(DOM_FILTER_SKIP, 3)
        self.failUnlessEqual(DOM_SHOW_ALL, cast_int(0xFFFFFFFF))
        self.failUnlessEqual(DOM_SHOW_ELEMENT, 0x00000001)
        self.failUnlessEqual(DOM_SHOW_ATTRIBUTE, 0x00000002)
        self.failUnlessEqual(DOM_SHOW_TEXT, 0x00000004)
        self.failUnlessEqual(DOM_SHOW_CDATA_SECTION, 0x00000008)
        self.failUnlessEqual(DOM_SHOW_ENTITY_REFERENCE, 0x00000010)
        self.failUnlessEqual(DOM_SHOW_ENTITY, 0x00000020)
        self.failUnlessEqual(DOM_SHOW_PROCESSING_INSTRUCTION, 0x00000040)
        self.failUnlessEqual(DOM_SHOW_COMMENT, 0x00000080)
        self.failUnlessEqual(DOM_SHOW_DOCUMENT, 0x00000100)
        self.failUnlessEqual(DOM_SHOW_DOCUMENT_TYPE, 0x00000200)
        self.failUnlessEqual(DOM_SHOW_DOCUMENT_FRAGMENT, 0x00000400)
        self.failUnlessEqual(DOM_SHOW_NOTATION, 0x00000800)

if __name__ == "__main__":
    main()
