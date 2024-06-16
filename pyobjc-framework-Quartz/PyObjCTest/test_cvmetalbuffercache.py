from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCVMetalBufferCache(TestCase):
    @min_os_level("15.0")
    def test_types(self):
        self.assertIsCFType(Quartz.CVMetalBufferCacheRef)

    @min_os_level("15.0")
    def test_functions(self):
        Quartz.CVMetalBufferCacheGetTypeID

        self.assertArgIsOut(Quartz.CVMetalBufferCacheCreate, 3)
        self.assertArgIsCFRetained(Quartz.CVMetalBufferCacheCreate, 3)

        self.assertArgIsOut(Quartz.CVMetalBufferCacheCreateBufferFromImage, 3)
        self.assertArgIsCFRetained(Quartz.CVMetalBufferCacheCreateBufferFromImage, 3)

        Quartz.CVMetalBufferCacheFlush
