from AppKit import *
from Foundation import *
from PyObjCTools import NibClassBuilder, AppHelper
import objc
import os

NibClassBuilder.extractClasses("MainMenu")

SAFARI = u'com.apple.Safari'

class IDNSnitchApplicationDelegate(NibClassBuilder.AutoBaseClass):
    def applicationDidFinishLaunching_(self, sender):
        ws = NSWorkspace.sharedWorkspace()
        for app in ws.launchedApplications():
            self.attachIfSafari_(app)
        nc = ws.notificationCenter()
        nc.addObserver_selector_name_object_(
            self,
            'applicationLaunched:',
            NSWorkspaceDidLaunchApplicationNotification,
            None)

    def applicationLaunched_(self, aNotification):
        # give Safari some time to launch.. otherwise it will be unhappy
        NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            2.0,
            self,
            'delayedAttachIfSafari:',
            aNotification.userInfo(),
            False)

    def delayedAttachIfSafari_(self, aTimer):
        self.attachIfSafari_(aTimer.userInfo())
    
    def attachIfSafari_(self, userInfo):
        if userInfo.get(u'NSApplicationBundleIdentifier') != SAFARI:
            return
        pid = userInfo['NSApplicationProcessIdentifier']
        path = NSBundle.mainBundle().pathForResource_ofType_(u'IDNSnitchPlugin', u'plugin')
        if path is None:
            NSLog(u'Could not find plugin')
            return
        path = os.path.join(path, u'Contents', u'MacOS', u'IDNSnitchPlugin')
        NSLog(u'Injecting %s into Safari [%d]' % (path, pid))
        objc.inject(pid, path.encode('utf-8'))
        self.statusText.setStringValue_(u'Injected into Safari [%d]' % (pid,))

if __name__ == '__main__':
    AppHelper.runEventLoop()
