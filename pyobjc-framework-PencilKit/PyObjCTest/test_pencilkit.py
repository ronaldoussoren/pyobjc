from PyObjCTools.TestSupport import TestCase

import PencilKit


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(PencilKit)
