from PyObjCTools.TestSupport import TestCase

import SafariServices


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(SafariServices)
