from PyObjCTools.TestSupport import TestCase

import PhotosUI


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(PhotosUI)
