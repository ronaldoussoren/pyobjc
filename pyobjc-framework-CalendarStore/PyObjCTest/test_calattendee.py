
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalAttendee (TestCase):
    def testConstants(self):
        self.assertIsInstance(CalAttendeeStatusNeedsAction, unicode)
        self.assertIsInstance(CalAttendeeStatusAccepted, unicode)
        self.assertIsInstance(CalAttendeeStatusDeclined, unicode)
        self.assertIsInstance(CalAttendeeStatusTentative, unicode)

if __name__ == "__main__":
    main()
