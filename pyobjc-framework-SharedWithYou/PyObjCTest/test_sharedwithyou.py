from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSharedWithYou(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(SharedWithYou)
