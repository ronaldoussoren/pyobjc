from PyObjCTools.TestSupport import *
import objc
from ScriptingBridge import *

class TestSBApplicationHelper (NSObject):
    def eventDidFail_withError_(self, event, error):
        pass

class TestSBApplication (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SBApplication.isRunning)

    @min_os_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('SBApplicationDelegate')
        self.assertArgHasType(TestSBApplicationHelper.eventDidFail_withError_, 0, b'r^{AEDesc=I^^{OpaqueAEDataStorageType}}')


if __name__ == "__main__":
    main()
