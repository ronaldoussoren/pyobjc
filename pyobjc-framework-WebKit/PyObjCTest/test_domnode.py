
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMNode (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_ELEMENT_NODE, 1)
        self.failUnlessEqual(DOM_ATTRIBUTE_NODE, 2)
        self.failUnlessEqual(DOM_TEXT_NODE, 3)
        self.failUnlessEqual(DOM_CDATA_SECTION_NODE, 4)
        self.failUnlessEqual(DOM_ENTITY_REFERENCE_NODE, 5)
        self.failUnlessEqual(DOM_ENTITY_NODE, 6)
        self.failUnlessEqual(DOM_PROCESSING_INSTRUCTION_NODE, 7)
        self.failUnlessEqual(DOM_COMMENT_NODE, 8)
        self.failUnlessEqual(DOM_DOCUMENT_NODE, 9)
        self.failUnlessEqual(DOM_DOCUMENT_TYPE_NODE, 10)
        self.failUnlessEqual(DOM_DOCUMENT_FRAGMENT_NODE, 11)
        self.failUnlessEqual(DOM_NOTATION_NODE, 12)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_DISCONNECTED, 1)
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_PRECEDING, 2)
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_FOLLOWING, 4)
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_CONTAINS, 8)
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_CONTAINED_BY, 16)
        self.failUnlessEqual(DOM_DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC, 32)


    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMNode.hasChildNodes)
        self.failUnlessArgIsBOOL(DOMNode.cloneNode_, 0)
        self.failUnlessResultIsBOOL(DOMNode.isSupported_version_)
        self.failUnlessResultIsBOOL(DOMNode.isSupported__)
        self.failUnlessResultIsBOOL(DOMNode.hasAttributes)
        self.failUnlessResultIsBOOL(DOMNode.isSameNode_)
        self.failUnlessResultIsBOOL(DOMNode.isEqualNode_)

        self.failUnlessResultIsBOOL(DOMNode.isContentEditable)

if __name__ == "__main__":
    main()
