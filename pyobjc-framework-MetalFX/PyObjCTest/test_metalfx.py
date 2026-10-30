from PyObjCTools.TestSupport import TestCase

import MetalFX


class TestMetalFX(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(MetalFX)
