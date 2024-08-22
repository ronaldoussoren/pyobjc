from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            FSKit.FSClient.fetchInstalledExtensionsWithCompletionHandler, 0, b"v@@"
        )
        self.assertArgIsOut(FSKit.FSClient.installedExtensionsWithError_, 0)
