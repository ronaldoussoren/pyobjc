
from StringIO import StringIO

## Install corefoundation reactor
import twisted.internet.cfreactor
reactor = twisted.internet.cfreactor.install()

## New HTTP client in Twisted/sandbox/moshez
import newclient

## ObjC stuff
from Foundation import *
from PyObjCTools import NibClassBuilder, AppHelper
from objc import YES, NO, selector

## plistlib from macpython
import plistlib


NibClassBuilder.extractClasses("MainMenu")


class DatabasesController(NibClassBuilder.AutoBaseClass):
    _databases = [
        {'description': "Standard", 'url': ''}
    ]

    def addDb_(self, sender):
        if len(self._databases) is 1:
            self._databases = self._databases[:]
        url = self.newDatabaseURL.stringValue()
        try:
            self.packageController.openDatabase(str(url))
        except ValueError, e:
            print "bad url", `url`, e
            return
        self._databases.append({'description': '', 'url': url})
        self.databaseTable.reloadData()
        self.databaseTable.selectRowIndexes_byExtendingSelection_(
            NSIndexSet.indexSetWithIndex_(len(self._databases)-1), NO
        )

    def numberOfRowsInTableView_(self, view):
        return len(self._databases)

    def tableView_objectValueForTableColumn_row_(self, view, column, row):
        row = self._databases[row]
        return row['description'] or row['url']

    def tableViewSelectionDidChange_(self, aNotification):
        pass


class PackageController(NibClassBuilder.AutoBaseClass):
    packages = []
    _allPackages = []

    def applicationDidFinishLaunching_(self, aNotification):
        self.databaseList.selectRowIndexes_byExtendingSelection_(
            NSIndexSet.indexSetWithIndex_(0), NO
        )
        self.openDatabase('http://undefined.org/python/pimp/darwin-7.0.0-Power_Macintosh.plist')
        reactor.run()

    def openDatabase(self, url):
        o = newclient.opener()
        d = o.open(
            newclient.Request(str(url))
        ).addCallback(
            newclient.read
        ).addCallback(
            self.gotPlist
        ).addErrback(
            self.errorOpening
        )

    def gotPlist(self, pliststring):
        fl = StringIO(pliststring)
        plist = plistlib.Plist.fromFile(fl)
        packages = plist['Packages']
        packages.sort(lambda x, y: cmp(x['Name'].lower(), y['Name'].lower()))
        self._allPackagesIncludingHidden = packages
        self._allPackages = self.packages = [x for x in packages if x.get('Version', None)]
        self.table.reloadData()

    def errorOpening(self, failure):
        print "error opening url", failure

    def install_(self, sender):
        print "SELECTED", self.packages[self.table.selectedRow()]['Name']

    def numberOfRowsInTableView_(self, view):
        return len(self.packages)

    def tableView_objectValueForTableColumn_row_(self, view, column, row):
        columnName = column.headerCell().stringValue()
        return getattr(self, 'column_%s' % columnName, lambda row: '')(row)

    def column_Installed(self, row):
        return "No"

    def column_Package(self, row):
        return self.packages[row]['Name']

    def column_Version(self, row):
        return self.packages[row].get('Version', 'No Version')

    def tableViewSelectionDidChange_(self, aNotification):
        row = self.table.selectedRow()
        self.descriptionField.setStringValue_(
            self.packages[row]['Description'].strip()
        )

    def filter_(self, sender):
        search = sender.stringValue()
        self.packages = [
            package for package in self._allPackages if search.lower() in package['Name'].lower()
        ]
        self.table.reloadData()


if __name__ == "__main__":
    AppHelper.runEventLoop()
