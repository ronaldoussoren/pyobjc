from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSScriptClassDescription (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSScriptClassDescription.matchesAppleEventCode_)
        self.assertResultIsBOOL(NSScriptClassDescription.supportsCommand_)
        self.assertResultIsBOOL(NSScriptClassDescription.isLocationRequiredToCreateForKey_)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSScriptClassDescription.hasPropertyForKey_)
        self.assertResultIsBOOL(NSScriptClassDescription.hasOrderedToManyRelationshipForKey_)
        self.assertResultIsBOOL(NSScriptClassDescription.hasReadablePropertyForKey_)
        self.assertResultIsBOOL(NSScriptClassDescription.hasWritablePropertyForKey_)
        self.assertResultIsBOOL(NSScriptClassDescription.isReadOnlyKey_)

if __name__ == "__main__":
    main()
