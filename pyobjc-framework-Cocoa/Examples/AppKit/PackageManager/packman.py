"""
Cocoa GUI for the Package Manager

This is a first generation of the Cocoa GUI, it inherits some of the nasty
features of the current Carbon version:

1. GUI blocks during some operations, such as downloading or installing

2. Checking on GUI packages may crash the application

The first item can only be solved by rewriting parts of the pimp module, the
second part will be solved by running at least some pimp related code in a
seperate process.

TODO:
- Make sure 'File -> Open...' actually works

XXX:
- save preferences in the favorites db (for databases that are in in there)?
"""

from Cocoa import *
import objc
import threading

from PyObjCTools import AppHelper

import sys
import pimp
import webbrowser

# File type for packman databases
DB_FILE_TYPE="Python Package Database"

# Extract class information from the NIB files
# - MainMenu: Global application stuff
# - OpenPanel: The 'Open URL...' window
# - PackageDatabase: Document window

def setString(field, value):
    """
    Set an NSTextField to the specified value. Clears the field if 'value'
    is None.
    """
    if value is None:
        field.setStringValue_("")
    else:
        field.setStringValue_(value)


##
# We break the abstraction of some of the objects in the pimp module. That
# is necessary because we cannot get at the required information using the
# public interfaces :-(
#
def DB_DESCRIPTION(pimpDB):
    return pimpDB._description

def DB_MAINTAINER(pimpDB):
    return pimpDB._maintainer

def DB_URL(pimpDB):
    return pimpDB._urllist[0]

def PKG_HIDDEN(package):
    """ Return True iff the package is a hidden package """
    return (package._dict.get('Download-URL', None) is None)




