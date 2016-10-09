from PyObjCTools.TestSupport import *
import objc
import array
import sys

from Foundation import *


class TestNSDateComponentsFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSDateComponentsFormatterUnitsStylePositional, 0)
        self.assertEqual(NSDateComponentsFormatterUnitsStyleAbbreviated, 1)
        self.assertEqual(NSDateComponentsFormatterUnitsStyleShort, 2)
        self.assertEqual(NSDateComponentsFormatterUnitsStyleFull, 3)
        self.assertEqual(NSDateComponentsFormatterUnitsStyleSpellOut, 4)
        self.assertEqual(NSDateComponentsFormatterUnitsStyleBrief, 5)

        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorNone, 0)
        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorDefault, 1 << 0)
        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorDropLeading, 1 << 1)
        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle, 1 << 2)
        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing, 1 << 3)
        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorDropAll, NSDateComponentsFormatterZeroFormattingBehaviorDropLeading | NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle | NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing)

        self.assertEqual(NSDateComponentsFormatterZeroFormattingBehaviorPad, 1 << 16)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSDateComponentsFormatter.allowsFractionalUnits)
        self.assertArgIsBOOL(NSDateComponentsFormatter.setAllowsFractionalUnits_, 0)
        self.assertResultIsBOOL(NSDateComponentsFormatter.collapsesLargestUnit)
        self.assertArgIsBOOL(NSDateComponentsFormatter.setCollapsesLargestUnit_, 0)
        self.assertResultIsBOOL(NSDateComponentsFormatter.includesApproximationPhrase)
        self.assertArgIsBOOL(NSDateComponentsFormatter.setIncludesApproximationPhrase_, 0)
        self.assertResultIsBOOL(NSDateComponentsFormatter.includesTimeRemainingPhrase)
        self.assertArgIsBOOL(NSDateComponentsFormatter.setIncludesTimeRemainingPhrase_, 0)

        self.assertResultIsBOOL(NSDateComponentsFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSDateComponentsFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSDateComponentsFormatter.getObjectValue_forString_errorDescription_, 2)

if __name__ == '__main__':
    main( )
