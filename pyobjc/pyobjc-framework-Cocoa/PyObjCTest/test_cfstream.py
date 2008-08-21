import unittest
from CoreFoundation import *


class TestStream (unittest.TestCase):
    def testDummy(self):
        self.fail("CFStream tests not implemented yet")

    def testConstants(self):
        self.failUnless(kCFStreamStatusNotOpen == 0)
        self.failUnless(kCFStreamStatusOpening == 1)
        self.failUnless(kCFStreamStatusOpen == 2)
        self.failUnless(kCFStreamStatusReading == 3) 
        self.failUnless(kCFStreamStatusWriting == 4)
        self.failUnless(kCFStreamStatusAtEnd == 5)
        self.failUnless(kCFStreamStatusClosed == 6)
        self.failUnless(kCFStreamStatusError == 7)

        self.failUnless(kCFStreamEventNone == 0)
        self.failUnless(kCFStreamEventOpenCompleted == 1)
        self.failUnless(kCFStreamEventHasBytesAvailable == 2)
        self.failUnless(kCFStreamEventCanAcceptBytes == 4)
        self.failUnless(kCFStreamEventErrorOccurred == 8)
        self.failUnless(kCFStreamEventEndEncountered == 16)

        self.failUnless(kCFStreamErrorDomainCustom == -1)
        self.failUnless(kCFStreamErrorDomainPOSIX == 1)
        self.failUnless(kCFStreamErrorDomainMacOSStatus == 2)

        self.failUnless(isinstance(kCFStreamPropertyAppendToFile, unicode))
        self.failUnless(isinstance(kCFStreamPropertyFileCurrentOffset, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketNativeHandle, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemoteHostName, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemotePortNumber, unicode))




if __name__ == "__main__":
    unittest.main()
