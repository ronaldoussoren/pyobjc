import sys
import os.path
from AppKit.NibClassBuilder import AutoBaseClass,  extractClasses

extractClasses('MainMenu.nib')

sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

import objc
import AppKit

class PyModel (AutoBaseClass, AppKit.NSTableDataSource):
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

sys.exit(AppKit.NSApplicationMain(sys.argv))
