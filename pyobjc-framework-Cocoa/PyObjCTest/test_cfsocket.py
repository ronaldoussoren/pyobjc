import unittest
from CoreFoundation import *


class TestSocket (unittest.TestCase):
    def testDummy(self):
        self.fail("CFSocket tests not implemented yet")


    def testTypeID(self):
        self.failUnless(isinstance(CFSocketGetTypeID(), (int, long)))

    def testConstants(self):
        self.failUnless(kCFSocketSuccess == 0)
        self.failUnless(kCFSocketError == -1)
        self.failUnless(kCFSocketTimeout == -2)

        self.failUnless(kCFSocketNoCallBack == 0)
        self.failUnless(kCFSocketReadCallBack == 1)
        self.failUnless(kCFSocketAcceptCallBack == 2)
        self.failUnless(kCFSocketDataCallBack == 3)
        self.failUnless(kCFSocketConnectCallBack == 4)
        self.failUnless(kCFSocketWriteCallBack == 8)

        self.failUnless(kCFSocketAutomaticallyReenableReadCallBack == 1)
        self.failUnless(kCFSocketAutomaticallyReenableAcceptCallBack == 2)
        self.failUnless(kCFSocketAutomaticallyReenableDataCallBack == 3)
        self.failUnless(kCFSocketAutomaticallyReenableWriteCallBack == 8)
        self.failUnless(kCFSocketCloseOnInvalidate == 128)

        self.failUnless(isinstance(kCFSocketCommandKey, unicode))
        self.failUnless(isinstance(kCFSocketNameKey, unicode))
        self.failUnless(isinstance(kCFSocketValueKey, unicode))
        self.failUnless(isinstance(kCFSocketResultKey, unicode))
        self.failUnless(isinstance(kCFSocketErrorKey, unicode))
        self.failUnless(isinstance(kCFSocketRegisterCommand, unicode))
        self.failUnless(isinstance(kCFSocketRetrieveCommand, unicode))


    def testStructs(self):
        o = CFSocketSignature()
        self.failUnless(hasattr(o, 'protocolFamily'))
        self.failUnless(hasattr(o, 'socketType'))
        self.failUnless(hasattr(o, 'protocol'))
        self.failUnless(hasattr(o, 'address'))





if __name__ == "__main__":
    unittest.main()
