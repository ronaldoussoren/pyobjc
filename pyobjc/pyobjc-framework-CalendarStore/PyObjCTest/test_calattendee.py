
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalAttendee (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(CalAttendeeStatusNeedsAction, unicode)
        self.failUnlessIsInstance(CalAttendeeStatusAccepted, unicode)
        self.failUnlessIsInstance(CalAttendeeStatusDeclined, unicode)
        self.failUnlessIsInstance(CalAttendeeStatusTentative, unicode)

if __name__ == "__main__":
    main()
