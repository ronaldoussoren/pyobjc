
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalAlarm (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(CalAlarmActionDisplay, unicode)
        self.failUnlessIsInstance(CalAlarmActionEmail, unicode)
        self.failUnlessIsInstance(CalAlarmActionProcedure, unicode)
        self.failUnlessIsInstance(CalAlarmActionSound, unicode)


if __name__ == "__main__":
    main()
