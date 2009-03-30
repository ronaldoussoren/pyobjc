from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSScriptClassDescription (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSScriptClassDescription.matchesAppleEventCode_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.supportsCommand_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.isLocationRequiredToCreateForKey_)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSScriptClassDescription.hasPropertyForKey_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.hasOrderedToManyRelationshipForKey_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.hasReadablePropertyForKey_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.hasWritablePropertyForKey_)
        self.failUnlessResultIsBOOL(NSScriptClassDescription.isReadOnlyKey_)

if __name__ == "__main__":
    main()
