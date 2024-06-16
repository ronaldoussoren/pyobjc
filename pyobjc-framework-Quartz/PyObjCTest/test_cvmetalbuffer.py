from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz


class TestCVMetalBuffer(TestCase):
    def test_types(self):
        self.assertIs(Quartz.CVMetalBufferRef, Quartz.CFBufferRef)

    @min_os_level("15.0")
    def test_functions15_0(self):
        Quartz.CVMetalBufferGetTypeID

    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolNamed("MTLBuffer")
