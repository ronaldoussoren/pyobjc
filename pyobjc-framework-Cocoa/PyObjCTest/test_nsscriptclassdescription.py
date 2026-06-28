import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptClassDescription(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.matchesAppleEventCode_
        )
        self.assertResultIsBOOL(Foundation.NSScriptClassDescription.supportsCommand_)
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.isLocationRequiredToCreateForKey_
        )

        self.assertResultIsBOOL(Foundation.NSScriptClassDescription.hasPropertyForKey_)
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.hasOrderedToManyRelationshipForKey_
        )
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.hasReadablePropertyForKey_
        )
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.hasWritablePropertyForKey_
        )
        self.assertResultIsBOOL(Foundation.NSScriptClassDescription.isReadOnlyKey_)
