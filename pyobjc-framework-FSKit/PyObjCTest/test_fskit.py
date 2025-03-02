from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSKit(TestCase):
    def test_constants(self):
        self.assertIsInstance(FSKit.FSKitVersionNumber, float)
        self.assertIsInstance(FSKit.FSKitVersionString, bytes)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(FSKit)
