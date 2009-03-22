from Foundation import *
from InfoWindowController import InfoWindowController

class ToDoAppDelegate (NSObject):

    @objc.IBAction
    def showInfo_(self, sender):
        InfoWindowController.sharedInfoWindowController().showWindow_(sender)
