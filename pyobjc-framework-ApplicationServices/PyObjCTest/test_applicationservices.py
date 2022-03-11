import ApplicationServices
import HIServices
import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestApplicationServices(TestCase):
    def testTrivial(self):
        ApplicationServices.kAXErrorSuccess


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ApplicationServices)
        self.assertCallableMetadataIsSane(HIServices)
        self.assertCallableMetadataIsSane(PrintCore)
