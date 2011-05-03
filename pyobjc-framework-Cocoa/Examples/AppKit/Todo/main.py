from AppKit import *
from PyObjCTools import AppHelper
objc.setVerbose(1)

# Import all submodules,  to make sure all
# classes are known to the runtime
import CalendarMatrix
import InfoWindowController
import SelectionNotifyMatrix
import ToDoCell
import ToDoDocument
import ToDoItem
import TodoAppDelegate

AppHelper.runEventLoop()
