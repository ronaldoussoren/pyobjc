import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCoreWLAN(TestCase):
    def test_constants(self):
        self.assertEqual(CoreWLAN.CoreWLANFrameworkVersionNumber2_0, 200)
        self.assertIsInstance(CoreWLAN.CoreWLANFrameworkVersionNumber, float)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CoreWLAN)
