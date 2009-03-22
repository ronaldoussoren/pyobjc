from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSStepperCell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSStepperCell.valueWraps)
        self.failUnlessArgIsBOOL(NSStepperCell.setValueWraps_, 0)
        self.failUnlessResultIsBOOL(NSStepperCell.autorepeat)
        self.failUnlessArgIsBOOL(NSStepperCell.setAutorepeat_, 0)

if __name__ == "__main__":
    main()
