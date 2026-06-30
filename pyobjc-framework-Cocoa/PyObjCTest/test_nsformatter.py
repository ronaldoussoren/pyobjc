import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSFormattingContext)
        self.assertEqual(Foundation.NSFormattingContextUnknown, 0)
        self.assertEqual(Foundation.NSFormattingContextDynamic, 1)
        self.assertEqual(Foundation.NSFormattingContextStandalone, 2)
        self.assertEqual(Foundation.NSFormattingContextListItem, 3)
        self.assertEqual(Foundation.NSFormattingContextBeginningOfSentence, 4)
        self.assertEqual(Foundation.NSFormattingContextMiddleOfSentence, 5)

        self.assertIsEnumType(Foundation.NSFormattingUnitStyle)
        self.assertEqual(Foundation.NSFormattingUnitStyleShort, 1)
        self.assertEqual(Foundation.NSFormattingUnitStyleMedium, 2)
        self.assertEqual(Foundation.NSFormattingUnitStyleLong, 3)

    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSFormatter.getObjectValue_forString_errorDescription_
        )
        self.assertArgIsOut(
            Foundation.NSFormatter.getObjectValue_forString_errorDescription_, 0
        )
        self.assertArgIsOut(
            Foundation.NSFormatter.getObjectValue_forString_errorDescription_, 2
        )

        self.assertResultIsBOOL(
            Foundation.NSFormatter.isPartialStringValid_newEditingString_errorDescription_
        )
        self.assertArgIsInOut(
            Foundation.NSFormatter.isPartialStringValid_newEditingString_errorDescription_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSFormatter.isPartialStringValid_newEditingString_errorDescription_,
            2,
        )

        self.assertResultIsBOOL(
            Foundation.NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_  # noqa: B950
        )
        self.assertArgIsInOut(
            Foundation.NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_,  # noqa: B950
            0,
        )
        self.assertArgIsInOut(
            Foundation.NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            Foundation.NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_,  # noqa: B950
            4,
        )
