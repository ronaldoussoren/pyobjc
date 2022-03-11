import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCoreWLAN(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(CoreWLAN.CoreWLANFrameworkVersionNumber2_0, 200)
        self.assertIsInstance(CoreWLAN.CoreWLANFrameworkVersionNumber, float)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CoreWLAN)
