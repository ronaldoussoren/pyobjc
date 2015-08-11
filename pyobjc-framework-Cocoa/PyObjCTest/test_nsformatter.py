from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSFormatter (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSFormattingContextUnknown, 0)
        self.assertEqual(NSFormattingContextDynamic, 1)
        self.assertEqual(NSFormattingContextStandalone, 2)
        self.assertEqual(NSFormattingContextListItem, 3)
        self.assertEqual(NSFormattingContextBeginningOfSentence, 4)
        self.assertEqual(NSFormattingContextMiddleOfSentence, 5)

        self.assertEqual(NSFormattingUnitStyleShort, 1)
        self.assertEqual(NSFormattingUnitStyleMedium, 2)
        self.assertEqual(NSFormattingUnitStyleLong, 3)


    def testMethods(self):
        self.assertResultIsBOOL(NSFormatter.getObjectValue_forString_errorDescription_)
        self.assertArgIsOut(NSFormatter.getObjectValue_forString_errorDescription_, 0)
        self.assertArgIsOut(NSFormatter.getObjectValue_forString_errorDescription_, 2)

        self.assertResultIsBOOL(NSFormatter.isPartialStringValid_newEditingString_errorDescription_)
        self.assertArgIsInOut(NSFormatter.isPartialStringValid_newEditingString_errorDescription_, 1)
        self.assertArgIsOut(NSFormatter.isPartialStringValid_newEditingString_errorDescription_, 2)

        self.assertResultIsBOOL(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_)
        self.assertArgIsInOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 0)
        self.assertArgIsInOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 1)
        self.assertArgIsOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 4)


if __name__ == "__main__":
    main()
