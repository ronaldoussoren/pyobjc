
from PyObjCTools.TestSupport import *

from CoreText import *

class TestCoreText (TestCase):
    def testConstants(self):
        self.assertEqual(kCTVersionNumber10_5, 0x00020000)
        self.assertEqual(kCTVersionNumber10_5_2, 0x00020001)
        self.assertEqual(kCTVersionNumber10_5_3, 0x00020002)
        self.assertEqual(kCTVersionNumber10_5_5, 0x00020003)
        self.assertEqual(kCTVersionNumber10_6, 0x00030000)
        self.assertEqual(kCTVersionNumber10_7, 0x00040000)
        self.assertEqual(kCTVersionNumber10_8, 0x00050000)
        self.assertEqual(kCTVersionNumber10_9, 0x00060000)
        self.assertEqual(kCTVersionNumber10_10, 0x00070000)
        self.assertEqual(kCTVersionNumber10_11, 0x00080000)
        self.assertEqual(kCTVersionNumber10_12, 0x00090000)
        self.assertEqual(kCTVersionNumber10_13, 0x000A0000)
        self.assertEqual(kCTVersionNumber10_14, 0x000B0000)

    def testFunctions(self):
        v = CTGetCoreTextVersion()
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
