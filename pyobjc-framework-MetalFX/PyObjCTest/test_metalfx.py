from PyObjCTools.TestSupport import TestCase

import MetalFX


class TestMetalFX(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(MetalFX)
