
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMNode (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_ELEMENT_NODE, 1)
        self.assertEqual(DOM_ATTRIBUTE_NODE, 2)
        self.assertEqual(DOM_TEXT_NODE, 3)
        self.assertEqual(DOM_CDATA_SECTION_NODE, 4)
        self.assertEqual(DOM_ENTITY_REFERENCE_NODE, 5)
        self.assertEqual(DOM_ENTITY_NODE, 6)
        self.assertEqual(DOM_PROCESSING_INSTRUCTION_NODE, 7)
        self.assertEqual(DOM_COMMENT_NODE, 8)
        self.assertEqual(DOM_DOCUMENT_NODE, 9)
        self.assertEqual(DOM_DOCUMENT_TYPE_NODE, 10)
        self.assertEqual(DOM_DOCUMENT_FRAGMENT_NODE, 11)
        self.assertEqual(DOM_NOTATION_NODE, 12)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(DOM_DOCUMENT_POSITION_DISCONNECTED, 1)
        self.assertEqual(DOM_DOCUMENT_POSITION_PRECEDING, 2)
        self.assertEqual(DOM_DOCUMENT_POSITION_FOLLOWING, 4)
        self.assertEqual(DOM_DOCUMENT_POSITION_CONTAINS, 8)
        self.assertEqual(DOM_DOCUMENT_POSITION_CONTAINED_BY, 16)
        self.assertEqual(DOM_DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC, 32)


    def testMethods(self):
        self.assertResultIsBOOL(DOMNode.hasChildNodes)
        self.assertArgIsBOOL(DOMNode.cloneNode_, 0)
        self.assertResultIsBOOL(DOMNode.isSupported_version_)
        self.assertResultIsBOOL(DOMNode.isSupported__)
        self.assertResultIsBOOL(DOMNode.hasAttributes)
        self.assertResultIsBOOL(DOMNode.isSameNode_)
        self.assertResultIsBOOL(DOMNode.isEqualNode_)

        self.assertResultIsBOOL(DOMNode.isContentEditable)

if __name__ == "__main__":
    main()
