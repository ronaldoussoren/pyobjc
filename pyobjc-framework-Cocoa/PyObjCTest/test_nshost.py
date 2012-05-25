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
        o = NSHost.hostWithAddress_(b'127.0.0.1'.decode('ascii'))
        self.assertEqual(o.addresses(), (b'127.0.0.1'.decode('ascii'),))
        self.assertEqual(o.address(), b'127.0.0.1'.decode('ascii'))

    def testCreation2(self):
        o = NSHost.hostWithName_(b'localhost'.decode('ascii'))
        l = list(o.addresses())
        l.sort()
        #self.assert_(l in ([b'127.0.0.1'.decode('ascii'), b'::1'.decode('ascii')], [b'127.0.0.1'.decode('ascii')]))
        self.assertEqual(o.address(), o.addresses()[0])

    def testIndirectCreation(self):
        o = PyObjC_TestClass3.createAHostWithAddress_(b'127.0.0.1'.decode('ascii'))
        self.assertEqual(o.address(), b'127.0.0.1'.decode('ascii'))

    def testMethods(self):
        self.assertArgIsBOOL(NSHost.setHostCacheEnabled_, 0)
        self.assertResultIsBOOL(NSHost.isHostCacheEnabled)
        self.assertResultIsBOOL(NSHost.isEqualToHost_)

if __name__ == "__main__":
    main()