class PackageDatabase (NSDocument):
    """
    The document class for a package database
    """
    databaseMaintainer = objc.IBOutlet()
    databaseName = objc.IBOutlet()
    installButton = objc.IBOutlet()
    installDependencies = objc.IBOutlet()
    installationLocation = objc.IBOutlet()
    installationLog = objc.IBOutlet()
    installationPanel = objc.IBOutlet()
    installationProgress = objc.IBOutlet()
    installationTitle = objc.IBOutlet()
    itemDescription = objc.IBOutlet()
    itemHome = objc.IBOutlet()
    itemInstalled = objc.IBOutlet()
    itemStatus = objc.IBOutlet()
    overwrite = objc.IBOutlet()
    packageTable = objc.IBOutlet()
    prerequisitesTable = objc.IBOutlet()
    progressOK = objc.IBOutlet()
    showHidden = objc.IBOutlet()
    verbose = objc.IBOutlet()


    def init(self):
        """
        Initialize the document without a database
        """

        self = super(PackageDatabase, self).init()
        if self is None: return None
        self.pimp =  None
        self._packages = []
        return self


    def initWithContentsOfFile_ofType_(self, path, type):
        """
        Open a local database.
        """
        self = self.init()
        if self is None: return self

        url = NSURL.fileURLWithPath_(path)

        self.openDB(url.absoluteString())
        return self

    def __del__(self):
        """ Clean up after ourselves """
        if hasattr(self, 'timer'):
            self.timer.invalidate()
            del self.timer

    def close(self):
        if hasattr(self, 'timer'):
            self.timer.invalidate()
            del self.timer
        super(PackageDatabase, self).close()

    def setDB(self, pimpURL, pimpDB):
        self.pimp = pimpDB
        self._packages = pimpDB.list()
        self._prerequisites = []
        if self.databaseName is not None:
            self.databaseName.setStringValue_(DB_DESCRIPTION(self.pimp))
            self.databaseMaintainer.setStringValue_(DB_MAINTAINER(self.pimp))

        if self.packageTable is not None:
            self.packageTable.reloadData()
            self.tableViewSelectionDidChange_(None)

        self.setFileName_(pimpURL)
        self.pimpURL = pimpURL

        if hasattr(self, 'timer'):
            self.timer.invalidate()

        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                10.0,
                self,
                self.checkUpdates_,
                None,
                True)


    def openDB(self, dbUrl=None):
        """
        Open a database at the specified URL
        """
        prefs = pimp.PimpPreferences()
        if dbUrl is not None:
            prefs.pimpDatabase = dbUrl
        else:
            prefs.pimpDatabase = pimp.DEFAULT_PIMPDATABASE

        db = pimp.PimpDatabase(prefs)
        db.appendURL(prefs.pimpDatabase)
        self.setDB(dbUrl, db)

    def checkUpdates_(self, sender):
        """
        Refresh the package information, the user may have installed or
        removed a package. This method is called once in a while using a timer.
        """
        if self.packageTable is None: return

        self.sortPackages()
        self.packageTable.reloadData()

    def windowNibName(self):
        """ Return the name of the document NIB """
        return 'PackageDatabase'

    def displayName(self):
        """ Return the document name for inside the window title """
        if self.pimp is None:
            return "Untitled"

        return DB_URL(self.pimp)

    def awakeFromNib(self):
        """
        Initialize the GUI now that the NIB has been loaded.
        """
        if self.pimp is not None:
            self.databaseName.setStringValue_(DB_DESCRIPTION(self.pimp))
            self.databaseMaintainer.setStringValue_(DB_MAINTAINER(self.pimp))

        else:
            self.databaseName.setStringValue_("")
            self.databaseMaintainer.setStringValue_("")


        self.setBoolFromDefaults(self.verbose, 'verbose')
        self.setBoolFromDefaults(
                self.installDependencies, 'installDependencies')
        self.setBoolFromDefaults(self.showHidden, 'showHidden')
        self.setBoolFromDefaults(self.overwrite, 'forceInstallation')

        b = NSUserDefaults.standardUserDefaults(
                ).boolForKey_('installSystemWide')
        if b:
            self.installationLocation.setState_atRow_column_(NSOnState, 0, 0)
        else:
            self.installationLocation.setState_atRow_column_(NSOnState, 1, 0)

        self.sortPackages()

    def setBoolFromDefaults(self, field, name):
        defaults = NSUserDefaults.standardUserDefaults()
        b = defaults.boolForKey_(name)
        if b:
            field.setState_(NSOnState)
        else:
            field.setState_(NSOffState)

    def saveBoolToDefaults(self, field, name):
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setBool_forKey_(field.state() == NSOnState, name)
        defaults.synchronize()

    @objc.IBAction
    def savePreferences_(self, sender):
        self.saveBoolToDefaults(self.verbose, 'verbose')
        self.saveBoolToDefaults(self.installDependencies, 'installDependencies')
        self.saveBoolToDefaults(self.showHidden, 'showHidden')
        self.saveBoolToDefaults(self.overwrite, 'forceInstallation')
        self.saveBoolToDefaults(
                self.installationLocation.cellAtRow_column_(0, 0),
                'installSystemWide')

    def packages(self):
        return self._packages

    def selectedPackage(self):
        row = self.packageTable.selectedRow()
        if row == -1: return None

        return self._packages[row]


    def tableViewSelectionDidChange_(self, obj):
        """
        Update the detail view
        """

        package = self.selectedPackage()

        if package is None:
            # No selected package, clear the detail view
            setString(self.itemHome, None)
            setString(self.itemStatus, None)
            setString(self.itemInstalled, None)
            self.itemDescription.setString_("")
            self.installButton.setEnabled_(False)
            self._prerequisites = []
            self.prerequisitesTable.reloadData()

        else:
            # Update the detail view

            setString(self.itemHome, package.homepage())

            # XXX: Could we use ReST for the the description?
            # Recognizing and 'activating' URL's would be fairly easy.
            self.itemDescription.setString_(
                    package.description()
            )

            status, msg = package.installed()
            setString(self.itemInstalled, status)
            setString(self.itemStatus, msg)
            self.installButton.setEnabled_(True)
            self._prerequisites = package.prerequisites()

            # XXX: Add the closure of all dependencies

            self.prerequisitesTable.reloadData()

    @objc.IBAction
    def addToFavorites_(self, sender):
        appdel = NSApplication.sharedApplication().delegate()
        appdel.addFavorite(self.pimp._description, self.pimp._urllist[0])

    #
    # NSTableDataSource implementation, for the package list
    #

    def numberOfRowsInTableView_(self, view):

        if not hasattr(self, 'pimp') or self.pimp is None:
            return 0

        if view is self.packageTable:
            return len(self._packages)
        else:
            return len(self._prerequisites)


    def tableView_objectValueForTableColumn_row_(self, view, col, row):

        colname = col.identifier()

        if view is self.packageTable:
            package = self._packages[row]
            shortdescription = None
        else:
            package, shortdescription = self._prerequisites[row]

        if colname == 'installed':
            # XXX: Nicer formatting
            return getattr(package, colname)()[0]

        return getattr(package, colname)()

    def tableView_sortDescriptorsDidChange_(self, view, oldDescriptors):
        if view is self.packageTable:
            self.sortPackages()

    def sortPackages(self):
        """
        Sort the package list in the order wished for by the user.
        """
        if self.pimp is None:
            return

        if self.packageTable is None:
            return

        sortInfo = [
            (item.key(), item.ascending(), item.selector())
                for item in self.packageTable.sortDescriptors()
        ]

        if self.showHidden.state() == NSOnState:
            self._packages = self.pimp.list()[:]
        else:
            self._packages = [ pkg
                for pkg in self.pimp.list() if not PKG_HIDDEN(pkg) ]

        if not sortInfo:
            self.packageTable.reloadData()
            self.tableViewSelectionDidChange_(None)
            return

        def cmpBySortInfo(l, r):
            for key, ascending, meth in sortInfo:
                if key == 'installed':
                    l_val = getattr(l, key)()[0]
                    r_val = getattr(r, key)()[0]
                else:
                    l_val = getattr(l, key)()
                    r_val = getattr(r, key)()
                if meth == 'compare:':
                    res = cmp(l_val, r_val)
                else:
                    if isinstance(l_val, objc.pyobjc_unicode):
                        l_val = l_val.nsstring()
                    elif isinstance(l_val, (unicode, str)):
                        l_val = NSString.stringWithString_(l_val).nsstring()
                    res = getattr(l_val, meth)(r_val)

                if not ascending:
                    res = -res
                if res != 0:
                    return res

            return 0

        self._packages.sort(cmpBySortInfo)
        self.packageTable.reloadData()

    @objc.IBAction
    def filterPackages_(self, sender):
        """
        GUI action that is triggered when one of the view options
        changes
        """
        self.sortPackages()

    @objc.IBAction
    def visitHome_(self, sender):
        """
        Open the homepage of the currently selected package in the
        default webbrowser.
        """
        package = self.selectedPackage()
        if package is None:
            return

        home = package.homepage()
        if home is None:
            return

        try:
            webbrowser.open(home)
        except Exception, msg:
            NSBeginAlertSheet(
                    'Opening homepage failed',
                    'OK', None, None, self.windowForSheet(), None, None, None,
                    0, 'Could not open homepage: %s'%(msg,))


    @objc.IBAction
    def installPackage_(self, sender):
        """
        Install the currently selected package
        """
        package = self.selectedPackage()
        if package is None: return

        force = self.overwrite.state() == NSOnState
        recursive = self.installDependencies.state() == NSOnState

        pimpInstaller = pimp.PimpInstaller(self.pimp)
        lst, messages = pimpInstaller.prepareInstall(package, force, recursive)

        if messages:
            NSBeginAlertSheet(
                    'Cannot install packages',
                    'OK', None, None,
                    self.windowForSheet(), None, None, None, 0,
                    '\n'.join(messages))
            return

        app = NSApplication.sharedApplication()
        self.installationTitle.setStringValue_(
                'Installing: %s ...'%(package.shortdescription(),))
        self.installationProgress.setHidden_(False)
        self.installationProgress.startAnimation_(self)
        self.progressOK.setEnabled_(False)
        ts = self.installationLog.textStorage()
        ts.deleteCharactersInRange_((0, ts.length()))
        app.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(
                self.installationPanel,
                self.windowForSheet(),
                None, None, 0)

        # I'm not sure if this accidental or not, but prepareInstall() returns
        # a list of package in the order that they should be installed in,
        # and install() installs them in the reverse order :-(
        # XXX: This seems to be a bug in pimp.
        self.runner = InstallerThread(
                            self,
                            pimpInstaller,
                            lst[::-1],
                            self.verbose.state() == NSOnState,
                            self.installationLog.textStorage()
                        )

        self.runner.start()

    @objc.IBAction
    def closeProgress_(self, sender):
        """
        Close the installation progress sheet
        """
        self.installationPanel.close()
        NSApplication.sharedApplication().endSheet_(self.installationPanel)

    @objc.IBAction
    def installationDone_(self, sender):
        """
        The installer thread is ready, close the sheet.
        """
        self.progressOK.setEnabled_(True)
        self.installationProgress.setHidden_(False)
        self.installationProgress.stopAnimation_(self)

        messages = self.runner.result
        if messages:
            ts = self.installationLog.textStorage()
            ts.appendAttributedString_(
                NSAttributedString.alloc().initWithString_attributes_(
                    '\n\nCannot install packages\n\n',
                    {
                        NSFontAttributeName: NSFont.boldSystemFontOfSize_(12),
                    }
                ))

            ts.appendAttributedString_(
                NSAttributedString.alloc().initWithString_(
                    '\n'.join(messages) + '\n'))

        self.packageTable.reloadData()
        self.tableViewSelectionDidChange_(None)


