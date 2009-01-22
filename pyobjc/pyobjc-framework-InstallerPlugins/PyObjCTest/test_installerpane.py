
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerPane (TestCase):
    def testConstants(self):
        self.failUnlessEqual(InstallerDirectionForward, 0)
        self.failUnlessEqual(InstallerDirectionBackward, 1)
        self.failUnlessEqual(InstallerDirectionUndefined, 2)

    def testMethods(self):
        self.failUnlessResultIsBOOL(InstallerPane.shouldExitPane_)
        self.failUnlessArgIsBOOL(InstallerPane.setNextEnabled_, 0)
        self.failUnlessResultIsBOOL(InstallerPane.nextEnabled)
        self.failUnlessArgIsBOOL(InstallerPane.setPreviousEnabled_, 0)
        self.failUnlessResultIsBOOL(InstallerPane.previousEnabled)
        self.failUnlessResultIsBOOL(InstallerPane.gotoNextPane)
        self.failUnlessResultIsBOOL(InstallerPane.gotoPreviousPane)



if __name__ == "__main__":
    main()
