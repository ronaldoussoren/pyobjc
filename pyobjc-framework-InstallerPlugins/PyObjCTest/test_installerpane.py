
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerPane (TestCase):
    def testConstants(self):
        self.assertEqual(InstallerDirectionForward, 0)
        self.assertEqual(InstallerDirectionBackward, 1)
        self.assertEqual(InstallerDirectionUndefined, 2)

    def testMethods(self):
        self.assertResultIsBOOL(InstallerPane.shouldExitPane_)
        self.assertArgIsBOOL(InstallerPane.setNextEnabled_, 0)
        self.assertResultIsBOOL(InstallerPane.nextEnabled)
        self.assertArgIsBOOL(InstallerPane.setPreviousEnabled_, 0)
        self.assertResultIsBOOL(InstallerPane.previousEnabled)
        self.assertResultIsBOOL(InstallerPane.gotoNextPane)
        self.assertResultIsBOOL(InstallerPane.gotoPreviousPane)



if __name__ == "__main__":
    main()
