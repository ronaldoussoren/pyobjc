from Foundation import NSObject
from InfoWindowController import InfoWindowController
from nibwrapper import ToDoAppDelegateBase

class ToDoAppDelegate (ToDoAppDelegateBase):
	def showInfo_(self, sender):
		InfoWindowController.sharedInfoWindowController().showWindow_(sender)
