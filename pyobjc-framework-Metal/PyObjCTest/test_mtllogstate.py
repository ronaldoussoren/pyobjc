from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level

import Metal


class TestMTLLogStateHelper(Metal.NSObject):
    def addLogHandler_(self, a):
        pass


class TestMTLLogState(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTLLogLevel)
        self.assertEqual(Metal.MTLLogLevelUndefined, 0)
        self.assertEqual(Metal.MTLLogLevelDebug, 1)
        self.assertEqual(Metal.MTLLogLevelInfo, 2)
        self.assertEqual(Metal.MTLLogLevelNotice, 3)
        self.assertEqual(Metal.MTLLogLevelError, 4)
        self.assertEqual(Metal.MTLLogLevelFault, 5)

        self.assertIsEnumType(Metal.TLLogStateError)
        self.assertEqual(Metal.MTLLogStateErrorInvalidSize, 1)
        self.assertEqual(Metal.MTLLogStateErrorInvalid, 2)

    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(Metal.MTLLogStateErrorDomain, str)

    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLLogState")

    def test_protocol_methods(self):
        self.assertArgIsBlock(TestMTLLogStateHelper.addLogHandler_, 0, b"v@@q@")
