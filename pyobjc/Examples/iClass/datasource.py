from Foundation import NSObject, NSBundle
from AppKit import NSOutlineViewDataSource, NSTableDataSource, NibClassBuilder
from AppKit.NibClassBuilder import AutoBaseClass
from objc import selector, getClassList, objc_object, IBOutlet

WRAPPED={}
class Wrapper (NSObject):
	"""
	NSOutlineView doesn't retain values, which means we cannot use normal
	python values as values in an outline view.
	"""
	def init_(self, value):
		self.value = value
		return self

	def __str__(self):
		return '<Wrapper for %s>'%self.value

	def description(self):
		return str(self)

methodIdentifier = {
	'objc_method':0,
	'python_method':1,
	'signature':2
}

def classPath(cls):
	if cls == objc_object:
		return ''
	elif cls.__bases__[0] == objc_object:
		return cls.__name__
	else:
		return '%s : %s'%(classPath(cls.__bases__[0]), cls.__name__)

SYSFRAMEWORKS_DIR='/System/Library/Frameworks/'
def classBundle(cls):
	framework = NSBundle.bundleForClass_(cls).bundlePath()
	if framework.startswith(SYSFRAMEWORKS_DIR):
		framework = framework[len(SYSFRAMEWORKS_DIR):]
		if framework.endswith('.framework'):
			framework = framework[:-len('.framework')]
	return framework

class ClassesDataSource (AutoBaseClass, NSOutlineViewDataSource, NSTableDataSource):
	__slots__ = ('_classList', '_classTree', '_methodInfo')

	def clearClassInfo(self):
		print "clearClassInfo"
		self._methodInfo = []
		self.methodTable.reloadData()
		self.window.setTitle_('iClass')


	def setClassInfo(self, cls):
		print "setClassInfo for",cls
		self.window.setTitle_('iClass: %s'%cls.__name__)
		self.classLabel.setStringValue_(classPath(cls))
		print (classPath(cls))
		self.frameworkLabel.setStringValue_(classBundle(cls))
		self._methodInfo = []
		for nm in dir(cls):
			meth = getattr(cls, nm)
			if not isinstance(meth, selector):
				continue
			self._methodInfo.append(
				(meth.selector, nm, meth.signature))
		self._methodInfo.sort()
		self.methodTable.reloadData()

	def selectClass_(self, event):
		print "selectClass:"
		rowNr = self.classTable.selectedRow()
		if rowNr == -1:
			self.clearClassInfo()
		else:
			item = self.classTable.itemAtRow_(rowNr)
			item = item.value
			self.setClassInfo(item)

	def showClass(self, cls):
		print "showClass:", cls
		# First expand the tree (to make item visible)
		super = cls.__bases__[0]
		if  super == objc_object:
			return

		self.showClass(super)
		item = WRAPPED[super]
		rowNr = self.classTable.rowForItem_(item)
		self.classTable.expandItem_(item)


	def selectClass(self, cls):
		print "selectClass"
		self.showClass(cls)

		item = WRAPPED[cls]
		rowNr = self.classTable.rowForItem_(item)

		self.classTable.scrollRowToVisible_(rowNr)
		self.classTable.selectRow_byExtendingSelection_(rowNr, False)


	def searchClass_(self, event):
		print "searchClass:"
		val = self.searchBox.stringValue()
		if not val:
			return
		print "Searching", val

		found = None
		for cls in self._classTree.keys():
			if not cls: continue
			if cls.__name__ == val:
				self.setClassInfo(cls)
				self.selectClass(cls)
				return
			elif cls.__name__.startswith(val):
				if not found:
					found = cls
				elif len(cls.__name__) > len(found.__name__):
					found = cls

		self.setClassInfo(found)
		self.selectClass(found)


	def refreshClasses(self):
		print "refreshClasses"
		self._classList = getClassList()
		self._classTree = {}
		self._methodInfo = []
		
		for cls in self._classList:
			super = cls.__bases__[0]
			if super == objc_object:
				super = None
			else:
				super = super
			if not self._classTree.has_key(cls):
				self._classTree[cls] = []

			if self._classTree.has_key(super):
				self._classTree[super].append(cls)
			else:
				self._classTree[super] = [ cls ]

		for lst in self._classTree.values():
			lst.sort()

		#print self._classTree

	def init(self):
		print "Init", self
		self._classInfo = getClassList()
		self.refreshClasses()
		return self

	def awakeFromNib(self):
		print "Awaking", self
		self._classInfo = getClassList()
		self.refreshClasses()
	

	def outlineView_child_ofItem_(self, outlineview, index, item):
		print "childOfItem:", index, item
		if not (item is None):
			item = item.value
		v = self._classTree[item][index]
		#print 'child is', v
		if not WRAPPED.has_key(v):
			print "Make Wrapper for", v
			WRAPPED[v] = Wrapper.alloc().init_(v)
		return WRAPPED[v]

	def outlineView_isItemExpandable_(self, outlineview, item):
		print "isItemExpandable:", item
		if not (item is None):
			item = item.value
		return len(self._classTree[item]) != 0


	def outlineView_numberOfChildrenOfItem_(self, outlineview, item):
		print "numChildren:", item
		if not (item is None):
			item = item.value
		return len(self._classTree[item])

	def outlineView_objectValueForTableColumn_byItem_(self, outlineview, column, item):
		print "objectValue:", item
		if item is None:
			return '<None>'
		else:
			#print "value:", item.value
			v = item.value
			return v.__name__

	
	def numberOfRowsInTableView_(self, aTableView):
		print "numberOfRows", aTableView
		return len(self._methodInfo)

	def tableView_objectValueForTableColumn_row_(self,    
	                         aTableView, aTableColumn, rowIndex):  
		print "objectValue", aTableView, aTableColumn, rowIndex
		return self._methodInfo[rowIndex][methodIdentifier[aTableColumn.identifier()]]
