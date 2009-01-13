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
