from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSCore_MPSKeyedUnarchiver(TestCase):
    @min_os_level("10.14")
    def test_methods(self):
        self.assertArgIsOut(
            MetalPerformanceShaders.MPSKeyedUnarchiver.unarchivedObjectOfClasses_fromData_device_error_,
            3,
        )
        self.assertArgIsOut(
            MetalPerformanceShaders.MPSKeyedUnarchiver.unarchivedObjectOfClass_fromData_device_error_,
            3,
        )
        self.assertArgIsOut(
            MetalPerformanceShaders.MPSKeyedUnarchiver.initForReadingFromData_device_error_,
            2,
        )
