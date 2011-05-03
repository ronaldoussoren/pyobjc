
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerState (TestCase):
    def testConstants(self):
        self.assertIsInstance(InstallerState_Choice_Identifier, unicode)
        self.assertIsInstance(InstallerState_Choice_Installed, unicode)
        self.assertIsInstance(InstallerState_Choice_CustomLocation, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(InstallerState.licenseAgreed)
        self.assertResultIsBOOL(InstallerState.installStarted)
        self.assertResultIsBOOL(InstallerState.installSucceeded)


if __name__ == "__main__":
    main()
