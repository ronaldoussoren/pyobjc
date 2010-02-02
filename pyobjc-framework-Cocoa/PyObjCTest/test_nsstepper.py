from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSStepper (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSStepper.valueWraps)
        self.assertArgIsBOOL(NSStepper.setValueWraps_, 0)
        self.assertResultIsBOOL(NSStepper.autorepeat)
        self.assertArgIsBOOL(NSStepper.setAutorepeat_, 0)


if __name__ == "__main__":
    main()
