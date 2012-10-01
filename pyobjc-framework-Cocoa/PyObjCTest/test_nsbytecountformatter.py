from PyObjCTools.TestSupport import *

import Foundation

class TestNSByteCountFormatter (TestCase):
    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSByteCountFormatterUseDefault, 0)
        self.assertEqual(Foundation.NSByteCountFormatterUseBytes, 1 << 0)
        self.assertEqual(Foundation.NSByteCountFormatterUseKB, 1 << 1)
        self.assertEqual(Foundation.NSByteCountFormatterUseMB, 1 << 2)
        self.assertEqual(Foundation.NSByteCountFormatterUseGB, 1 << 3)
        self.assertEqual(Foundation.NSByteCountFormatterUseTB, 1 << 4)
        self.assertEqual(Foundation.NSByteCountFormatterUsePB, 1 << 5)
        self.assertEqual(Foundation.NSByteCountFormatterUseEB, 1 << 6)
        self.assertEqual(Foundation.NSByteCountFormatterUseZB, 1 << 7)
        self.assertEqual(Foundation.NSByteCountFormatterUseYBOrHigher, 0x0FF << 8)
        self.assertEqual(Foundation.NSByteCountFormatterUseAll, 0x0FFFF)
        self.assertEqual(Foundation.NSByteCountFormatterCountStyleFile, 0)
        self.assertEqual(Foundation.NSByteCountFormatterCountStyleMemory, 1)
        self.assertEqual(Foundation.NSByteCountFormatterCountStyleDecimal, 2)
        self.assertEqual(Foundation.NSByteCountFormatterCountStyleBinary, 3)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.allowsNonnumericFormatting)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setAllowsNonnumericFormatting_, 0)

        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.includesUnit)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setIncludesUnit_, 0)

        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.includesCount)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setIncludesCount_, 0)

        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.includesActualByteCount)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setIncludesActualByteCount_, 0)

        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.isAdaptive)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setAdaptive_, 0)

        self.assertResultIsBOOL(Foundation.NSByteCountFormatter.zeroPadsFractionDigits)
        self.assertArgIsBOOL(Foundation.NSByteCountFormatter.setZeroPadsFractionDigits_, 0)

if __name__ == "__main__":
    main()
