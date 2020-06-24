import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import ScriptingBridge


class TestSBApplicationHelper(ScriptingBridge.NSObject):
    def eventDidFail_withError_(self, event, error):
        pass


class TestSBApplication(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ScriptingBridge.SBApplication.isRunning)

    @min_os_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("SBApplicationDelegate")
        self.assertArgHasType(
            TestSBApplicationHelper.eventDidFail_withError_,
            0,
            b"r^{AEDesc=I^^{OpaqueAEDataStorageType}}",
        )
