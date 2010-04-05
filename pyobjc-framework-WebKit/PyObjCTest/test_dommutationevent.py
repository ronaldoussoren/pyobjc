
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMMutationEvent (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_MODIFICATION, 1)
        self.assertEqual(DOM_ADDITION, 2)
        self.assertEqual(DOM_REMOVAL, 3)

    def testMethods(self):
        self.assertArgIsBOOL(DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_, 1)
        self.assertArgIsBOOL(DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_, 2)
        self.assertArgIsBOOL(DOMMutationEvent.initMutationEvent________, 2)

if __name__ == "__main__":
    main()
