
from PyObjCTools.TestSupport import *

from CoreText import *

class TestCoreText (TestCase):
    def testConstants(self):
        self.assertEqual(kCTVersionNumber10_5, 0x00020000)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCTVersionNumber10_5_2, 0x00020001)
        self.assertEqual(kCTVersionNumber10_5_3, 0x00020002)
        self.assertEqual(kCTVersionNumber10_5_5, 0x00020003)
        self.assertEqual(kCTVersionNumber10_6, 0x00030000)

    @min_os_level('10.7')
    def testConstants10_8(self):
        self.assertEqual(kCTVersionNumber10_7, 0x00040000)


    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(kCTVersionNumber10_8, 0x00050000)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertEqual(kCTVersionNumber10_9, 0x00060000)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(kCTVersionNumber10_10, 0x00070000)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(kCTVersionNumber10_11, 0x00080000)

    def testFunctions(self):
        v = CTGetCoreTextVersion()
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
