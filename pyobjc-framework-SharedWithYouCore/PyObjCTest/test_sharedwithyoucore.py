from PyObjCTools.TestSupport import TestCase
import SharedWithYouCore


class TestSharedWithYouCore(TestCase):
    def test_constants(self):
        self.assertIsInstance(SharedWithYouCore.SharedWithYouCoreVersionNumber, float)
        self.assertNotHasAttr(SharedWithYouCore, "SharedWithYouCoreVersionString")

    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(SharedWithYouCore)
