from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSFormatter (TestCase):
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
