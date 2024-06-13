from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(FSKit.FSClient.installedExtensions_, 0, b"v@@")
        self.assertArgIsBlock(FSKit.FSClient.installedExtensionsSync_, 0, b"v@@")
