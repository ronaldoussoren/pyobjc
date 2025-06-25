import Cocoa
import objc
from objc import super  # noqa: A004
from SelectionNotifyMatrix import RowSelectedNotification
from ToDoCell import ToDoCell
from ToDoItem import ToDoItem, INCOMPLETE

ToDoItemChangedNotification = "ToDoItemChangedNotification"


class ToDoDocument(Cocoa.NSDocument):
    calendar = objc.IBOutlet()
    dayLabel = objc.IBOutlet()
    itemList = objc.IBOutlet()
    statusList = objc.IBOutlet()

    __slots__ = (
        "_dataFromFile",
        "_activeDays",
        "_currentItems",
        "_selectedItem",
        "_selectedItemEdited",
    )

    def rowSelected_(self, notification):
        row = notification.object().selectedRow()

        if row == -1:
            return

        self._selectedItem = self._currentItems.objectAtIndex_(row)

        if not isinstance(self._selectedItem, ToDoItem):
            self._selectedItem = None

        Cocoa.NSNotificationCenter.defaultCenter().postNotificationName_object_userInfo_(
            ToDoItemChangedNotification, self._selectedItem, None
        )

    def init(self):
        self = super().init()
        if self is None:
            return self
        self._activeDays = None
        self._currentItems = None
        self._selectedItem = None
        self._selectedItemEdited = 0
        self._dataFromFile = None

        return self

    def __del__(self):  # dealloc in Objective-C code
        Cocoa.NSNotificationCenter.defaultCenter().removeObserver_(self)

    def selectedItem(self):
        return self._selectedItem

    def windowNibName(self):
        return "ToDoDocument"

    def windowControllerDidLoadNib_(self, aController):
        # Cocoa.NSDocument.windowControllerDidLoadNib_(self, aController)

        self.setHasUndoManager_(0)
        self.itemList.setDelegate_(self)

        index = self.statusList.cells().count()
        while index:
            index -= 1

            aCell = ToDoCell.alloc().init()
            aCell.setTarget_(self)
            aCell.setAction_("itemStatusClicked:")
            self.statusList.putCell_atRow_column_(aCell, index, 0)

        if self._dataFromFile:
            self.loadDocWithData_(self._dataFromFile)
            self._dataFromFile = None
        else:
            self.loadDocWithData_(None)

        Cocoa.NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "rowSelected:", RowSelectedNotification, self.itemList
        )
        Cocoa.NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
            self, "rowSelected:", RowSelectedNotification, self.statusList
        )

    def loadDocWithData_(self, data):
        if data:
            dct = Cocoa.NSUnarchiver.unarchiveObjectWithData_(data)
            self.initDataModelWithDictinary_(dct)
            dayEnum = self._activeDays.keyEnumerator()
            now = Cocoa.NSDate.date()

            itemDate = dayEnum.nextObject()
            while itemDate:
                itemArray = self._activeDays.objectForKey_(itemDate)
                itemEnum = itemArray.objectEnumerator()

                anItem = itemEnum.nextObject()
                while anItem:
                    if (
                        isinstance(anItem, ToDoItem)
                        and anItem.secsUntilNotify()
                        and anItem.status() == INCOMPLETE
                    ):
                        due = anItem.day().addTimeInterfval_(anItem.secondsUntilDue())
                        elapsed = due.timeIntervalSinceDate_(now)
                        if elapsed > 0:
                            self.setTimerForItem_(anItem)
                        else:
                            Cocoa.NSBeep()
                            Cocoa.NSRunAlertPanel(
                                "To Do",
                                "%s on %s is past due!"
                                % (
                                    anItem.itemName(),
                                    due.descriptionWithCalendarFormat_timeZone_locale_(
                                        "%b %d, %Y at %I:%M %p",
                                        Cocoa.NSTimeZone.localTimeZone(),
                                        None,
                                    ),
                                ),
                                None,
                                None,
                                None,
                            )
                            anItem.setSecsUntilNotify_(0)
                    anItem = itemEnum.nextObject()

                itemDate = dayEnum.nextObject()
        else:
            self.initDataModelWithDictionary_(None)

        self.selectItemAtRow_(0)
        self.updateLists()

        self.dayLabel.setStringValue_(
            self.calendar.selectedDay().descriptionWithCalendarFormat_timeZone_locale_(
                "To Do on %a %B %d %Y", Cocoa.NSTimeZone.defaultTimeZone(), None
            )
        )

    def initDataModelWithDictionary_(self, aDict):
        if aDict:
            self._activeDays = aDict
        else:
            self._activeDays = Cocoa.NSMutableDictionary.alloc().init()

        date = self.calendar.selectedDay()
        self.setCurrentItems_(self._activeDays.objectForKey_(date))

    def setCurrentItems_(self, newItems):
        if newItems:
            self._currentItems = newItems.mutableCopy()
        else:
            numRows, numCols = self.itemList.getNumberOfRows_columns_(None, None)
            self._currentItems = Cocoa.NSMutableArray.alloc().initWithCapacity_(numRows)

            for _ in range(numRows):
                self._currentItems.addObject_("")

    def updateLists(self):
        numRows = self.itemList.cells().count()

        for i in range(numRows):
            if self._currentItems:
                thisItem = self._currentItems.objectAtIndex_(i)
            else:
                thisItem = None

            if isinstance(thisItem, ToDoItem):
                if thisItem.secsUntilDue():
                    due = thisItem.day().addTimeInterval_(thisItem.secsUntilDue())
                else:
                    due = None

                self.itemList.cellAtRow_column_(i, 0).setStringValue_(thisItem.itemName())
                self.statusList.cellAtRow_column_(i, 0).setTimeDue_(due)
                self.statusList.cellAtRow_column_(i, 0).setTriState_(thisItem.status())
            else:
                self.itemList.cellAtRow_column_(i, 0).setStringValue_("")
                self.statusList.cellAtRow_column_(i, 0).setTitle_("")
                self.statusList.cellAtRow_column_(i, 0).setImage_(None)

    def saveDocItems(self):
        if self._currentItems:
            cnt = self._currentItems.count()

            for i in range(cnt):
                anItem = self._currentItems.objectAtIndex_(i)
                if isinstance(anItem, ToDoItem):
                    self._activeDays.setObject_forKey_(self._currentItems, anItem.day())
                    break

    def controlTextDidEndEditing_(self, notif):
        if not self._selectedItemEdited:
            return

        row = self.itemList.selectedRow()
        newName = self.itemList.selectedCell().stringValue()

        if isinstance(self._currentItems.objectAtIndex_(row), ToDoItem):
            prevNameAtIndex = self._currentItems.objectAtIndex_(row).itemName()
            if newName == "":
                self._currentItems.replaceObjectAtRow_withObject_(row, "")
            elif prevNameAtIndex != newName:
                self._currentItems.objectAtRow_(row).setItemName_(newName)
        elif newName != "":
            newItem = ToDoItem.alloc().initWithName_andDate_(
                newName, self.calendar.selectedDay()
            )
            self._currentItems.replaceObjectAtIndex_withObject_(row, newItem)

        self._selectedItem = self._currentItems.objectAtIndex_(row)

        if not isinstance(self._selectedItem, ToDoItem):
            self._selectedItem = None

        self.updateLists()
        self._selectedItemEdited = 0
        self.updateChangeCount_(Cocoa.NSChangeDone)

        Cocoa.NSNotificationCenter.defaultCenter().postNotificationName_object_userInfo_(
            ToDoItemChangedNotification, self._selectedItem, None
        )

    def selectedItemModified(self):
        if self._selectedItem:
            self.setTimerForItem_(self._selectedItem)

        self.updateLists()
        self.updateChangeCount_(Cocoa.NSChangeDone)

    def calendarMatrix_didChangeToDate_(self, matrix, date):
        self.saveDocItems()

        if self._activeDays:
            self.setCurrentItems_(self._activeDays.objectForKey_(date))
        else:
            pass

        self.dayLabel.setStringValue_(
            date.descriptionWithCalendarFormat_timeZone_locale_(
                "To Do on %a %B %d %Y", Cocoa.NSTimeZone.defaultTimeZone(), None
            )
        )
        self.updateLists()
        self.selectedItemAtRow_(0)

    def selectedItemAtRow_(self, row):
        self.itemList.selectCellAtRow_column_(row, 0)

    def controlTextDidBeginEditing_(self, notif):
        self._selectedItemEdited = 1

    def dataRepresentationOfType_(self, aType):
        self.saveDocItems()

        return Cocoa.NSArchiver.archivedDataWithRootObject_(self._activeDays)

    def loadRepresentation_ofType_(self, data, aType):
        if self.calendar:
            self.loadDocWithData_(data)
        else:
            self._dataFromFile = data

        return 1

    @objc.IBAction
    def itemStatusClicked_(self, sender):
        row = sender.selectedRow()
        cell = sender.cellAtRow_column_(row, 0)
        item = self._currentItems.objectAtIndex_(row)

        if isinstance(item, ToDoItem):
            item.setStatus_(cell.triState())
            self.setTimerForItem_(item)

            self.updateLists()
            self.updateChangeCount_(Cocoa.NSChangeDone)

            Cocoa.NSNotificationCenter.defaultCenter().postNotificationName_object_userInfo_(
                ToDoItemChangedNotification, item, None
            )

    def setTimerForItem_(self, anItem):
        if anItem.secsUntilNotify() and anItem.status() == INCOMPLETE:
            notifyDate = anItem.day().addTimeInterval_(
                anItem.secsUntilDue() - anItem.secsUntilNotify()
            )

            aTimer = Cocoa.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(  # noqa: B950
                notifyDate.timeIntervalSinceNow(),
                self,
                "itemTimerFired:",
                anItem,
                False,
            )
            anItem.setTimer_(aTimer)
        else:
            anItem.setTimer_(None)

    def itemTimerFired_(self, timer):
        anItem = timer.userInfo()
        dueDate = anItem.day().addTimeInterval_(anItem.secsUntilDue())

        Cocoa.NSBeep()

        Cocoa.NSRunAlertPanel(
            "To Do",
            "%s on %s"
            % (
                anItem.itemName(),
                dueDate.descriptionWithCalendarFormat_timeZone_locale_(
                    "%b %d, %Y at %I:%M: %p", Cocoa.NSTimeZone.defaultTimeZone(), None
                ),
            ),
            None,
            None,
            None,
        )
        anItem.setSecsUntilNotify_(0)
        self.setTimerForItem_(anItem)
        self.updateLists()

        Cocoa.NSNotificationCenter.defaultCenter().postNotificationName_object_userInfo_(
            ToDoItemChangedNotification, anItem, None
        )

    def selectItemAtRow_(self, row):
        self.itemList.selectCellAtRow_column_(row, 0)
