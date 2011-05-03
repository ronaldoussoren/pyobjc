from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSStepperCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSStepperCell.valueWraps)
        self.assertArgIsBOOL(NSStepperCell.setValueWraps_, 0)
        self.assertResultIsBOOL(NSStepperCell.autorepeat)
        self.assertArgIsBOOL(NSStepperCell.setAutorepeat_, 0)

if __name__ == "__main__":
    main()
