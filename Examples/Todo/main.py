import sys
import os
path = [ os.path.split(sys.argv[0])[0] ]
print path
path.extend(sys.path)
sys.path = path
import objc
from AppKit import *

# Import all submodules,  to make sure all 
# classes are known to the runtime
import CalendarMatrix
import InfoWindowController
import SelectionNotifyMatrix
import ToDoCell
import ToDoDocument
import ToDoItem
import TodoAppDelegate

print objc.lookUpClass('ToDoDocument')

NSApplicationMain(sys.argv)
