import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSStreamHelper(Foundation.NSObject):
    def stream_handleEvent_(self, a, b):
        pass


class TestNSStreamUsage(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSStreamNetworkServiceTypeValue, str)
        self.assertIsTypedEnum(Foundation.NSStreamPropertyKey, str)
        self.assertIsTypedEnum(Foundation.NSStreamSOCKSProxyConfiguration, str)
        self.assertIsTypedEnum(Foundation.NSStreamSOCKSProxyVersion, str)
        self.assertIsTypedEnum(Foundation.NSStreamSocketSecurityLevel, str)

    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSStreamEvent)
        self.assertIsEnumType(Foundation.NSStreamStatus)

    def testUsage(self):
        # Test the usage of methods that require extra work

        # Try to create a connection to the IPP port on the local host
        (
            inputStream,
            outputStream,
        ) = Foundation.NSStream.getStreamsToHost_port_inputStream_outputStream_(
            Foundation.NSHost.hostWithAddress_("127.0.0.1"), 631, None, None  # IPP port
        )

        self.assertIsInstance(inputStream, Foundation.NSInputStream)
        self.assertIsInstance(outputStream, Foundation.NSOutputStream)

        inputStream.close()
        outputStream.close()

    def testConstants(self):
        self.assertEqual(Foundation.NSStreamStatusNotOpen, 0)
        self.assertEqual(Foundation.NSStreamStatusOpening, 1)
        self.assertEqual(Foundation.NSStreamStatusOpen, 2)
        self.assertEqual(Foundation.NSStreamStatusReading, 3)
        self.assertEqual(Foundation.NSStreamStatusWriting, 4)
        self.assertEqual(Foundation.NSStreamStatusAtEnd, 5)
        self.assertEqual(Foundation.NSStreamStatusClosed, 6)
        self.assertEqual(Foundation.NSStreamStatusError, 7)

        self.assertEqual(Foundation.NSStreamEventNone, 0)
        self.assertEqual(Foundation.NSStreamEventOpenCompleted, 1 << 0)
        self.assertEqual(Foundation.NSStreamEventHasBytesAvailable, 1 << 1)
        self.assertEqual(Foundation.NSStreamEventHasSpaceAvailable, 1 << 2)
        self.assertEqual(Foundation.NSStreamEventErrorOccurred, 1 << 3)
        self.assertEqual(Foundation.NSStreamEventEndEncountered, 1 << 4)

        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelKey, str)
        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelNone, str)
        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelSSLv2, str)
        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelSSLv3, str)
        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelTLSv1, str)
        self.assertIsInstance(Foundation.NSStreamSocketSecurityLevelNegotiatedSSL, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyConfigurationKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyHostKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyPortKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyVersionKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyUserKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyPasswordKey, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyVersion4, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSProxyVersion5, str)
        self.assertIsInstance(Foundation.NSStreamDataWrittenToMemoryStreamKey, str)
        self.assertIsInstance(Foundation.NSStreamFileCurrentOffsetKey, str)
        self.assertIsInstance(Foundation.NSStreamSocketSSLErrorDomain, str)
        self.assertIsInstance(Foundation.NSStreamSOCKSErrorDomain, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Foundation.NSStreamNetworkServiceType, str)
        self.assertIsInstance(Foundation.NSStreamNetworkServiceTypeVoIP, str)
        self.assertIsInstance(Foundation.NSStreamNetworkServiceTypeVideo, str)
        self.assertIsInstance(Foundation.NSStreamNetworkServiceTypeBackground, str)
        self.assertIsInstance(Foundation.NSStreamNetworkServiceTypeVoice, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Foundation.NSStreamNetworkServiceTypeCallSignaling, str)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSStream.setProperty_forKey_)

        self.assertArgHasType(Foundation.NSInputStream.read_maxLength_, 0, b"o^v")
        self.assertArgSizeInArg(Foundation.NSInputStream.read_maxLength_, 0, 1)
        self.assertArgSizeInResult(Foundation.NSInputStream.read_maxLength_, 0)

        self.assertResultIsBOOL(Foundation.NSInputStream.hasBytesAvailable)

        self.assertArgHasType(Foundation.NSOutputStream.write_maxLength_, 0, b"n^v")
        self.assertArgSizeInArg(Foundation.NSOutputStream.write_maxLength_, 0, 1)
        self.assertResultIsBOOL(Foundation.NSOutputStream.hasSpaceAvailable)

        b = Foundation.NSOutputStream.alloc().initToMemory()
        self.assertArgHasType(b.initToFileAtPath_append_, 1, objc._C_NSBOOL)
        self.assertArgHasType(
            Foundation.NSOutputStream.outputStreamToFileAtPath_append_,
            1,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(b.initToBuffer_capacity_, 0, b"o^v")
        self.assertArgSizeInArg(b.initToBuffer_capacity_, 0, 1)
        self.assertArgHasType(
            Foundation.NSOutputStream.outputStreamToBuffer_capacity_, 0, b"o^v"
        )
        self.assertArgSizeInArg(
            Foundation.NSOutputStream.outputStreamToBuffer_capacity_, 0, 1
        )

        self.assertArgIsOut(Foundation.NSInputStream.getBuffer_length_, 0)
        self.assertArgIsOut(Foundation.NSInputStream.getBuffer_length_, 1)
        self.assertArgSizeInArg(Foundation.NSInputStream.getBuffer_length_, 0, 1)

    def testDelegate(self):
        self.assertArgHasType(
            TestNSStreamHelper.stream_handleEvent_, 1, objc._C_NSUInteger
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        b = Foundation.NSOutputStream.alloc()
        try:
            self.assertArgIsBOOL(b.initWithURL_append_, 1)
        finally:
            b = b.initToMemory()
        self.assertArgIsBOOL(Foundation.NSOutputStream.outputStreamWithURL_append_, 1)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsOut(
            Foundation.NSStream.getStreamsToHostWithName_port_inputStream_outputStream_,
            2,
        )
        self.assertArgIsOut(
            Foundation.NSStream.getStreamsToHostWithName_port_inputStream_outputStream_,
            3,
        )

        self.assertArgIsOut(
            Foundation.NSStream.getBoundStreamsWithBufferSize_inputStream_outputStream_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSStream.getBoundStreamsWithBufferSize_inputStream_outputStream_,
            2,
        )

    @min_sdk_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("NSStreamDelegate")
