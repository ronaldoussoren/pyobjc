import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCoreWLAN(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(CoreWLAN.CoreWLANFrameworkVersionNumber2_0, 200)
        self.assertIsInstance(CoreWLAN.CoreWLANFrameworkVersionNumber, float)
