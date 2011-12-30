from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSProxyHelper (NSObject):
    def allowsWeakReference(self): return 0
    def retainWeakReference(self): return 0



class TestNSProxy (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSProxy.respondsToSelector_)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(TestNSProxyHelper.allowsWeakReference)
        self.assertResultIsBOOL(TestNSProxyHelper.retainWeakReference)


if __name__ == "__main__":
    main()
