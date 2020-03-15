import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDateComponentsFormatter(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStylePositional, 0)
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStyleAbbreviated, 1)
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStyleShort, 2)
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStyleFull, 3)
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStyleSpellOut, 4)
        self.assertEqual(Foundation.NSDateComponentsFormatterUnitsStyleBrief, 5)

        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorNone, 0
        )
        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDefault, 1 << 0
        )
        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropLeading,
            1 << 1,
        )
        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle, 1 << 2
        )
        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing,
            1 << 3,
        )
        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropAll,
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropLeading
            | Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle
            | Foundation.NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing,
        )

        self.assertEqual(
            Foundation.NSDateComponentsFormatterZeroFormattingBehaviorPad, 1 << 16
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            Foundation.NSDateComponentsFormatter.allowsFractionalUnits
        )
        self.assertArgIsBOOL(
            Foundation.NSDateComponentsFormatter.setAllowsFractionalUnits_, 0
        )
        self.assertResultIsBOOL(
            Foundation.NSDateComponentsFormatter.collapsesLargestUnit
        )
        self.assertArgIsBOOL(
            Foundation.NSDateComponentsFormatter.setCollapsesLargestUnit_, 0
        )
        self.assertResultIsBOOL(
            Foundation.NSDateComponentsFormatter.includesApproximationPhrase
        )
        self.assertArgIsBOOL(
            Foundation.NSDateComponentsFormatter.setIncludesApproximationPhrase_, 0
        )
        self.assertResultIsBOOL(
            Foundation.NSDateComponentsFormatter.includesTimeRemainingPhrase
        )
        self.assertArgIsBOOL(
            Foundation.NSDateComponentsFormatter.setIncludesTimeRemainingPhrase_, 0
        )

        self.assertResultIsBOOL(
            Foundation.NSDateComponentsFormatter.getObjectValue_forString_errorDescription_
        )
        self.assertArgIsOut(
            Foundation.NSDateComponentsFormatter.getObjectValue_forString_errorDescription_,
            0,
        )
        self.assertArgIsOut(
            Foundation.NSDateComponentsFormatter.getObjectValue_forString_errorDescription_,
            2,
        )
