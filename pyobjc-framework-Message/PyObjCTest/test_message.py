import Message  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestMessage(TestCase):
    pass


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(Message)
