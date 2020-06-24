from PyObjCTools.TestSupport import TestCase
import InstallerPlugins


class TestInstallerPane(TestCase):
    def testConstants(self):
        self.assertEqual(InstallerPlugins.InstallerDirectionForward, 0)
        self.assertEqual(InstallerPlugins.InstallerDirectionBackward, 1)
        self.assertEqual(InstallerPlugins.InstallerDirectionUndefined, 2)

    def testMethods(self):
        self.assertResultIsBOOL(InstallerPlugins.InstallerPane.shouldExitPane_)
        self.assertArgIsBOOL(InstallerPlugins.InstallerPane.setNextEnabled_, 0)
        self.assertResultIsBOOL(InstallerPlugins.InstallerPane.nextEnabled)
        self.assertArgIsBOOL(InstallerPlugins.InstallerPane.setPreviousEnabled_, 0)
        self.assertResultIsBOOL(InstallerPlugins.InstallerPane.previousEnabled)
        self.assertResultIsBOOL(InstallerPlugins.InstallerPane.gotoNextPane)
        self.assertResultIsBOOL(InstallerPlugins.InstallerPane.gotoPreviousPane)
