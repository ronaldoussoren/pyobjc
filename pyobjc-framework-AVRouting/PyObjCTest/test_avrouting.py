from PyObjCTools.TestSupport import TestCase

import AVRouting


class TestAVRouting(TestCase):
    def test_metadata_sane(self):
        self.assertCallableMetadataIsSane(AVRouting)
