from PyObjCTools.TestSupport import TestCase

import CryptoTokenKit


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CryptoTokenKit)
