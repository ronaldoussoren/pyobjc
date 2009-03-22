from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSStepper (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSStepper.valueWraps)
        self.failUnlessArgIsBOOL(NSStepper.setValueWraps_, 0)
        self.failUnlessResultIsBOOL(NSStepper.autorepeat)
        self.failUnlessArgIsBOOL(NSStepper.setAutorepeat_, 0)


if __name__ == "__main__":
    main()
