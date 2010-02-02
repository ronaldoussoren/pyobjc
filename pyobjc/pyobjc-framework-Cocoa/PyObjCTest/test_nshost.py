from PyObjCTools.TestSupport import *
from PyObjCTest.testhelper import PyObjC_TestClass3
from Foundation import NSHost

class TestNSHost (TestCase):
    def testCreation(self):
        #
        # This gives an exception on GNUstep:
        #   NSRecursiveLockException - unlock: failed to unlock mutex
        #
        # testIndirectCreation performs the same operation from Objective-C
        # and doesn't fail. I don't see any significant differences in the
        # implementation of -hostWithAddress: and -hostWithName: yet the latter
        # does not have the problem we're seeing here.
        #
        o = NSHost.hostWithAddress_(u'127.0.0.1')
        self.assertEqual(o.addresses(), (u'127.0.0.1',))
        self.assertEqual(o.address(), u'127.0.0.1')

    def testCreation2(self):
        o = NSHost.hostWithName_(u'localhost')
        l = list(o.addresses())
        l.sort()
        #self.assert_(l in ([u'127.0.0.1', u'::1'], [u'127.0.0.1']))
        self.assertEqual(o.address(), o.addresses()[0])

    def testIndirectCreation(self):
        o = PyObjC_TestClass3.createAHostWithAddress_(u'127.0.0.1')
        self.assertEqual(o.address(), u'127.0.0.1')

    def testMethods(self):
        self.assertArgIsBOOL(NSHost.setHostCacheEnabled_, 0)
        self.assertResultIsBOOL(NSHost.isHostCacheEnabled)
        self.assertResultIsBOOL(NSHost.isEqualToHost_)

if __name__ == "__main__":
    main()
