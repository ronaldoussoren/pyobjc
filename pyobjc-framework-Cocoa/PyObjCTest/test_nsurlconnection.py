from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURLConnectionHelper (NSObject):
    def connection_canAuthenticateAgainstProtectionSpace_(self, a, b): return 1
    def connectionShouldUseCredentialStorage_(self, a): return 1
    def connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_(self, a, b, c, d): return 1

class TestNSURLConnection (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLConnection.canHandleRequest_)

        self.failUnlessArgIsBOOL(NSURLConnection.initWithRequest_delegate_startImmediately_, 2)

        self.failUnlessArgIsOut(NSURLConnection.sendSynchronousRequest_returningResponse_error_, 1)
        self.failUnlessArgIsOut(NSURLConnection.sendSynchronousRequest_returningResponse_error_, 2)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(TestNSURLConnectionHelper.connection_canAuthenticateAgainstProtectionSpace_)
        self.failUnlessResultIsBOOL(TestNSURLConnectionHelper.connectionShouldUseCredentialStorage_)
        self.failUnlessArgHasType(TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSURLConnectionHelper.connection_didSendBodyData_totalBytesWritten_totalBytesExpectedToWrite_, 3, objc._C_NSInteger)

if __name__ == "__main__":
    main()
