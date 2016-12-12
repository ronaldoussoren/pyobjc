'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import InstallerPlugins

    class TestInstallerPlugins (TestCase):
        def testClasses(self):
            self.assert_( hasattr(InstallerPlugins, 'InstallerSection') )
            self.assert_( isinstance(InstallerPlugins.InstallerSection, objc.objc_class) )

            self.assert_( hasattr(InstallerPlugins, 'InstallerPane') )
            self.assert_( isinstance(InstallerPlugins.InstallerPane, objc.objc_class) )


if __name__ == "__main__":
    main()
