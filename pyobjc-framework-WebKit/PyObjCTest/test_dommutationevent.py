from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMMutationEvent(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_MODIFICATION, 1)
        self.assertEqual(WebKit.DOM_ADDITION, 2)
        self.assertEqual(WebKit.DOM_REMOVAL, 3)

    def testMethods(self):
        self.assertArgIsBOOL(
            WebKit.DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            WebKit.DOMMutationEvent.initMutationEvent_canBubble_cancelable_relatedNode_prevValue_newValue_attrName_attrChange_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(WebKit.DOMMutationEvent.initMutationEvent________, 2)
