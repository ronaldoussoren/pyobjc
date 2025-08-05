import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4CommandAllocatorHelper(Metal.NSObject):
    def allocatedSize(self):
        return 1


class TestMTL4CommandAllocator(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CommandAllocator")

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTL4CommandAllocatorHelper.allocatedSize, b"Q")
