import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDiscRecording(TestCase):
    def test_functions(self):
        DiscRecording.DRGetVersion


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(DiscRecording)
