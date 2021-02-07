from PyObjCTools.TestSupport import TestCase

import InstallerPlugins


class TestInstallerSection(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(InstallerPlugins.InstallerSection.shouldLoad)
        self.assertResultIsBOOL(InstallerPlugins.InstallerSection.gotoPane_)
