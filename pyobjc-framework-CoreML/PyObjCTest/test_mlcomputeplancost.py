from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLComputePlanCost(TestCase):
    @min_os_level("14.4")
    def testClasses(self):
        self.assertTrue(CoreML.MLComputePlanCost.__objc_final__)
