from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLConnection (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLConnection.canHandleRequest_)

        self.failUnlessArgIsBOOL(NSURLConnection.initWithRequest_delegate_startImmediately_, 2)

        self.failUnlessArgIsOut(NSURLConnection.sendSynchronousRequest_returningResponse_error_, 1)
        self.failUnlessArgIsOut(NSURLConnection.sendSynchronousRequest_returningResponse_error_, 2)

if __name__ == "__main__":
    main()
