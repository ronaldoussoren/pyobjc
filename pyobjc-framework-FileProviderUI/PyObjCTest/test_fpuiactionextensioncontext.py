from PyObjCTools.TestSupport import *

import FileProviderUI


class TestFPUIActionExtensionContext(TestCase):
    def test_constants(self):
        self.assertEqual(FileProviderUI.FPUIExtensionErrorCodeUserCancelled, 0)
        self.assertEqual(FileProviderUI.FPUIExtensionErrorCodeFailed, 1)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(FileProviderUI.FPUIErrorDomain, unicode)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            FileProviderUI.FPUIActionExtensionContext.completeRequestReturningItems_completionHandler_,
            1,
            b"vZ",
        )
