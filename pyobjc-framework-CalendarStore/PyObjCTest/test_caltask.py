
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalTask (TestCase):
    def testConstants(self):
        self.assertEqual(CalPriorityNone, 0)
        self.assertEqual(CalPriorityHigh, 1)
        self.assertEqual(CalPriorityMedium, 5)
        self.assertEqual(CalPriorityLow, 9)

    def testMethods(self):
        self.assertResultIsBOOL(CalTask.isCompleted)
        self.assertArgIsBOOL(CalTask.setIsCompleted_, 0)


if __name__ == "__main__":
    main()
