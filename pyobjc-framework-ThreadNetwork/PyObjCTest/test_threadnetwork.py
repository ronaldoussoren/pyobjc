from PyObjCTools.TestSupport import TestCase

import ThreadNetwork


class TestThreadNetwork(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ThreadNetwork)
