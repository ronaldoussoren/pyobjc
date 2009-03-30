from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSFormatter (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFormatter.getObjectValue_forString_errorDescription_)
        self.failUnlessArgIsOut(NSFormatter.getObjectValue_forString_errorDescription_, 0)
        self.failUnlessArgIsOut(NSFormatter.getObjectValue_forString_errorDescription_, 2)

        self.failUnlessResultIsBOOL(NSFormatter.isPartialStringValid_newEditingString_errorDescription_)
        self.failUnlessArgIsInOut(NSFormatter.isPartialStringValid_newEditingString_errorDescription_, 1)
        self.failUnlessArgIsOut(NSFormatter.isPartialStringValid_newEditingString_errorDescription_, 2)

        self.failUnlessResultIsBOOL(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_)
        self.failUnlessArgIsInOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 0)
        self.failUnlessArgIsInOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 1)
        self.failUnlessArgIsOut(NSFormatter.isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_, 4)


if __name__ == "__main__":
    main()
