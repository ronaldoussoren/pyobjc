
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


    def testFunctions(self):
        v = CTGetCoreTextVersion()
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