class DownloadThread (threading.Thread):
    """
    Thread for downloading a PackageManager database.

    This is used by the application delegate to open databases.
    """
    daemon_thread = True

    def __init__(self, master, document, url):
        """
        Initialize the thread.

        master   - NSObject implementing dbReceived: and dbProblem:
        document - An PackageDatabase
        url      - The PackMan URL
        """
        threading.Thread.__init__(self)
        self.master = master
        self.document = document
        self.url = url

    def run(self):
        """
        Run the thread. This creates a new pimp.PimpDatabase, tells it to
        download our database and then forwards the database to the
        master. The last step is done on the main thread because of Cocoa
        threading issues.
        """
        pool = NSAutoreleasePool.alloc().init()

        try:
            prefs = pimp.PimpPreferences()
            if self.url is not None:
                prefs.pimpDatabase = self.url
            else:
                prefs.pimpDatabase = pimp.DEFAULT_PIMPDATABASE

            db = pimp.PimpDatabase(prefs)
            db.appendURL(prefs.pimpDatabase)

            self.master.performSelectorOnMainThread_withObject_waitUntilDone_(
                'dbReceived:', (self.document, self.url, db), False)

        except:
            self.master.performSelectorOnMainThread_withObject_waitUntilDone_(
                'dbProblem:', (self.document, self.url, sys.exc_info()), False)

        del pool




