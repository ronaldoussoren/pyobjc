import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDiscRecording(TestCase):
    def testFunctions(self):
        DiscRecording.DRGetVersion


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(DiscRecording)
