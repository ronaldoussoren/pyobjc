import sys
import os
import objc
from AppKit import *
from PyObjCTools.NibClassBuilder import extractClasses
from PyObjCTools import AppHelper

extractClasses('MainMenu')
extractClasses('ToDoDocument')
extractClasses('ToDoInfoWindow')

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
