from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            FSKit.FSClient.fetchInstalledExtensionsWithCompletionHandler_, 0, b"v@@"
        )
