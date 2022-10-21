from PyObjCTools.TestSupport import TestCase

import SafetyKit
import objc


class TestSACrashDetectionManager(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SACrashDetectionDelegate")

    def test_methods(self):
        self.assertResultIsBOOL(SafetyKit.SACrashDetectionManager.isAvailable)
        self.assertArgIsBlock(
            SafetyKit.SACrashDetectionManager.requestAuthorizationWithCompletionHandler_,
            0,
            b"v" + objc._C_NSInteger + b"@",
        )
