from Foundation import NSObject
from AppKit import NSApplicationMain
from objc import selector
import sys

class PyModel (NSObject):
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

	numberOfRowsInTableView_ = selector(numberOfRowsInTableView_,
		signature="i@:@")


	def tableView_objectValueForTableColumn_row_(self, 
			aTableView, aTableColumn, rowIndex):
		print "tableView:objectValueForTableColumn:row: called"
		return "{%s, %d}"%(aTableColumn.identifier(), rowIndex)

	tableView_objectValueForTableColumn_row_ = selector(
		tableView_objectValueForTableColumn_row_,
		signature='@@:@@i')


sys.exit(NSApplicationMain(sys.argv))
