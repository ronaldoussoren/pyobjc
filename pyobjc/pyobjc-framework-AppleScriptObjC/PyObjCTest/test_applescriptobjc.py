
from PyObjCTools.TestSupport import *
from AppleScriptObjC import *

class TestAppleScriptObjC (TestCase):
    @min_os_level('10.6')
    def testDummy(self):
        # Nothing to test...
        self.failUnless(hasattr(NSBundle, 'loadAppleScriptObjectiveCScripts'))

if __name__ == "__main__":
    main()
