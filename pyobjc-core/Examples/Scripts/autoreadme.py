#!/usr/bin/python
"""
This script is a daemon that will open the ReadMe file in the root of any
(removable) volume that is inserted while this script is running.

The script is part of an article at MAcDevCenter:
    http://www.macdevcenter.com/pub/a/mac/2003/01/31/pyobjc_one.html

Usage:
    python autoreadme.py
"""
import os
import re

from Cocoa import NSObject, NSLog, NSWorkspace, NSWorkspaceDidMountNotification
from PyObjCTools import AppHelper

readTheseFiles = re.compile(r"(.*read\s*me.*|.*release.*note.*|^about.*)", re.I)


class NotificationHandler(NSObject):
    """
    Class that handles the mount notifications
    """

    def handleMountNotification_(self, aNotification):
        # Find the path to the just inserted volume
        path = aNotification.userInfo()["NSDevicePath"]

        for fname in os.listdir(path):
            if readTheseFiles.match(fname):
                # Found a readme file, try to open it using the Workspace API

                fullPath = os.path.join(path, fname)
                success, app, _ = workspace.getInfoForFile_application_type_(fullPath)
                if not success:
                    NSLog("Failed to find application to open file %s", fullPath)
                    return
                workspace.openFile_withApplication_(fullPath, app)


# Create an instance of our notification handler, and ask the workspace
# notification center to tell us when a new volume is mounted.
workspace = NSWorkspace.sharedWorkspace()
notificationCenter = workspace.notificationCenter()
notificationHandler = NotificationHandler.new()
notificationCenter.addObserver_selector_name_object_(
    notificationHandler,
    "handleMountNotification:",
    NSWorkspaceDidMountNotification,
    None,
)

NSLog("Listening for mount notifications....")
AppHelper.runConsoleEventLoop()
