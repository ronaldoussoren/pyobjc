
from StringIO import StringIO

## Install corefoundation reactor
import twisted.internet.cfreactor
reactor = twisted.internet.cfreactor.install()

from twisted.internet import error

## New HTTP client in Twisted/sandbox/moshez
import newclient

## ObjC stuff
from Foundation import *
from PyObjCTools import NibClassBuilder, AppHelper
from objc import YES, NO, selector

## plistlib from macpython
import plistlib

import newpimp

# DEBUG
import sys
from twisted.python import log
log.startLogging(sys.stdout)

# the test-multidatabase
DATABASE = 'http://undefined.org/python/pimp/panther.plist'

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
    packages = ()
    _allPackages = ()

    def applicationDidFinishLaunching_(self, aNotification):
        self.databaseList.selectRowIndexes_byExtendingSelection_(
            NSIndexSet.indexSetWithIndex_(0), NO
        )
        self.openDatabase(DATABASE)
        reactor.run()

    def openDatabase(self, url):
        log.msg('Opening database: %s' % (url,))
        return newpimp.downloadPackmanDatabase(url.encode('utf8')
        ).addCallback(
            self.gotPlist
        ).addErrback(
            self.errorOpening
        )

    def gotPlist(self, plist):
        log.msg('received plist')
        packages = plist['Packages']
        #
        # XXX - Flavors and Version should be condensed into one row?
        #
        # default sort is
        #   Name, Version, Flavor
        #
        packages.sort(lambda a,b:(
            cmp(a['Name'].lower(), b['Name'].lower()) or
            cmp(a.get('Version'), b.get('Version')) or
            cmp(a.get('Flavor'), b.get('Flavor'))))
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
