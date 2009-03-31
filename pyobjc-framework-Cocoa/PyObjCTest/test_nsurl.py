from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURL (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSURL.initFileURLWithPath_isDirectory_, 1)
        self.failUnlessArgIsBOOL(NSURL.fileURLWithPath_isDirectory_, 1)

        self.failUnlessArgIsBOOL(NSURL.resourceDataUsingCache_, 0)
        self.failUnlessArgIsBOOL(NSURL.loadResourceDataNotifyingClient_usingCache_, 1)
        self.failUnlessResultIsBOOL(NSURL.setResourceData_)
        self.failUnlessResultIsBOOL(NSURL.setProperty_forKey_)
        self.failUnlessArgIsBOOL(NSURL.URLHandleUsingCache_, 0)

if __name__ == "__main__":
    main()
