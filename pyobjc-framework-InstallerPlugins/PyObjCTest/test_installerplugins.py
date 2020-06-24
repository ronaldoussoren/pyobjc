"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import TestCase
import InstallerPlugins


class TestInstallerPlugins(TestCase):
    def testClasses(self):
        self.assertHasAttr(InstallerPlugins, "InstallerSection")
        self.assertIsInstance(InstallerPlugins.InstallerSection, objc.objc_class)

        self.assertHasAttr(InstallerPlugins, "InstallerPane")
        self.assertIsInstance(InstallerPlugins.InstallerPane, objc.objc_class)
