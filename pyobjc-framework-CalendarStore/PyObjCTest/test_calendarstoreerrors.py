
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalendarStoreErrors (TestCase):
    def testConstants(self):
        self.assertEqual(CalCalendarNotEditableError, 1025)
        self.assertEqual(CalDateInvalidError, 1026)
        self.assertEqual(CalCalendarNotInRepository, 1027)
        self.assertEqual(CalCalendarTitleNotUniqueError, 1028)

if __name__ == "__main__":
    main()