class InstallerThread (threading.Thread):
    """
    A thread for installing packages.

    Like downloading a database, installing (and downloading!) packages is
    a time-consuming task that is better done on a seperate thread.
    """
    daemon_thread = True

    def __init__(self, document, installer, packages, verbose, textStorage):
        threading.Thread.__init__(self)
        self.document = document
        self.installer = installer
        self.packages = packages
        self.verbose = verbose
        self.textStorage = textStorage
        self.result = None

    def write(self, data):
        self.textStorage.performSelectorOnMainThread_withObject_waitUntilDone_(
                'appendAttributedString:',
                NSAttributedString.alloc().initWithString_(data),
                False)

    def run(self):
        pool = NSAutoreleasePool.alloc().init()

        if self.verbose:
            result = self.installer.install(self.packages, self)
        else:
            result = self.installer.install(self.packages, None)

        self.write('\nDone.\n')

        self.document.performSelectorOnMainThread_withObject_waitUntilDone_(
                'installationDone:', None, False)

        del pool

class URLOpener (NSObject):
    """
    Model/controller for the 'File/Open URL...' panel
    """
    okButton = objc.IBOutlet
    urlField = objc.IBOutlet()

    def __del__(self):
        # XXX: I'm doing something wrong, this function is never called!
        print "del URLOpener %#x"%(id(self),)


    def awakeFromNib(self):
        self.urlField.window().makeKeyAndOrderFront_(None)

    @objc.IBAction
    def doOpenURL_(self, sender):
        url = self.urlField.stringValue()
        if not url:
            return

        # Ask the application delegate to open the selected database
        NSApplication.sharedApplication().delegate().openDatabase(url)

    @objc.IBAction
    def controlTextDidChange_(self, sender):
        """
        The value of the URL input field changed, enable the OK button
        if there is input, disable it otherwise.
        """
        if self.urlField.stringValue() != "":
            self.okButton.setEnabled_(True)
        else:
            self.okButton.setEnabled_(False)



