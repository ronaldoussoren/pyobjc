from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLProtocol (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSURLProtocol.canInitWithRequest_)
        self.assertResultIsBOOL(NSURLProtocol.requestIsCacheEquivalent_toRequest_)
        self.assertResultIsBOOL(NSURLProtocol.registerClass_)

if __name__ == "__main__":
    main()
