from PyObjCTools.TestSupport import TestCase, min_os_level

import MLCompute


class TestMLCDevice(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBOOL(
            MLCompute.MLCDevice.deviceWithType_selectsMultipleComputeDevices_, 1
        )
