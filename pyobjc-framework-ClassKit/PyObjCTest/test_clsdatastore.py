from PyObjCTools.TestSupport import TestCase, min_os_level

import ClassKit
import objc


class TestCLSDataStore(TestCase):
    def test_protocols(self):
        objc.protocolNamed("CLSDataStoreDelegate")

    def test_methods(self):
        self.assertArgIsBlock(ClassKit.CLSDataStore.saveWithCompletion_, 0, b"v@")
        self.assertArgIsBlock(
            ClassKit.CLSDataStore.contextsMatchingIdentifierPath_completion_, 1, b"v@@"
        )

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertArgIsBlock(
            ClassKit.CLSDataStore.fetchActivityForURL_completion_, 1, b"v@@"
        )
