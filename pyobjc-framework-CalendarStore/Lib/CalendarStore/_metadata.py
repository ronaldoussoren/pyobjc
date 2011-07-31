# Generated file, don't edit
# Source: BridgeSupport/CalendarStore.bridgesupport
# Last update: Sun Jul 31 21:44:19 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$CalAlarmActionDisplay$CalAlarmActionEmail$CalAlarmActionProcedure$CalAlarmActionSound$CalAttendeeStatusAccepted$CalAttendeeStatusDeclined$CalAttendeeStatusNeedsAction$CalAttendeeStatusTentative$CalCalendarStoreErrorDomain$CalCalendarTypeBirthday$CalCalendarTypeCalDAV$CalCalendarTypeIMAP$CalCalendarTypeLocal$CalCalendarTypeSubscription$CalCalendarTypeExchange$CalCalendarsChangedExternallyNotification$CalCalendarsChangedNotification$CalDeletedRecordsKey$CalEventsChangedExternallyNotification$CalEventsChangedNotification$CalInsertedRecordsKey$CalSenderProcessIDKey$CalTasksChangedExternallyNotification$CalTasksChangedNotification$CalUpdatedRecordsKey$CalUserUIDKey$'''
constants_dict = {'CalDefaultRecurrenceInterval': sel32or64('I', 'Q')}
enums = '''$CalCalendarNotEditableError@1025$CalCalendarNotInRepository@1027$CalCalendarTitleNotUniqueError@1028$CalDateInvalidError@1026$CalPriorityHigh@1$CalPriorityLow@9$CalPriorityMedium@5$CalPriorityNone@0$CalRecurrenceDaily@0$CalRecurrenceMonthly@2$CalRecurrenceWeekly@1$CalRecurrenceYearly@3$CalSpanAllEvents@2$CalSpanFutureEvents@1$CalSpanThisEvent@0$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('CalCalendarItem', b'hasAlarm', {'retval': {'type': b'Z'}})
    r('CalCalendarStore', b'removeCalendar:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('CalCalendarStore', b'removeEvent:span:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('CalCalendarStore', b'removeTask:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('CalCalendarStore', b'saveCalendar:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('CalCalendarStore', b'saveEvent:span:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('CalCalendarStore', b'saveTask:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('CalEvent', b'isAllDay', {'retval': {'type': b'Z'}})
    r('CalEvent', b'setIsAllDay:', {'arguments': {2: {'type': b'Z'}}})
    r('CalEvent', b'isDetached', {'retval': {'type': b'Z'}})
    r('CalRecurrenceEnd', b'usesEndDate', {'retval': {'type': b'Z'}})
    r('CalTask', b'isCompleted', {'retval': {'type': b'Z'}})
    r('CalTask', b'setIsCompleted:', {'arguments': {2: {'type': b'Z'}}})
    r('CalCalendar', b'isEditable', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
