
from PyObjCTools.TestSupport import *
from CalendarStore import *

try:
    unicode
except NameError:
    unicode = str

class TestCalAlarm (TestCase):
    def testConstants(self):
        self.assertIsInstance(CalAlarmActionDisplay, unicode)
        self.assertIsInstance(CalAlarmActionEmail, unicode)
        self.assertIsInstance(CalAlarmActionProcedure, unicode)
        self.assertIsInstance(CalAlarmActionSound, unicode)


if __name__ == "__main__":
    main()
