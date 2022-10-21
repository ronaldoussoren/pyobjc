from PyObjCTools.TestSupport import TestCase

import ThreadNetwork


class TestThreadNetwork(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(ThreadNetwork)
