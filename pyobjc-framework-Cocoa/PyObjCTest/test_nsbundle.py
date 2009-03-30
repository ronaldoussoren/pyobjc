from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation

class TestNSBundle (TestCase):
    def testOutput(self):
        obj = NSBundle.mainBundle()

        m = obj.preflightAndReturnError_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))

        m = obj.loadAndReturnError_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))

    def testMethods(self):
        b = NSBundle.mainBundle()
        # Test on an instance because NSBundle has class methods
        # that interfere with this test
        self.failUnlessResultIsBOOL(b.load)
        self.failUnlessResultIsBOOL(b.isLoaded)
        self.failUnlessResultIsBOOL(b.unload)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSBundle.preflightAndReturnError_)
        self.failUnlessArgIsOut(NSBundle.preflightAndReturnError_, 0)
        self.failUnlessResultIsBOOL(NSBundle.loadAndReturnError_)
        self.failUnlessArgIsOut(NSBundle.loadAndReturnError_, 0)

    def testConstants(self):
        self.assertEquals(NSBundleExecutableArchitectureI386, 0x00000007)
        self.assertEquals(NSBundleExecutableArchitecturePPC, 0x00000012)
        self.assertEquals(NSBundleExecutableArchitectureX86_64, 0x01000007)
        self.assertEquals(NSBundleExecutableArchitecturePPC64, 0x01000012)

        self.failUnless( isinstance(NSBundleDidLoadNotification, unicode) )
        self.failUnless( isinstance(NSLoadedClasses, unicode) )

    def testDefines(self):
        self.failUnless(hasattr(Foundation, 'NSLocalizedString'))
        self.failUnless(hasattr(Foundation, 'NSLocalizedStringFromTable'))
        self.failUnless(hasattr(Foundation, 'NSLocalizedStringFromTableInBundle'))
        self.failUnless(hasattr(Foundation, 'NSLocalizedStringWithDefaultValue'))



if __name__ == "__main__":
    main()
