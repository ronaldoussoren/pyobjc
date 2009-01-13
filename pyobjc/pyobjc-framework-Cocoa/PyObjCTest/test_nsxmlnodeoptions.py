from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSXMLNodeOptions (TestCase):
    def testConstants(self):
        self.assertEquals(NSXMLNodeOptionsNone, 0)
        self.assertEquals(NSXMLNodeIsCDATA, 1 << 0)
        self.assertEquals(NSXMLNodeExpandEmptyElement, 1 << 1)
        self.assertEquals(NSXMLNodeCompactEmptyElement,  1 << 2)
        self.assertEquals(NSXMLNodeUseSingleQuotes, 1 << 3)
        self.assertEquals(NSXMLNodeUseDoubleQuotes, 1 << 4)
        self.assertEquals(NSXMLDocumentTidyHTML, 1 << 9)
        self.assertEquals(NSXMLDocumentTidyXML, 1 << 10)
        self.assertEquals(NSXMLDocumentValidate, 1 << 13)
        self.assertEquals(NSXMLDocumentXInclude, 1 << 16)
        self.assertEquals(NSXMLNodePrettyPrint, 1 << 17)
        self.assertEquals(NSXMLDocumentIncludeContentTypeDeclaration, 1 << 18)
        self.assertEquals(NSXMLNodePreserveNamespaceOrder, 1 << 20)
        self.assertEquals(NSXMLNodePreserveAttributeOrder, 1 << 21)
        self.assertEquals(NSXMLNodePreserveEntities, 1 << 22)
        self.assertEquals(NSXMLNodePreservePrefixes, 1 << 23)
        self.assertEquals(NSXMLNodePreserveCDATA, 1 << 24)
        self.assertEquals(NSXMLNodePreserveWhitespace, 1 << 25)
        self.assertEquals(NSXMLNodePreserveDTD, 1 << 26)
        self.assertEquals(NSXMLNodePreserveCharacterReferences, 1 << 27)
        self.assertEquals(NSXMLNodePreserveEmptyElements, (
            NSXMLNodeExpandEmptyElement | NSXMLNodeCompactEmptyElement))
        self.assertEquals(NSXMLNodePreserveQuotes, (NSXMLNodeUseSingleQuotes | NSXMLNodeUseDoubleQuotes))
        self.assertEquals(NSXMLNodePreserveAll & 0xFFFFFFFF, 0xFFFFFFFF & (
            NSXMLNodePreserveNamespaceOrder |
            NSXMLNodePreserveAttributeOrder |
            NSXMLNodePreserveEntities |
            NSXMLNodePreservePrefixes |
            NSXMLNodePreserveCDATA |
            NSXMLNodePreserveEmptyElements |
            NSXMLNodePreserveQuotes |
            NSXMLNodePreserveWhitespace |
            NSXMLNodePreserveDTD |
            NSXMLNodePreserveCharacterReferences |
            0xFFF00000))

if __name__ == "__main__":
    main()
