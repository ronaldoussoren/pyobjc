from Foundation import NSObject
from AppKit import NSApplicationMain, NSTableDataSource
from objc import selector
import sys

class PyModel (NSObject, NSTableDataSource):
	__slots__  = ('rowcount')

	def awakeFromNib(self):
		self.rowcount = 10
		return self

	def init(self):
		self.rowcount = 10
		return self

	def numberOfRowsInTableView_(self, aTableView):
		print "numerOfRowsInTableView: called"
		return self.rowcount


	def tableView_objectValueForTableColumn_row_(self, 
			aTableView, aTableColumn, rowIndex):
		print "tableView:objectValueForTableColumn:row: called"
		return "{%s, %d}"%(aTableColumn.identifier(), rowIndex)



sys.exit(NSApplicationMain(sys.argv))
