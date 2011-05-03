import objc; objc.setVerbose(1)
from AppKit import *
from Foundation import *
from PyObjCTools import AppHelper
from MyDocument import *
from LaunchServices import *
from PreferencesWindowController import *

PYTHON_EXTENSIONS = [u'py', 'pyw', u'pyc']

FILE_TYPE_BINDING_MESSAGE = u"""
%s is not the default application for all Python script types.  You should fix this with the Finder's "Get Info" command.

See "Changing the application that opens a file" in Mac Help for details.
""".strip()

class MyAppDelegate(NSObject):
    def init(self):
        self = super(MyAppDelegate, self).init()
        self.initial_action_done = False
        self.should_terminate = False
        return self

    @objc.IBAction
    def showPreferences_(self, sender):
        PreferencesWindowController.getPreferencesWindow()

    def applicationDidFinishLaunching_(self, aNotification):
        self.testFileTypeBinding()
        if not self.initial_action_done:
            self.initial_action_done = True
            self.showPreferences_(self)

    def shouldShowUI(self):
        if not self.initial_action_done:
            self.should_terminate = True
        self.initial_action_done = True
        if NSApp().currentEvent().modifierFlags() & NSAlternateKeyMask:
            return True
        return False

    def shouldTerminate(self):
        return self.should_terminate

    def applicationShouldOpenUntitledFile_(self, sender):
        return False

    def testFileTypeBinding(self):
        if NSUserDefaults.standardUserDefaults().boolForKey_(u'SkipFileBindingTest'):
            return
        bndl = NSBundle.mainBundle()
        myURL = NSURL.fileURLWithPath_(bndl.bundlePath())
        myName = bndl.infoDictionary()[u'CFBundleName']
        for ext in PYTHON_EXTENSIONS:
            err, outRef, outURL = LSGetApplicationForInfo(kLSUnknownType, kLSUnknownCreator, u'txt', kLSRolesViewer, None, None)
            if (err or myURL != outURL):
                res = NSRunAlertPanel(
                    u'File type binding',
                    FILE_TYPE_BINDING_MESSAGE % myName,
                    u'OK',
                    u"Don't show this warning again",
                    None)
                if res == 0:
                    NSUserDefaults.standardUserDefaults().setObject_forKey_(u'YES', u'SkipFileBindingTest')
                return

if __name__ == '__main__':
    AppHelper.runEventLoop()
