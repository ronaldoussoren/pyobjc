"""
Tests for PyObjCTools.KeyValueCoding

TODO: 
    - Accessing properties in superclass of ObjC hybrids (see also Foundation.test.test_keyvalue)

NOTE: Testcases here should be synchronized with the Key-Value Coding tests
in objc.test.test_keyvalue and Foundation.test.test_keyvalue.
"""

from PyObjCTools import KeyValueCoding
import objc
import unittest

from PyObjCTools.test.testkvcodingbndl import *

DirectString = u'Direct String'
IndirectString = u'Indirect String'
DirectNumber = 42
IndirectNumber = 84

class KVPyBase(KeyValueCoding.KeyValueCodingMixIn):
    def __init__(self):
        self.directString = DirectString
        self._indirectString = IndirectNumber
        self.directNumber = DirectNumber
        self._indirectNumber = IndirectNumber

    def indirectString(self):
        return self._indirectString
    def setIndirectString_(self, aString):
        self._indirectString = aString

    def indirectNumber(self):
        return self._indirectNumber
    def setIndirectNumber_(self, aNumber):
        self._indirectNumber = aNumber

class KVPyPath(KeyValueCoding.KeyValueCodingMixIn):
    def __init__(self):
        self.directHead = KVPyBase()
        self._indirectHead = KVPyBase()

    def indirectHead(self):
        return self._indirectHead
    def setIndirectHead_(self, aHead):
        self._indirectHead = aHead

class KVPySubObjCBase(KVBaseClass):
    pass

class KVPySubObjCPath(KVPathClass):
    pass

class KVPySubOverObjCBase(KVBaseClass):
    def init(self):
        super(KVPySubOverObjCBase, self).init()
        self.overDirect = DirectString
        self._overIndirect = IndirectString

    def overIndirectString(self):
        return self._overIndirect
    def setOverIndirectString_(self, aString):
        self._overIndirect = aString

class KVPySubOverObjCPath(KVPathClass):
    def init(self):
        super(KVPySubOverObjCPath, self).init()
        self.overDirectHead = KVPySubOverObjCBase.new()
        self._overIndirectHead = KVPySubOverObjCBase.new()

    def overIndirectHead(self):
        return self._overIndirectHead
    def setOverIndirectHead_(self, aHead):
        self._overIndirectHead = aHead

class AbstractKVCodingTest:
    def testBaseCValueForKey(self):
        self.assertEquals(DirectString, self.base.valueForKey_("directString"))
        self.assertEquals(IndirectString, self.base.valueForKey_("indirectString"))
        self.assertEquals(DirectNumber, self.base.valueForKey_("directNumber"))
        self.assertEquals(IndirectNumber, self.base.valueForKey_("indirectNumber"))

    def testPathValueForKey(self):
        self.assertEquals(DirectString, self.path.valueForKeyPath_("directHead.directString"))
        self.assertEquals(IndirectString, self.path.valueForKeyPath_("indirectHead.indirectString"))
        self.assertEquals(DirectNumber, self.path.valueForKeyPath_("directHead.directNumber"))
        self.assertEquals(IndirectNumber, self.path.valueForKeyPath_("indirectHead.indirectNumber"))
        
class TestObjCKVCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVBaseClass.new()
        self.path = KVPathClass.new()

class TestPythonKVCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPyBase()
        self.path = KVPyPath()

class TestPythonSubObjCContainerCoding(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPySubObjCBase.new()
        self.path = KVPySubObjCPath.new()

class TestPythonSubOverObjC(AbstractKVCodingTest, unittest.TestCase):
    def setUp(self):
        self.base = KVPySubOverObjCBase.new()
        self.path = KVPySubOverObjCPath.new()

    def testOverValueForKey(self):
        self.assertEquals(DirectString, self.base.valueForKey_("overDirectString"))
        self.assertEquals(IndirectString, self.base.valueForKey_("overIndirectString"))

    def testOverValueForKeyPath(self):
        self.assertEquals(DirectString, self.path.valueForKeyPath_("overDirectHead.directString"))
        self.assertEquals(IndirectString, self.path.valueForKeyPath_("overIndirectHead.indirectString"))

if __name__ == "__main__":
    unittest.main()
