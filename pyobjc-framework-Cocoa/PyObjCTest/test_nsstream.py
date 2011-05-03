from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSStreamHelper (NSObject):
    def stream_handleEvent_(self, a, b): pass

class TestNSStreamUsage(TestCase):

    def testUsage(self):
        # Test the usage of methods that require extra work

        # Try to create a connection to the IPP port on the local host
        inputStream, outputStream = NSStream.getStreamsToHost_port_inputStream_outputStream_(
                NSHost.hostWithAddress_(u"127.0.0.1"), 
                631, # IPP port
                None,
                None
        )

        self.assert_(isinstance(inputStream, NSInputStream))
        self.assert_(isinstance(outputStream, NSOutputStream))

        inputStream.close()
        outputStream.close()

    def testConstants(self):
        self.assertEqual(NSStreamStatusNotOpen, 0)
        self.assertEqual(NSStreamStatusOpening, 1)
        self.assertEqual(NSStreamStatusOpen, 2)
        self.assertEqual(NSStreamStatusReading, 3)
        self.assertEqual(NSStreamStatusWriting, 4)    
        self.assertEqual(NSStreamStatusAtEnd, 5)
        self.assertEqual(NSStreamStatusClosed, 6)
        self.assertEqual(NSStreamStatusError, 7)

        self.assertEqual(NSStreamEventNone, 0)
        self.assertEqual(NSStreamEventOpenCompleted, 1 << 0)
        self.assertEqual(NSStreamEventHasBytesAvailable, 1 << 1)
        self.assertEqual(NSStreamEventHasSpaceAvailable, 1 << 2)
        self.assertEqual(NSStreamEventErrorOccurred, 1 << 3)
        self.assertEqual(NSStreamEventEndEncountered, 1 << 4)

        self.assertIsInstance(NSStreamSocketSecurityLevelKey, unicode)
        self.assertIsInstance(NSStreamSocketSecurityLevelNone, unicode)
        self.assertIsInstance(NSStreamSocketSecurityLevelSSLv2, unicode)
        self.assertIsInstance(NSStreamSocketSecurityLevelSSLv3, unicode)
        self.assertIsInstance(NSStreamSocketSecurityLevelTLSv1, unicode)
        self.assertIsInstance(NSStreamSocketSecurityLevelNegotiatedSSL, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyConfigurationKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyHostKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyPortKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyVersionKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyUserKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyPasswordKey, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyVersion4, unicode)
        self.assertIsInstance(NSStreamSOCKSProxyVersion5, unicode)
        self.assertIsInstance(NSStreamDataWrittenToMemoryStreamKey, unicode)
        self.assertIsInstance(NSStreamFileCurrentOffsetKey, unicode)
        self.assertIsInstance(NSStreamSocketSSLErrorDomain, unicode)
        self.assertIsInstance(NSStreamSOCKSErrorDomain, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSStream.setProperty_forKey_)

        self.assertArgHasType(NSInputStream.read_maxLength_, 0, b'o^v')
        self.assertArgSizeInArg(NSInputStream.read_maxLength_, 0, 1)
        self.assertArgSizeInResult(NSInputStream.read_maxLength_, 0)

        self.assertResultIsBOOL(NSInputStream.hasBytesAvailable)

        self.assertArgHasType(NSOutputStream.write_maxLength_, 0, b'n^v')
        self.assertArgSizeInArg(NSOutputStream.write_maxLength_, 0, 1)
        self.assertResultIsBOOL(NSOutputStream.hasSpaceAvailable)

        b = NSOutputStream.alloc().initToMemory()
        self.assertArgHasType(b.initToFileAtPath_append_, 1, objc._C_NSBOOL)
        self.assertArgHasType(NSOutputStream.outputStreamToFileAtPath_append_, 1, objc._C_NSBOOL)

        self.assertArgHasType(b.initToBuffer_capacity_, 0, b'o^v')
        self.assertArgSizeInArg(b.initToBuffer_capacity_, 0, 1)
        self.assertArgHasType(NSOutputStream.outputStreamToBuffer_capacity_, 0, b'o^v')
        self.assertArgSizeInArg(NSOutputStream.outputStreamToBuffer_capacity_, 0, 1)

    def testDelegate(self):
        self.assertArgHasType(TestNSStreamHelper.stream_handleEvent_, 1, objc._C_NSUInteger)

    @min_os_level('10.6')
    def testMethods10_6(self):
        b = NSOutputStream.alloc()
        try:
            self.assertArgIsBOOL(b.initWithURL_append_, 1)
        finally:
            b = b.initToMemory()
        self.assertArgIsBOOL(NSOutputStream.outputStreamWithURL_append_, 1)

if __name__ == '__main__':
    main()
