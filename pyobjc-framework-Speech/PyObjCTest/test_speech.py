from PyObjCTools.TestSupport import TestCase

import Speech


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(Speech)
