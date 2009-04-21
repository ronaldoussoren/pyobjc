
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMMutationEvent (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_MODIFICATION, 1)
        self.failUnlessEqual(DOM_ADDITION, 2)
        self.failUnlessEqual(DOM_REMOVAL, 3)

    def testMethods(self):
        self.failUnlessArgIsBOOL(DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_, 1)
        self.failUnlessArgIsBOOL(DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_, 2)
        self.failUnlessArgIsBOOL(DOMMutationEvent.initMutationEvent________, 2)

if __name__ == "__main__":
    main()
