# Import all submodules,  to make sure all
# classes are known to the runtime
import CalendarMatrix  # noqa: F401
import InfoWindowController  # noqa: F401
import SelectionNotifyMatrix  # noqa: F401
import TodoAppDelegate  # noqa: F401
import ToDoCell  # noqa: F401
import ToDoDocument  # noqa: F401
import ToDoItem  # noqa: F401
from PyObjCTools import AppHelper

AppHelper.runEventLoop()
