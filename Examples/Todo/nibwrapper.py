# THIS FILE IS GENERATED. DO NOT EDIT!!!
# Interface classes for using NIB files

from objc import IBOutlet
from Foundation import NSObject
from AppKit import NSDocument, NSMatrix, NSWindowController

class ToDoAppDelegateBase (NSObject):
	"Base class for class 'ToDoAppDelegate'"
	def showInfo_(self, sender): pass


class ToDoDocumentBase (NSDocument):
	"Base class for class 'ToDoDocument'"
	calendar = IBOutlet("calendar")
	itemList = IBOutlet("itemList")
	dayLabel = IBOutlet("dayLabel")
	statusList = IBOutlet("statusList")

	def itemStatusClicked_(self, sender): pass


class InfoWindowControllerBase (NSWindowController):
	"Base class for class 'InfoWindowController'"
	infoWindowViews = IBOutlet("infoWindowViews")
	infoItem = IBOutlet("infoItem")
	reschedView = IBOutlet("reschedView")
	infoNotifyMinute = IBOutlet("infoNotifyMinute")
	infoPopUp = IBOutlet("infoPopUp")
	infoNotifyOtherHours = IBOutlet("infoNotifyOtherHours")
	notesView = IBOutlet("notesView")
	dummyView = IBOutlet("dummyView")
	infoNotifyHour = IBOutlet("infoNotifyHour")
	infoDate = IBOutlet("infoDate")
	notifyView = IBOutlet("notifyView")
	infoSchedMatrix = IBOutlet("infoSchedMatrix")
	infoSchedDate = IBOutlet("infoSchedDate")
	infoSchedComplete = IBOutlet("infoSchedComplete")
	infoNotifyAMPM = IBOutlet("infoNotifyAMPM")
	infoNotifySwitchMatrix = IBOutlet("infoNotifySwitchMatrix")
	infoNotes = IBOutlet("infoNotes")

	def swapInfoWindowView_(self, sender): pass

	def switchClicked_(self, sender): pass


class CalendarMatrixBase (NSMatrix):
	"Base class for class 'CalendarMatrix'"
	monthName = IBOutlet("monthName")
	lastMonthButton = IBOutlet("lastMonthButton")
	nextMonthButton = IBOutlet("nextMonthButton")

	def choseDay_(self, sender): pass

	def monthChanged_(self, sender): pass


class SelectionNotifyMatrixBase (NSMatrix):
	"Base class for class 'SelectionNotifyMatrix'"
	pass

