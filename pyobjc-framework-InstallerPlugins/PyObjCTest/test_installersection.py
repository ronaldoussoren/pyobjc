from PyObjCTools.TestSupport import *
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    from InstallerPlugins import *

    class TestInstallerSection (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(InstallerSection.shouldLoad)
            self.assertResultIsBOOL(InstallerSection.gotoPane_)

if __name__ == "__main__":
    main()
