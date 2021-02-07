from PyObjCTools.TestSupport import TestCase

import ClassKit


class TestCLSProgressReportingCapability(TestCase):
    def test_constants(self):
        self.assertEqual(ClassKit.CLSProgressReportingCapabilityKindDuration, 0)
        self.assertEqual(ClassKit.CLSProgressReportingCapabilityKindPercent, 1)
        self.assertEqual(ClassKit.CLSProgressReportingCapabilityKindBinary, 2)
        self.assertEqual(ClassKit.CLSProgressReportingCapabilityKindQuantity, 3)
        self.assertEqual(ClassKit.CLSProgressReportingCapabilityKindScore, 4)