class PackageManager (NSObject):
    """
    Application controller: application-level callbacks and actions
    """
    favoritesPanel = objc.IBOutlet()
    favoritesTable = objc.IBOutlet()
    favoritesTitle = objc.IBOutlet()
    favoritesURL   = objc.IBOutlet()

    #
    # Standard actions
    #

    def awakeFromNib(self):
        """
        We've been restored from the NIB
        """
        self.loadFavorites()

    #
    # Working with favorites
    #
    # The favorites are stored in the user defaults for the application.

    def loadFavorites(self):
        """
        Load our favorite database
        """
        self.favorites = NSUserDefaults.standardUserDefaults().arrayForKey_(
                    'favorites')
        if self.favorites is None:
            self.favorites = []
        else:
            self.favorites = list(self.favorites)

    def saveFavorites(self):
        """
        Save the favorites database, must be called whenever self.favorites
        is changed.
        """
        defaults = NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_(
                self.favorites,
                'favorites')
        defaults.synchronize()

    def addFavorite(self, title, url):
        """
        Add a new favorite, and save the database
        """
        self.favorites.append({'title':title, 'URL':url})
        self.favoritesTable.reloadData()
        self.saveFavorites()

    def menuNeedsUpdate_(self, menu):
        """
        We're the delegate for the Favorites menu

        Update the menu: it should list the entries in the favorites database.
        """
        menuLen = menu.numberOfItems()

        # Remove old items
        for i in range(menuLen-1, 2, -1):
            menu.removeItemAtIndex_(i)

        # Insert new ones
        for item in self.favorites:
            title = item['title']
            url = item['URL']

            mi = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
                    title, self.openFavorite_, "")
            mi.setTarget_(self)
            mi.setRepresentedObject_(item)
            menu.addItem_(mi)


    def tableViewSelectionDidChange_(self, obj):
        """
        We're the delegate (and datasource) for the favorites list in the
        edit pane for the favorites.

        Update the input fields to show the current item.
        """

        row = self.favoritesTable.selectedRow()
        if row == -1:
            self.favoritesTitle.setStringValue_('')
            self.favoritesURL.setStringValue_('')
            self.favoritesTitle.setEnabled_(False)
            self.favoritesURL.setEnabled_(False)
        else:
            self.favoritesTitle.setStringValue_(self.favorites[row]['title'])
            self.favoritesURL.setStringValue_(self.favorites[row]['URL'])
            self.favoritesTitle.setEnabled_(True)
            self.favoritesURL.setEnabled_(True)


    def numberOfRowsInTableView_(self, view):
        """
        We're the datasource for the favorites list in the Favorites panel
        """
        if not hasattr(self, 'favorites'):
            return 0

        return len(self.favorites)

    def tableView_objectValueForTableColumn_row_(self, view, col, row):
        """
        We're the datasource for the favorites list in the Favorites panel
        """
        return self.favorites[row]['title']

    @objc.IBAction
    def changeFavoritesTitle_(self, sender):
        """
        Update the title of the currently selected favorite item
        """
        row = self.favoritesTable.selectedRow()
        if row == -1:
            return

        self.favorites[row]['title'] = self.favoritesTitle.stringValue()
        self.saveFavorites()

        self.favoritesTable.reloadData()


    @objc.IBAction
    def changeFavoritesUrl_(self, sender):
        """
        Update the URL of the currently selected favorite item
        """
        row = self.favoritesTable.selectedRow()
        if row == -1:
            return

        self.favorites[row]['URL'] = self.favoritesURL.stringValue()
        self.saveFavorites()

        self.favoritesTable.reloadData()

    @objc.IBAction
    def openFavorite_(self, sender):
        """
        Open a favorite database (action for entries in the Favorites menu)
        """
        self.openDatabase(sender.representedObject()['URL'])


    #
    # Global actions/callbacks
    #

    def openDatabase(self, url):
        """
        Create a new NSDocument for the database at the specified URL.
        """
        doc = NSDocumentController.sharedDocumentController(
                ).openUntitledDocumentOfType_display_(DB_FILE_TYPE, False)
        try:
            downloader = DownloadThread(self, doc, url)
            downloader.start()
        except:
            doc.close()
            raise

    def dbReceived_(self, (doc, url, db)):
        doc.setDB(url, db)
        doc.showWindows()

    def dbProblem_(self, (doc, url, exc_info)):
        NSRunAlertPanel(
                "Cannot open database",
                "Opening database at %s failed: %s"%(url, exc_info[1]),
                "OK", None, None)
        doc.close()



    @objc.IBAction
    def openURL_(self, sender):
        """
        The user wants to open a package URL, show the user-interface.
        """
        res = NSBundle.loadNibNamed_owner_('OpenPanel', self)

    @objc.IBAction
    def openStandardDatabase_(self, sender):
        """
        Open the standard database.
        """
        self.openDatabase(pimp.DEFAULT_PIMPDATABASE)

    def applicationShouldOpenUntitledFile_(self, app):
        """
        The default window is not an untitled window, but the default
        database
        """
        return False

    def applicationDidFinishLaunching_(self, app):
        """
        The application finished launching, show the default database.
        """
        # XXX: We shouldn't open the standard database if the user explicitly
        # opened another one!
        self.openStandardDatabase_(None)

#
# Set some sensible defaults
#
NSUserDefaults.standardUserDefaults().registerDefaults_(
        {
          'verbose': True,
          'installDependencies': True,
          'showHidden': False,
          'forceInstallation': False,
          'installSystemWide': True,
        })

#
# A nasty hack. For some reason sys.prefix is /usr/bin/../../System/..., while
# it is /System/... in Jack's PackageManager.app.  At least one package
# manager database relies on sys.prefix being /System/... (Bob's additional
# packages).
#
import os
sys.prefix = os.path.abspath(sys.prefix)

AppHelper.runEventLoop()
