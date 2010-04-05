
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSOpen (TestCase):
    def testConstants(self):
        self.assertEqual(kLSLaunchDefaults, 0x00000001)
        self.assertEqual(kLSLaunchAndPrint, 0x00000002)
        self.assertEqual(kLSLaunchReserved2, 0x00000004)
        self.assertEqual(kLSLaunchReserved3, 0x00000008)
        self.assertEqual(kLSLaunchReserved4, 0x00000010)
        self.assertEqual(kLSLaunchReserved5, 0x00000020)
        self.assertEqual(kLSLaunchAndDisplayErrors, 0x00000040)
        self.assertEqual(kLSLaunchInhibitBGOnly, 0x00000080)
        self.assertEqual(kLSLaunchDontAddToRecents, 0x00000100)
        self.assertEqual(kLSLaunchDontSwitch, 0x00000200)
        self.assertEqual(kLSLaunchNoParams, 0x00000800)
        self.assertEqual(kLSLaunchAsync, 0x00010000)
        self.assertEqual(kLSLaunchStartClassic, 0x00020000)
        self.assertEqual(kLSLaunchInClassic, 0x00040000)
        self.assertEqual(kLSLaunchNewInstance, 0x00080000)
        self.assertEqual(kLSLaunchAndHide, 0x00100000)
        self.assertEqual(kLSLaunchAndHideOthers, 0x00200000)
        self.assertEqual(kLSLaunchHasUntrustedContents, 0x00400000)

    def testStructs(self):
        pass


        
    def testIncomplete(self):
        self.fail("Add header tests for <LaunchServices/LSOpen.h>")

if __name__ == "__main__":
    main()
