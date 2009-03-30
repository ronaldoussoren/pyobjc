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
        self.failUnlessEqual(NSStreamStatusNotOpen, 0)
        self.failUnlessEqual(NSStreamStatusOpening, 1)
        self.failUnlessEqual(NSStreamStatusOpen, 2)
        self.failUnlessEqual(NSStreamStatusReading, 3)
        self.failUnlessEqual(NSStreamStatusWriting, 4)    
        self.failUnlessEqual(NSStreamStatusAtEnd, 5)
        self.failUnlessEqual(NSStreamStatusClosed, 6)
        self.failUnlessEqual(NSStreamStatusError, 7)

        self.failUnlessEqual(NSStreamEventNone, 0)
        self.failUnlessEqual(NSStreamEventOpenCompleted, 1 << 0)
        self.failUnlessEqual(NSStreamEventHasBytesAvailable, 1 << 1)
        self.failUnlessEqual(NSStreamEventHasSpaceAvailable, 1 << 2)
        self.failUnlessEqual(NSStreamEventErrorOccurred, 1 << 3)
        self.failUnlessEqual(NSStreamEventEndEncountered, 1 << 4)

        self.failUnlessIsInstance(NSStreamSocketSecurityLevelKey, unicode)
        self.failUnlessIsInstance(NSStreamSocketSecurityLevelNone, unicode)
        self.failUnlessIsInstance(NSStreamSocketSecurityLevelSSLv2, unicode)
        self.failUnlessIsInstance(NSStreamSocketSecurityLevelSSLv3, unicode)
        self.failUnlessIsInstance(NSStreamSocketSecurityLevelTLSv1, unicode)
        self.failUnlessIsInstance(NSStreamSocketSecurityLevelNegotiatedSSL, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyConfigurationKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyHostKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyPortKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyVersionKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyUserKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyPasswordKey, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyVersion4, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSProxyVersion5, unicode)
        self.failUnlessIsInstance(NSStreamDataWrittenToMemoryStreamKey, unicode)
        self.failUnlessIsInstance(NSStreamFileCurrentOffsetKey, unicode)
        self.failUnlessIsInstance(NSStreamSocketSSLErrorDomain, unicode)
        self.failUnlessIsInstance(NSStreamSOCKSErrorDomain, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSStream.setProperty_forKey_)

        self.failUnlessArgHasType(NSInputStream.read_maxLength_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSInputStream.read_maxLength_, 0, 1)
        self.failUnlessArgSizeInResult(NSInputStream.read_maxLength_, 0)

        self.failUnlessResultIsBOOL(NSInputStream.hasBytesAvailable)

        self.failUnlessArgHasType(NSOutputStream.write_maxLength_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSOutputStream.write_maxLength_, 0, 1)
        self.failUnlessResultIsBOOL(NSOutputStream.hasSpaceAvailable)

        b = NSOutputStream.alloc().initToMemory()
        self.failUnlessArgHasType(b.initToFileAtPath_append_, 1, objc._C_NSBOOL)
        self.failUnlessArgHasType(NSOutputStream.outputStreamToFileAtPath_append_, 1, objc._C_NSBOOL)

        self.failUnlessArgHasType(b.initToBuffer_capacity_, 0, 'o^v')
        self.failUnlessArgSizeInArg(b.initToBuffer_capacity_, 0, 1)
        self.failUnlessArgHasType(NSOutputStream.outputStreamToBuffer_capacity_, 0, 'o^v')
        self.failUnlessArgSizeInArg(NSOutputStream.outputStreamToBuffer_capacity_, 0, 1)

    def testDelegate(self):
        self.failUnlessArgHasType(TestNSStreamHelper.stream_handleEvent_, 1, objc._C_NSUInteger)

if __name__ == '__main__':
    main()
