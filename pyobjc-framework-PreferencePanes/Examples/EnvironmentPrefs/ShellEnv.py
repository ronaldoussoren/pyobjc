"""
EnvironmentPane - PreferencePane for changing the global user environment

This PreferencePane provides an easy to use UI for changeing
~/.MacOSX/environment.plist. This plist is loaded by the loginwindow application
when the user logs in and is used to initialize the "shell" environment.

Note that these variables are also available outside of the Terminal, but not
when the user logs in using SSH.

TODO:
- Undo
"""
import objc
from AppKit import *
from Foundation import *
from PreferencePanes import *
from PyObjCTools import NibClassBuilder, AppHelper
import os

# Uncomment this during development, you'll get exception tracebacks when
# the Python code fails.
#objc.setVerbose(1)

NibClassBuilder.extractClasses("EnvironmentPane")

# Location of the environment.plist
ENVPLIST="~/.MacOSX/environment.plist"

# Template for new keys
NEWTMPL=NSLocalizedString("New_Variable_%d", "")

class EnvironmentPane (NibClassBuilder.AutoBaseClass):
    """
    The 'model/controller' for the "Shell Environment" preference pane
    """

    #__slots__ = (
    #    'environ',  # The actual environment, as a NSMutableDictionary
    #    'keys',     # The list of keys, in the right order for the tableView
    #    'changed',  # True if we should save before exitting
    #)

    def initWithBundle_(self, bundle):
        # Our bundle has been loaded, initialize the instance variables.
        # We don't load the environment.plist yet, do that when we're
        # actually selected. That way we can easier pick up manual changes.

        self = super(EnvironmentPane, self).initWithBundle_(bundle)
        if self is None: return None

        self.keys = ()
        self.environ = None
        self.changed = False

        return self

    def mainViewDidLoad(self):
        self.deleteButton.setEnabled_(False)

    def didSelect(self):
        # We are the selected preference pane. Load the environment.plist.

        self.environ = NSMutableDictionary.dictionaryWithContentsOfFile_(
            os.path.expanduser(ENVPLIST))
        if self.environ is None:
            self.environ = NSMutableDictionary.dictionary()
        self.keys = list(self.environ.keys())
        self.keys.sort()
        self.changed = False
        self.mainTable.reloadData()

    def shouldUnselect(self):
        # The user wants to select another preference pane. If we have
        # unsaved changes ask if they should be saved right now.

        if self.changed:
            NSBeginAlertSheet(
                NSLocalizedString("Save changes?", ""),
                NSLocalizedString("Cancel", ""),
                NSLocalizedString("Don't Save", ""),
                NSLocalizedString("Save", ""),
                self.mainView().window(),
                self,
                None,
                "sheetDidDismiss:returnCode:contextInfo:",
                0,
                NSLocalizedString("There are unsaved changed, should these be saved?", ""))
            return NSUnselectLater
        return NSUnselectNow

    def sheetDidDismiss_returnCode_contextInfo_(self, sheet, code, info):
        # Sheet handler for saving unsaved changes.

        if code == NSAlertDefaultReturn: # 'Cancel'
            self.replyToShouldUnselect_(NSUnselectCancel)
            return

        elif code == NSAlertAlternateReturn: # 'Don't Save'
            pass

        elif code == NSAlertOtherReturn: # 'Save'
            r = self.saveEnvironment()
            if not r:
                self.runAlertSheet(
                    NSLocalizedString("Cannot save changes", ""),
                    NSLocalizedString("It was not possible to save your changes", ""))
                self.replyToShouldUnselect_(NSUnselectCancel)
                return

        self.keys = ()
        self.environ = None
        self.changed = False
        self.replyToShouldUnselect_(NSUnselectNow)

    sheetDidDismiss_returnCode_contextInfo_ = AppHelper.endSheetMethod(
        sheetDidDismiss_returnCode_contextInfo_)

    def saveEnvironment(self):
        """
        Save the data to environment.plist
        """
        fname = os.path.expanduser(ENVPLIST)
        dname = os.path.dirname(fname)
        if not os.path.isdir(dname):
            try:
                os.mkdir(dname)
            except os.error, msg:
                return False

        if not self.environ.writeToFile_atomically_(fname, True):
            return False

        return True

    def deleteVariable_(self, sender):
        """
        Delete the selected variable
        """
        r = self.mainTable.selectedRow()

        envname = self.keys[r]
        del self.environ[envname]
        self.keys.remove(envname)
        self.mainTable.reloadData()
        self.changed = True

    def newVariable_(self, sender):
        """
        Add a new variable
        """
        i = 0
        name = NEWTMPL%(i,)
        while self.environ.has_key(name):
            i += 1
            name = NEWTMPL%(i,)
        self.environ[name] = NSLocalizedString("New Value", "")
        self.keys = list(self.environ.keys())
        self.keys.sort()
        self.mainTable.reloadData()
        self.changed = True

    def numberOfRowsInTableView_(self, aView):
        """ Return the number of environment variables """
        return len(self.keys)

    def tableView_objectValueForTableColumn_row_(self, aView, aCol, rowIndex):
        """ Get the name of value of an environment variable """
        name = aCol.identifier()
        envname = self.keys[rowIndex]

        if name == "name":
            return envname
        elif name == "value":
            return self.environ[envname]

    def tableView_setObjectValue_forTableColumn_row_(self,
            aView, value, aCol,rowIndex):
        """ Change the name or value of an environment variable """
        if self.environ is None:
            aView.reloadData()
            return

        name = aCol.identifier()
        envname = self.keys[rowIndex]

        if name == "name":
            if value != envname:
                if self.environ.has_key(value):
                    self.runAlertSheet(
                        NSLocalizedString("Name exists", ""),
                        NSLocalizedString("The name %s is already used", "")%(
                            value,))
                    aView.reloadData()
                    return

                val = self.environ[envname]
                del self.environ[envname]
                self.environ[value] = val
                self.keys = list(self.environ.keys())
                self.keys.sort()
                aView.reloadData()
                self.changed = True

        elif name == "value":
            val = self.environ[envname]
            if val != value:
                self.environ[envname] = value
                self.changed = True

    def tableViewSelectionDidChange_(self, notification):
        """ The delete button should only be active if a row is selected """
        if self.mainTable.numberOfSelectedRows() == 0:
            self.deleteButton.setEnabled_(False)
        else:
            self.deleteButton.setEnabled_(True)

    def runAlertSheet(self, title, message):
        """ Run an alertsheet without callbacks """
        NSBeginAlertSheet(title,
            NSLocalizedString("OK", ""), None, None,
            self.mainView().window(),
            self,
            None,
            None,
            0,
            message)

objc.removeAutoreleasePool()
