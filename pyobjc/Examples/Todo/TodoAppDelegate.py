from Foundation import NSObject
from InfoWindowController import InfoWindowController
from PyObjCTools.NibClassBuilder import AutoBaseClass

class ToDoAppDelegate (AutoBaseClass):
    def showInfo_(self, sender):
        InfoWindowController.sharedInfoWindowController().showWindow_(sender)
