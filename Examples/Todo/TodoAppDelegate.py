from Foundation import NSObject
from InfoWindowController import InfoWindowController

class ToDoAppDelegate (NSObject):
	def showInfo_(self, sender):
		InfoWindowController.sharedInfoWindowController().showWindow_(sender)
