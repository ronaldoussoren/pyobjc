from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLAllComputeDevices(TestCase):
    @min_os_level("14.0")
    def test_functions(self):
        CoreML.MLAllComputeDevices
