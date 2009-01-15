
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalTask (TestCase):
    def testConstants(self):
        self.failUnlessEqual(CalPriorityNone, 0)
        self.failUnlessEqual(CalPriorityHigh, 1)
        self.failUnlessEqual(CalPriorityMedium, 5)
        self.failUnlessEqual(CalPriorityLow, 9)

    def testMethods(self):
        self.failUnlessResultIsBOOL(CalTask.isCompleted)
        self.failUnlessArgIsBOOL(CalTask.setIsCompleted_, 0)


if __name__ == "__main__":
    main()
