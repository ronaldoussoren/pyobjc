from Foundation import *
import objc

# enum ToDoItemStatus
INCOMPLETE=0
COMPLETE=1
DEFER_TO_NEXT_DAY=2

SECS_IN_MINUTE=60
SECS_IN_HOUR=SECS_IN_MINUTE*60
SECS_IN_DAY=SECS_IN_HOUR*24
SECS_IN_WEEK=SECS_IN_DAY*7

class ToDoItem (NSObject):
    __slots__ = (
        '_day',
        '_itemName',
        '_notes',
        '_timer',
        '_secsUntilDue',
        '_secsUntilNotify',
        '_status',
    )

    def init(self):
        self = NSObject.init(self)
        if not self:
            return None

        self._day = None
        self._itemName = None
        self._notes = None
        self._secsUntilDue = 0
        self._secsUntilNotify = 0
        self._status = None
        self._timer = None

    def description(self):
        descr = """%s
\tName: %s
\tNotes: %s
\tCompleted: %s
\tSecs Until Due: %d
\tSecs Until Notify: %d
"""%(
            super.description(),
            self.itemName(),
            self._day,
            self._notes,
            ['No', 'YES'][self.status() == COMPLETE],
            self._secsUntilDue,
            self._secsUntilNotify)
        return descr

    def initWithName_andDate_(self, aName, aDate):
        self = NSObject.init(self)
        if not self:
            return None

        self._day = None
        self._itemName = None
        self._notes = None
        self._secsUntilDue = 0
        self._secsUntilNotify = 0
        self._status = None
        self._timer = None

        if not aName:
            return None

        self.setItemName_(aName)

        if aDate:
            self.setDay_(aDate)
        else:
            now = NSCalendarDate.date()

            self.setDay_(
                NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                now.yearOfCommonEra(), now.monthOfYear(), now.dayOfMonth(), 0, 0, 0,
                NSTimeZone.localTimeZone()))
        self.setStatus_(INCOMPLETE)
        self.setNotes_("")
        return self

    def encodeWithCoder_(self, coder):

        coder.encodeObject_(self._day)
        coder.encodeObject_(self._itemName)
        coder.encodeObject_(self._notes)

        tempTime = self._secsUntilDue
        coder.encodeValueOfObjCType_at_(objc._C_LNG, tempTime)

        tempTime = self._secsUntilNotify
        coder.encodeValueOfObjCType_at_(objc._C_LNG, tempTime)

        tempStatus = self._status
        coder.encodeValueOfObjCType_at_(objc._C_INT, tempStatus)

    def initWithCoder_(self, coder):

        self.setDay_(coder.decodeObject())
        self.setItemName_(coder.decodeObject())
        self.setNotes_(coder.decodeObject())

        tempTime = coder.decodeObjectOfObjCType_at_(objc._C_LNG)
        self.setSecsUntilDue_(tempTime)

        tempTime = coder.decodeObjectOfObjCType_at_(objc._C_LNG)
        self.setSecsUntilNotify_(tempTime)

        tempStatus = coder.decodeObjectOfObjCType_at_(objc._C_INT)
        self.setSecsUntilNotify_(tempStatus)

        return self

    def __del__(self): # dealloc
        if self._notes:
            self._timer.invalidate()

    def setDay_(self, newDay):
        self._day = newDay

    def day(self):
        return self._day

    def setItemName_(self, newName):
        self._itemName = newName

    def itemName(self):
        return self._itemName

    def setNotes_(self, newNotes):
        self._notes = newNotes

    def notes(self):
        return self._notes

    def setTimer_(self, newTimer):
        if self._timer:
            self._timer.invalidate()

        if newTimer:
            self._timer = newTimer
        else:
            self._timer = None

    def timer(self):
        return self._timer

    def setStatus_(self, newStatus):
        self._status = newStatus

    def status(self):
        return self._status

    def setSecsUntilDue_(self, secs):
        self._secsUntilDue = secs

    def secsUntilDue(self):
        return self._secsUntilDue


    def setSecsUntilNotify_(self, secs):
        self._secsUntilNotify = secs

    def secsUntilNotify(self):
        return self._secsUntilNotify


def ConvertTimeToSeconds(hour, minute, pm):
    if hour == 12:
        hour = 0

    if pm:
        hour += 12

    return (hour * SECS_IN_HOUR) + (minute * SECS_IN_MINUTE)

def ConvertSecondsToTime(secs):
    pm = 0

    hour = secs / SECS_IN_HOUR
    if hour > 11:
        hour -= 12
        pm = 1

    if hour == 0:
        hour = 12

    minute = (secs % SECS_IN_HOUR) / SECS_IN_MINUTE

    return (hour, minute, pm)
