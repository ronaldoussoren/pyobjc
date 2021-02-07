import CoreMedia
from PyObjCTools.TestSupport import TestCase


class TestCMMemoryPool(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMMemoryPoolError_AllocationFailed, -15490)
        self.assertEqual(CoreMedia.kCMMemoryPoolError_InvalidParameter, -15491)

    def test_types(self):
        self.assertIsCFType(CoreMedia.CMMemoryPoolRef)

    def test_functions(self):
        CoreMedia.kCMMemoryPoolOption_AgeOutPeriod

        self.assertResultIsCFRetained(CoreMedia.CMMemoryPoolCreate)

        CoreMedia.CMMemoryPoolGetAllocator
        CoreMedia.CMMemoryPoolFlush
        CoreMedia.CMMemoryPoolInvalidate
