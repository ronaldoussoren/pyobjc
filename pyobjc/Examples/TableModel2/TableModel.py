import sys
import os.path

sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

import objc
import Foundation
import AppKit

class PyModel (Foundation.NSObject):
	__slots__  = ('rowcount')

	def init(self):
		print "init"
		self.rowcount = 10
		return self

	def numberOfRowsInTableView_(self, aTableView):
		print "numerOfRowsInTableView: called"
		return self.rowcount

	def tableView_objectValueForTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
		print "tableView:objectValueForTableColumn:row: called"
		return "{%s, %d}"%(aTableColumn.identifier(), rowIndex)

	tableView_objectValueForTableColumn_row_ = objc.selector(tableView_objectValueForTableColumn_row_, signature='@@:@@i')
	numberOfRowsInTableView_ = objc.selector(numberOfRowsInTableView_, signature="i@:@")

sys.exit( AppKit.NSApplicationMain(sys.argv) )
