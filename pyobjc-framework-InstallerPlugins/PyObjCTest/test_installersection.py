
from PyObjCTools.TestSupport import *
from InstallerPlugins import *

class TestInstallerSection (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(InstallerSection.shouldLoad)
        self.assertResultIsBOOL(InstallerSection.gotoPane_)

if __name__ == "__main__":
    main()
