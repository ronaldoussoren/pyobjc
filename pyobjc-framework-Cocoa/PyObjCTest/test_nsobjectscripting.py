import Foundation
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSObjectScriptionHelper(Foundation.NSObject):
    def newScriptingObjectOfClass_forValueForKey_withContentsValue_properties_(
        self, a, b, c, d
    ):
        return 1


class TestNSObjectScription(TestCase):
    def test_protocol_methods(self):
        # Informal protocol
        self.assertArgHasType(
            TestNSObjectScriptionHelper.newScriptingObjectOfClass_forValueForKey_withContentsValue_properties_,
            0,
            objc._C_CLASS,
        )
        self.assertResultIsRetained(
            TestNSObjectScriptionHelper.newScriptingObjectOfClass_forValueForKey_withContentsValue_properties_
        )

        self.assertArgHasType(
            TestNSObjectScriptionHelper.newScriptingObjectOfClass_forValueForKey_withContentsValue_properties_,
            0,
            objc._C_CLASS,
        )
        self.assertResultIsRetained(
            TestNSObjectScriptionHelper.newScriptingObjectOfClass_forValueForKey_withContentsValue_properties_
        )
