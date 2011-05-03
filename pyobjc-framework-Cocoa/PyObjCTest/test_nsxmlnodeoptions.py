from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSXMLNodeOptions (TestCase):
    def testConstants(self):
        self.assertEqual(NSXMLNodeOptionsNone, 0)
        self.assertEqual(NSXMLNodeIsCDATA, 1 << 0)
        self.assertEqual(NSXMLNodeExpandEmptyElement, 1 << 1)
        self.assertEqual(NSXMLNodeCompactEmptyElement,  1 << 2)
        self.assertEqual(NSXMLNodeUseSingleQuotes, 1 << 3)
        self.assertEqual(NSXMLNodeUseDoubleQuotes, 1 << 4)
        self.assertEqual(NSXMLDocumentTidyHTML, 1 << 9)
        self.assertEqual(NSXMLDocumentTidyXML, 1 << 10)
        self.assertEqual(NSXMLDocumentValidate, 1 << 13)
        self.assertEqual(NSXMLDocumentXInclude, 1 << 16)
        self.assertEqual(NSXMLNodePrettyPrint, 1 << 17)
        self.assertEqual(NSXMLDocumentIncludeContentTypeDeclaration, 1 << 18)
        self.assertEqual(NSXMLNodePreserveNamespaceOrder, 1 << 20)
        self.assertEqual(NSXMLNodePreserveAttributeOrder, 1 << 21)
        self.assertEqual(NSXMLNodePreserveEntities, 1 << 22)
        self.assertEqual(NSXMLNodePreservePrefixes, 1 << 23)
        self.assertEqual(NSXMLNodePreserveCDATA, 1 << 24)
        self.assertEqual(NSXMLNodePreserveWhitespace, 1 << 25)
        self.assertEqual(NSXMLNodePreserveDTD, 1 << 26)
        self.assertEqual(NSXMLNodePreserveCharacterReferences, 1 << 27)
        self.assertEqual(NSXMLNodePreserveEmptyElements, (
            NSXMLNodeExpandEmptyElement | NSXMLNodeCompactEmptyElement))
        self.assertEqual(NSXMLNodePreserveQuotes, (NSXMLNodeUseSingleQuotes | NSXMLNodeUseDoubleQuotes))
        self.assertEqual(NSXMLNodePreserveAll & 0xFFFFFFFF, 0xFFFFFFFF & (
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
