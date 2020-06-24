from PyObjCTools.TestSupport import TestCase
import InstallerPlugins


class TestInstallerState(TestCase):
    def testConstants(self):
        self.assertIsInstance(InstallerPlugins.InstallerState_Choice_Identifier, str)
        self.assertIsInstance(InstallerPlugins.InstallerState_Choice_Installed, str)
        self.assertIsInstance(
            InstallerPlugins.InstallerState_Choice_CustomLocation, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(InstallerPlugins.InstallerState.licenseAgreed)
        self.assertResultIsBOOL(InstallerPlugins.InstallerState.installStarted)
        self.assertResultIsBOOL(InstallerPlugins.InstallerState.installSucceeded)
