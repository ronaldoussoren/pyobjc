
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerState (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(InstallerState_Choice_Identifier, unicode)
        self.failUnlessIsInstance(InstallerState_Choice_Installed, unicode)
        self.failUnlessIsInstance(InstallerState_Choice_CustomLocation, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(InstallerState.licenseAgreed)
        self.failUnlessResultIsBOOL(InstallerState.installStarted)
        self.failUnlessResultIsBOOL(InstallerState.installSucceeded)


if __name__ == "__main__":
    main()
