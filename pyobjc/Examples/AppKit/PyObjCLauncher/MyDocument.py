from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder
import os
from FileSettings import *
from doscript import doscript

class MyDocument(NibClassBuilder.AutoBaseClass):
    def init(self):
        self = super(MyDocument, self).init()
        if self is not None:
            self.script = u'<no script>.py'
            self.filetype = u'Python Script'
            self.settings = None
        return self

    def windowNibName(self):
        return u'MyDocument'

    def close(self):
        super(MyDocument, self).close()
        if NSApp().delegate().shouldTerminate():
            NSApp().terminate_(self)

    def load_defaults(self):
        self.settings = FileSettings.newSettingsForFileType_(self.filetype)

    def update_display(self):
        dct = self.settings.fileSettingsAsDict()
        self.interpreter.setStringValue_(dct['interpreter'])
        self.honourhashbang.setState_(dct['honourhashbang'])
        self.debug.setState_(dct['verbose'])
        self.inspect.setState_(dct['inspect'])
        self.optimize.setState_(dct['optimize'])
        self.nosite.setState_(dct['nosite'])
        self.tabs.setState_(dct['tabs'])
        self.others.setStringValue_(dct['others'])
        self.scriptargs.setStringValue_(dct['scriptargs'])
        self.with_terminal.setState_(dct['with_terminal'])
        self.commandline.setStringValue_(self.settings.commandLineForScript_(self.script))

    def update_settings(self):
        self.settings.updateFromSource_(self)

    def run(self):
        cmdline = self.settings.commandLineForScript_(self.script)
        dct = self.settings.fileSettingsAsDict()
        if dct['with_terminal']:
            res = doscript(cmdline)
        else:
            res = os.system(cmdline)
        if res:
            NSLog(u'Exit status: %d' % (res,))
            return False
        return True

    def windowControllerDidLoadNib_(self, aController):
        super(MyDocument, self).windowControllerDidLoadNib_(aController)
        self.load_defaults()
        self.update_display()

    def dataRepresentationOfType_(self, aType):
        return None

    def readFromFile_ofType_(self, filename, typ):
        show_ui = NSApp().delegate().shouldShowUI()
        self.script = filename
        self.filetype = typ
        self.settings = FileSettings.newSettingsForFileType_(typ)
        if show_ui:
            self.update_display()
            return True
        else:
            self.run()
            self.close()
            return False

    def doRun_(self, sender):
        self.update_settings()
        self.update_display()
        if self.run():
            self.close()

    def doCancel_(self, sender):
        self.close()

    def doReset_(self, sender):
        self.settings.reset()
        self.update_display()

    def doApply_(self, sender):
        self.update_settings()
        self.update_display()

    def controlTextDidChange_(self, aNotification):
        self.update_settings()
        self.update_display()

    def fileSettingsAsDict(self):
        return dict(
            interpreter=self.interpreter.stringValue(),
            honourhashbang=self.honourhashbang.state(),
            debug=self.debug.state(),
            verbose=self.verbose.state(),
            inspect=self.inspect.state(),
            optimize=self.optimize.state(),
            nosite=self.nosite.state(),
            tabs=self.tabs.state(),
            others=self.others.stringValue(),
            with_terminal=self.with_terminal.state(),
            scriptargs=self.scriptargs.stringValue(),
        )
