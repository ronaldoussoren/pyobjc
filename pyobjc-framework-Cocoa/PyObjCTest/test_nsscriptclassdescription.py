import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScriptClassDescription(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.matchesAppleEventCode_
        )
        self.assertResultIsBOOL(Foundation.NSScriptClassDescription.supportsCommand_)
        self.assertResultIsBOOL(
            Foundation.NSScriptClassDescription.isLocationRequiredToCreateForKey_
        )

    @min_os_level("10.5")
    def test_methods10_5(self):
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
