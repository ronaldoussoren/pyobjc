import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLIOCommandQueueHelper(Metal.NSObject):
    def newScratchBufferWithMinimumSize_(self, a):
        return 1


class TestMTLIOCommandQueue(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Metal.MTLIOPriority)
        self.assertEqual(Metal.MTLIOPriorityHigh, 0)
        self.assertEqual(Metal.MTLIOPriorityNormal, 1)
        self.assertEqual(Metal.MTLIOPriorityLow, 2)

        self.assertIsEnumType(Metal.MTLIOCommandQueueType)
        self.assertEqual(Metal.MTLIOCommandQueueTypeConcurrent, 0)
        self.assertEqual(Metal.MTLIOCommandQueueTypeSerial, 1)

        self.assertIsEnumType(Metal.MTLIOError)
        self.assertEqual(Metal.MTLIOErrorURLInvalid, 1)
        self.assertEqual(Metal.MTLIOErrorInternal, 2)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(Metal.MTLIOErrorDomain, str)

    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLIOCommandQueue")
        self.assertProtocolExists("MTLIOScratchBuffer")
        self.assertProtocolExists("MTLIOScratchBufferAllocator")
        self.assertProtocolExists("MTLIOFileHandle")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTLIOCommandQueueHelper.newScratchBufferWithMinimumSize_,
            0,
            objc._C_NSUInteger,
        )
