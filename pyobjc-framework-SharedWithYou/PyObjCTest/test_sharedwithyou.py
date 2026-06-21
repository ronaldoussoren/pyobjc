from PyObjCTools.TestSupport import TestCase

import SharedWithYou


class TestSharedWithYou(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SharedWithYou)
