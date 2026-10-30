from PyObjCTools.TestSupport import TestCase

import AVRouting


class TestAVRouting(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(AVRouting)
