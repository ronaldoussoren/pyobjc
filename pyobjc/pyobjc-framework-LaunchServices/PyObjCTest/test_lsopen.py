
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSOpen (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kLSLaunchDefaults, 0x00000001)
        self.failUnlessEqual(kLSLaunchAndPrint, 0x00000002)
        self.failUnlessEqual(kLSLaunchReserved2, 0x00000004)
        self.failUnlessEqual(kLSLaunchReserved3, 0x00000008)
        self.failUnlessEqual(kLSLaunchReserved4, 0x00000010)
        self.failUnlessEqual(kLSLaunchReserved5, 0x00000020)
        self.failUnlessEqual(kLSLaunchAndDisplayErrors, 0x00000040)
        self.failUnlessEqual(kLSLaunchInhibitBGOnly, 0x00000080)
        self.failUnlessEqual(kLSLaunchDontAddToRecents, 0x00000100)
        self.failUnlessEqual(kLSLaunchDontSwitch, 0x00000200)
        self.failUnlessEqual(kLSLaunchNoParams, 0x00000800)
        self.failUnlessEqual(kLSLaunchAsync, 0x00010000)
        self.failUnlessEqual(kLSLaunchStartClassic, 0x00020000)
        self.failUnlessEqual(kLSLaunchInClassic, 0x00040000)
        self.failUnlessEqual(kLSLaunchNewInstance, 0x00080000)
        self.failUnlessEqual(kLSLaunchAndHide, 0x00100000)
        self.failUnlessEqual(kLSLaunchAndHideOthers, 0x00200000)
        self.failUnlessEqual(kLSLaunchHasUntrustedContents, 0x00400000)

    def testStructs(self):
        pass


        
    def testIncomplete(self):
        self.fail("Add header tests for <LaunchServices/LSOpen.h>")

if __name__ == "__main__":
    main()
