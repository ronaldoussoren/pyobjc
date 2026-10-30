from PyObjCTools.TestSupport import TestCase, min_os_level

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            FSKit.FSClient.fetchInstalledExtensionsWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBlock(
            FSKit.FSClient.mountSingleVolumeForResource_bundleID_options_completionHandler_,
            3,
            b"v@@",
        )

        self.assertResultIsBOOL(FSKit.FSClient.openFileSystemExtensionsSettings)
