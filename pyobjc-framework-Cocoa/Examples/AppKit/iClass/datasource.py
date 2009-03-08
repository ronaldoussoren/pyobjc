from Foundation import NSObject, NSBundle
from objc import selector, getClassList, objc_object, IBOutlet, IBAction

import objc
import AppKit
objc.setVerbose(1)

try:
    import AddressBook
except ImportError:
    pass

try:
    import PreferencePanes
except ImportError:
    pass

try:
    import InterfaceBuilder
except ImportError:
    pass

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

def wrap_object(obj):
    if WRAPPED.has_key(obj):
        return WRAPPED[obj]
    else:
        WRAPPED[obj] = Wrapper.alloc().init_(obj)
        return WRAPPED[obj]

def unwrap_object(obj):
    if obj is None:
        return obj
    return obj.value

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

class ClassesDataSource (NSObject):
    __slots__ = ('_classList', '_classTree', '_methodInfo', '_classInfo')

    classLabel = IBOutlet()
    classTable = IBOutlet()
    frameworkLabel = IBOutlet()
    methodTable = IBOutlet()
    searchBox = IBOutlet()
    window = IBOutlet()

    def clearClassInfo(self):
        self._methodInfo = []
        self.methodTable.reloadData()
        self.window.setTitle_('iClass')


    def setClassInfo(self, cls):
        self.window.setTitle_('iClass: %s'%cls.__name__)
        self.classLabel.setStringValue_(classPath(cls))
        self.frameworkLabel.setStringValue_(classBundle(cls))
        self._methodInfo = []
        for nm, meth in cls.pyobjc_instanceMethods.__dict__.items():
            if not isinstance(meth, selector):
                continue
            self._methodInfo.append(
                ('-'+meth.selector, nm, meth.signature))

        for nm, meth in cls.pyobjc_classMethods.__dict__.items():
            if not isinstance(meth, selector):
                continue
            self._methodInfo.append(
                ('+'+meth.selector, nm, meth.signature))
        self._methodInfo.sort()
        self.methodTable.reloadData()

    def outlineViewSelectionDidChange_(self, notification):
        rowNr = self.classTable.selectedRow()
        if rowNr == -1:
            self.clearClassInfo()
        else:
            item = self.classTable.itemAtRow_(rowNr)
            self.setClassInfo(unwrap_object(item))

    def showClass(self, cls):
        # First expand the tree (to make item visible)
        super = cls.__bases__[0]
        if  super == objc_object:
            return

        self.showClass(super)
        item = wrap_object(super)
        rowNr = self.classTable.rowForItem_(item)
        self.classTable.expandItem_(item)

    def selectClass(self, cls):
        self.showClass(cls)

        item = wrap_object(cls)
        rowNr = self.classTable.rowForItem_(item)

        self.classTable.scrollRowToVisible_(rowNr)
        self.classTable.selectRow_byExtendingSelection_(rowNr, False)

    @IBAction
    def searchClass_(self, event):
        val = self.searchBox.stringValue()
        if not val:
            return

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

        # mvl 2009-03-02: fix case where no match is found caused exception:
        if (found is None): return  
        
        self.setClassInfo(found)
        self.selectClass(found)


    def refreshClasses(self):
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

    def init(self):
        self._classInfo = getClassList()
        self.refreshClasses()
        return self

    def awakeFromNib(self):
        self._classInfo = getClassList()
        self.refreshClasses()


    def outlineView_child_ofItem_(self, outlineview, index, item):
        return wrap_object(self._classTree[unwrap_object(item)][index])

    def outlineView_isItemExpandable_(self, outlineview, item):
        return len(self._classTree[unwrap_object(item)]) != 0


    def outlineView_numberOfChildrenOfItem_(self, outlineview, item):
        return len(self._classTree[unwrap_object(item)])

    def outlineView_objectValueForTableColumn_byItem_(self, outlineview, column, item):
        if item is None:
            return '<None>'
        else:
            v = item.value
            return v.__name__


    def numberOfRowsInTableView_(self, aTableView):
        return len(self._methodInfo)

    def tableView_objectValueForTableColumn_row_(self,
                             aTableView, aTableColumn, rowIndex):
        return self._methodInfo[rowIndex][methodIdentifier[aTableColumn.identifier()]]
