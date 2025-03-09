from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSKit(TestCase):
    def test_constants(self):
        self.assertIsInstance(FSKit.FSKitVersionNumber, float)
        self.assertNotHasAttr(FSKit, "FSKitVersionString")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(FSKit)
