#!/usr/bin/python
import sys
import os
import re

from AppKit import NSWorkspace, NSWorkspaceDidMountNotification
from Foundation import *

workspace = NSWorkspace.sharedWorkspace()
notificationCenter = workspace.notificationCenter()

readTheseFiles = re.compile('(.*read\s*me.*|.*release.*note.*|^about.*)', re.I)

class NotificationHandler(NSObject):
    def handleMountNotification_(self, aNotification):
        path = aNotification.userInfo()['NSDevicePath']
        for aFile in os.listdir(path):
            if readTheseFiles.match(aFile):
                fullPath = os.path.join(path, aFile)
                success, app, None = workspace.getInfoForFile_application_type_(fullPath)
                if not success:
                    NSLog("Failed to find application to open file %s" % fullPath)
                    return
                workspace.openFile_withApplication_(fullPath, app)
            
notificationHandler = NotificationHandler.new()
notificationCenter.addObserver_selector_name_object_(notificationHandler,
                                                     "handleMountNotification:",
                                                     NSWorkspaceDidMountNotification,
                                                     None)

NSLog("Listening for mount notifications....")
NSRunLoop.currentRunLoop().run() # never exits
