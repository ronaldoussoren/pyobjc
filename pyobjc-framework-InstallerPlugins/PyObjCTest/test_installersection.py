
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerSection (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(InstallerSection.shouldLoad)
        self.failUnlessResultIsBOOL(InstallerSection.gotoPane_)

if __name__ == "__main__":
    main()
