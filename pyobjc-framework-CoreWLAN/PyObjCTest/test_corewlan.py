import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CoreWLAN)
