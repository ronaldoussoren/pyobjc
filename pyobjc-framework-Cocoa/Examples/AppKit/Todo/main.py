# Import all submodules,  to make sure all
# classes are known to the runtime
import CalendarMatrix
import InfoWindowController
import objc
import SelectionNotifyMatrix
import TodoAppDelegate
import ToDoCell
import ToDoDocument
import ToDoItem
from PyObjCTools import AppHelper

objc.setVerbose(1)


AppHelper.runEventLoop()
