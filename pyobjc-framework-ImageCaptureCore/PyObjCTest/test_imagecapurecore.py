from PyObjCTools.TestSupport import TestCase

import ImageCaptureCore


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ImageCaptureCore)
