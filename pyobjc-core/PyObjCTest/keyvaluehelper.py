"""
Helper module for KeyValue tests
"""
from PyObjCTest.testbndl import PyObjCTest_KVBaseClass, PyObjCTest_KVPathClass
import objc

NSObject = objc.lookUpClass('NSObject')

DirectString = u'Direct String'
IndirectString = u'Indirect String'
DirectNumber = 42
IndirectNumber = 84

class KVPyBase:
    def __init__(self):
        self.directString = DirectString
        self._indirectString = IndirectString
        self.directNumber = DirectNumber
        self._indirectNumber = IndirectNumber

    def get_indirectString(self):
        return self._indirectString

    def set_indirectString(self, aString):
        self._indirectString = aString

    def getIndirectNumber(self):
        return self._indirectNumber

    def setIndirectNumber(self, aNumber):
        self._indirectNumber = aNumber

class KVPyPath:
    def __init__(self):
        self.directHead = KVPyBase()
        self._indirectHead = KVPyBase()

    def indirectHead(self):
        return self._indirectHead

    def setIndirectHead(self, aHead):
        self._indirectHead = aHead

class KVPySubObjCBase (PyObjCTest_KVBaseClass):
    pass

class KVPySubObjCPath (PyObjCTest_KVPathClass):
    pass

class KVPySubOverObjCBase (PyObjCTest_KVBaseClass):
    def init(self):
        self = super(KVPySubOverObjCBase, self).init()
        if not self:
            return self

        self.overDirectString = DirectString
        self._overIndirectString = IndirectString
        return self

    def getOverIndirectString(self):
        return self._overIndirectString

    def setOverIndirectString_(self, aString):
        self._overIndirectString = aString

class KVPySubOverObjCPath(PyObjCTest_KVPathClass):
    def init(self):
        self = super(KVPySubOverObjCPath, self).init()
        self.overDirectHead = KVPySubOverObjCBase.new()
        self._overIndirectHead = KVPySubOverObjCBase.new()
        return self

    def overIndirectHead(self):
        return self._overIndirectHead

    def setOverIndirectHead_(self, aHead):
        self._overIndirectHead = aHead

class PyObjCTestObserver (NSObject):
    def init(self):
        self = super(PyObjCTestObserver, self).init()
        if self is not None:
            self.observed = []
            self.willChange = []
        return self

    def observeValueForKeyPath_ofObject_change_context_(self, keyPath, obj, change, context):
        self.observed.append( (keyPath, obj, change, context) )

    def willChangeValueForKey_(self, key):
        self.willChange.append(key)
