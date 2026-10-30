from PyObjCTools.TestSupport import TestCase
import ScriptingBridge


class TestSBApplicationHelper(ScriptingBridge.NSObject):
    def eventDidFail_withError_(self, event, error):
        pass


class TestSBApplication(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ScriptingBridge.SBApplication.isRunning)

    def test_protocols(self):
        self.assertProtocolExists("SBApplicationDelegate", ScriptingBridge)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestSBApplicationHelper.eventDidFail_withError_,
            0,
            b"r^{AEDesc=I^^{OpaqueAEDataStorageType}}",
        )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ScriptingBridge)
