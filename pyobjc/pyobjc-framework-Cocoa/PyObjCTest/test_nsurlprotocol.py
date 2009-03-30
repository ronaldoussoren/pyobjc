from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLProtocol (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSURLProtocol.canInitWithRequest_)
        self.failUnlessResultIsBOOL(NSURLProtocol.requestIsCacheEquivalent_toRequest_)
        self.failUnlessResultIsBOOL(NSURLProtocol.registerClass_)

if __name__ == "__main__":
    main()
