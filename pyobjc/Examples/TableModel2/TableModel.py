import sys
import os.path
import AppKit
from AppKit import NibClassBuilder
from AppKit.NibClassBuilder import AutoBaseClass

sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

import objc
import AppKit

NibClassBuilder.extractClasses("MainMenu")
class PyModel (AutoBaseClass, AppKit.NSTableDataSource, AppKit.NSTableViewDelegate):
    __slots__  = ('rowcount')

    def init(self):
        print "PyModel instance initialized"
        self.rowcount = 10
        return self

    def numberOfRowsInTableView_(self, aTableView):
        print "numerOfRowsInTableView: called"
        return self.rowcount


    def tableView_objectValueForTableColumn_row_(
        self, aTableView, aTableColumn, rowIndex):

        print "tableView:objectValueForTableColumn:row: called"
        return "{%s, %d}"%(aTableColumn.identifier(), rowIndex)
    
    def tableView_shouldSelectRow_(self, aTableView, aRow):
        print "tableView:shouldSelectRow:", aRow
        return 1

sys.exit(AppKit.NSApplicationMain(sys.argv))
