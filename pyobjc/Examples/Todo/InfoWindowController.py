from AppKit import *
from objc import selector, IBOutlet, NO
from ToDoDocument import *
from PyObjCTools.NibClassBuilder import AutoBaseClass

NOTIFY_TAG     = 0
RESCHEDULE_TAG = 1
NOTES_TAG      = 2

NotifyLengthNone    = 0
NotifyLengthQuarter = 1
NotifyLengthHour    = 2
NotifyLengthDay     = 3
NotifyLengthOther   = 4

_sharedInfoWindowController = None

class InfoWindowController (AutoBaseClass):

    __slots__ = ('_inspectingDocument', )

    def switchClicked_(self, sender):
        dueSecs = 0
        idx = 0
        theItem = self._inspectingDocument.selectedItem()
        if theItem is None:
            return

        if sender is self.infoNotifyAMPM:
            if self.infoNotifyHour.intValue():
                pmFlag = (self.infoNotifyAMPM.selectedRow() == 1)
                dueSecs = ConvertTimeToSeconds(
                    self.infoNotifyHour.intValue(),
                    self.infoNotifyMinute.intValue(),
                    pmFlag)
                theItem.setSecsUntilDue_(dueSecs)
        elif sender is self.infoNotifySwitchMatrix:
            idx = self.infoNotifySwitchMatrix.selectedRow()

            if not theItem:
                pass
            elif idx == NotifyLengthNone:
                theItem.setSecsUntilNotify_(0)
            elif idx == NotifyLengthQuarter:
                theItem.setSecsUntilNotify_(SECS_IN_HOUR/4)
            elif idx == NotifyLengthHour:
                theItem.setSecsUntilNotify_(SECS_IN_HOUR)
            elif idx == NotifyLengthDay:
                theItem.setSecsUntilNotify_(SECS_IN_DAY)
            elif idx == NotifyLengthOther:
                theItem.setSecsUntilNotify_(
                    infoNotifyOtherHours.intValue() *
                    SECS_IN_HOUR)
            else:
                NSLog("Error in selectedRow")
        elif sender is self.infoSchedComplete:
            if theItem:
                theItem.setStatus_(COMPLETE)
        elif sender is self.infoSchedMatrix:
            # left as an exercise in the objective-C code
            pass

        self.updateInfoWindow()
        self._inspectingDocument.selectedItemModified()

    def textDidChange_(self, notification):
        if notification.object() is self.infoNotes:
            self._inspectingDocument.selectedItem().setNotes_(self.infoNotes.string())
            self._inspectingDocument.selectItemModified()

    def textDidEndEditing_(self, notification):
        if notification.object() is self.infoNotes:
            self._inspectingDocument.selectedItem().setNotes_(infoNotes.string())
            self._inspectingDocument.selectedItemModified()



    def controlTextDidEndEditing_(self, notification):
        #print "controlTextDidEndEditing:", notification.description()
        dueSecs = 0
        theItem = self._inspectingDocument.selectedItem()
        if theItem is None:
            return

        if (notification.object() is self.infoNotifyHour) or \
           (notification.object() is self.infoNotifyMinute):

            dueSecs = ConvertTimeToSeconds(
                 self.infoNotifyHour.intValue(),
                self.infoNotifyMinute.intValue(),
                self.infoNotifyAMPM.cellAtRow_column_(1,0).state())
            #print "New dueSecs: ", dueSecs
            #theItem.setSecsUntilDue_(dueSecs)
        elif notification.object() is self.infoNotifyOtherHours:
            if self.infoNotifySwitchMatrix.selectedRow() == NotifyLengthOther:
                theItem.setSecsUntilNotify_(self.infoNotifyOtherHours.intValue() * SECS_IN_HOUR)
            else:
                return
        elif notification.object() is self.infoSchedDate:
            # Left as an exercise
            pass

        self._inspectingDocument.selectedItemModified()


    def sharedInfoWindowController(self):
        global _sharedInfoWindowController

        if not _sharedInfoWindowController:
            _sharedInfoWindowController = InfoWindowController.alloc().init()

        return _sharedInfoWindowController

    sharedInfoWindowController = selector(
        sharedInfoWindowController, isClassMethod=1)


    def init(self):
        # XXX: Not sure if the native code works correctly if the return value
        # from super != self.
        self = self.initWithWindowNibName_("ToDoInfoWindow")
        if self:
            self.setWindowFrameAutosaveName_("Info")

        return self

    def dump_outlets(self):
        print 'dummyView', self.dummyView
        print 'infoDate', self.infoDate
        print 'infoItem', self.infoItem
        print 'infoNotes', self.infoNotes
        print 'infoNotifyAMPM', self.infoNotifyAMPM
        print 'infoNotifyHour', self.infoNotifyHour
        print 'infoNotifyMinute', self.infoNotifyMinute
        print 'infoNotifyOtherHours', self.infoNotifyOtherHours
        print 'infoNotifySwitchMatrix', self.infoNotifySwitchMatrix
        print 'infoPopUp', self.infoPopUp
        print 'infoSchedComplet', self.infoSchedComplete
        print 'infoSchedDate', self.infoSchedDate
        print 'infoSchedMatrix', self.infoSchedMatrix
        print 'infoWindowViews', self.infoWindowViews
        print 'notesView', self.notesView
        print 'notifyView', self.notifyView
        print 'reschedView', self.reschedView

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

        # XXX: The calls to retain may not be necessary.
        self.notifyView.retain()
        self.notifyView.removeFromSuperview()

        self.reschedView.retain()
        self.reschedView.removeFromSuperview()

        self.notesView.retain()
        self.notesView.removeFromSuperview()

        self.infoWindowViews = None

        self.infoNotes.setDelegate_(self)
        self.swapInfoWindowView_(self)
        self.setMainWindow_(NSApp().mainWindow())
        self.updateInfoWindow()

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "mainWindowChanged:",
            NSWindowDidBecomeMainNotification,
            None)

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "mainWindowResigned:",
            NSWindowDidResignMainNotification,
            None)

        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "selectedItemChanged:",
            ToDoItemChangedNotification,
            None)



    def __del__(self): # dealloc

        NSNotificationCenter.defaultCenter().removeObserver_(self)

        # Cannot to this
        NSWindowController.dealloc(self)

    def updateInfoWindow(self):
        minute = 0
        hour = 0

        selected = self.infoPopUp.selectedItem().tag()
        selectedItem = self._inspectingDocument.selectedItem()

        if isinstance(selectedItem, ToDoItem):
            self.infoItem.setStringValue_(selectedItem.itemName())
            self.infoDate.setStringValue_(
                selectedItem.day().descriptionWithCalendarFormat_timeZone_locale_("%a, %b %d %Y", NSTimeZone.localTimeZone(), None))

            if selected == NOTIFY_TAG:
                dueSecs = selectedItem.secsUntilDue()
                hour, minutes, pmFlag = ConvertSecondsToTime(dueSecs)
                self.infoNotifyAMPM.cellAtRow_column_(0, 0).setState_(not pmFlag)
                self.infoNotifyAMPM.cellAtRow_column_(1, 0).setState_(pmFlag)
                self.infoNotifyHour.setIntValue_(hour)
                self.infoNotifyMinute.setIntValue_(minute)

                notifySecs = selectedItem.secsUntilNotify()
                clearButtonMatrix(self.infoNotifySwitchMatrix)

                if notifySecs == 0:
                    self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthNone, 0).setState_(NSOnState)
                elif notifySecs == SECS_IN_HOUR / 4:
                    self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthQuarter, 0).setState_(NSOnState)
                elif notifySecs == SECS_IN_HOUR:
                    self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthHour, 0).setState_(NSOnState)
                elif notifySecs == SECS_IN_DAY:
                    self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthDay, 0).setState_(NSOnState)
                else:
                    self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthOther, 0).setState_(NSOnState)
                    self.infoNotifyOtherHours.setIntValue_(notifySecs / SECS_IN_HOUR)
            elif selected == RESCHEDULE_TAG:
                # left as an exercise
                pass
            elif selected == NOTES_TAG:
                self.infoNotes.setString_(selectedItem.notes())
        else:
            self.infoItem.setStringValue_("")
            self.infoDate.setStringValue_("")
            self.infoNotifyHour.setStringValue_("")
            self.infoNotifyMinute.setStringValue_("")
            self.infoNotifyAMPM.cellAtRow_column_(0, 0).setState_(NSOnState)
            self.infoNotifyAMPM.cellAtRow_column_(1, 0).setState_(NSOffState)
            clearButtonMatrix(self.infoNotifySwitchMatrix)
            self.infoNotifySwitchMatrix.cellAtRow_column_(NotifyLengthNone, 0).setState_(NSOnState)
            self.infoNotifyOtherHours.setStringValue_("")
            self.infoNotes.setString_("")

    def setMainWindow_(self, mainWindow):
        if not mainWindow:
            return

        controller = mainWindow.windowController()

        if isinstance(controller.document(), ToDoDocument):
            self._inspectingDocument = controller.document()
        else:
            self._inspectingDocument = None

        self.updateInfoWindow()


    def mainWindowChanged_(self, notification):
        self.setMainWindow_(notification.object())

    def mainWindowResigned_(self, notification):
        self.setMainWindow_(None)

    def swapInfoWindowView_(self, sender):
        selected = self.infoPopUp.selectedItem().tag()

        if selected == NOTIFY_TAG:
            newView = self.notifyView
        elif selected == RESCHEDULE_TAG:
            newView = self.reschedView
        elif selected == NOTES_TAG:
            newView = self.notesView

        if self.dummyView.contentView() != newView:
            self.dummyView.setContentView_(newView)

    def selectedItemChanged_(self, notification):
        self.updateInfoWindow()


def clearButtonMatrix(matrix):
    rows, cols = matrix.getNumberOfRows_columns_()

    for i in range(rows):
        cell = matrix.cellAtRow_column_(i, 0)
        if cell: cell.setState_(NO)
