from PyObjCTools.TestSupport import TestCase

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
