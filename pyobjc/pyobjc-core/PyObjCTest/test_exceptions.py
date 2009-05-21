# 
# Some more tests for exception handling.
# XXX: we should centralize all exception handling tests into this file, this
#      is now mostly used to check general unicode support in exceptions.
#
from PyObjCTest.exceptions import *

from PyObjCTools.TestSupport import *
import objc

class TestExceptionsFromObjC (TestCase):
    def testSimple(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseSimple()

        except objc.error, e:
            self.assertEquals(str(e), 'SimpleException - hello world')
            self.assertEquals(e._pyobjc_info_['name'], u'SimpleException')
            self.assertEquals(e._pyobjc_info_['reason'], u'hello world')
            self.assertEquals(e._pyobjc_info_['userInfo'], None)

    def testSimpleWithInfo(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseSimpleWithInfo()

        except objc.error, e:
            self.assertEquals(str(e), 'InfoException - Reason string')
            self.assertEquals(e._pyobjc_info_['name'], u'InfoException')
            self.assertEquals(e._pyobjc_info_['reason'], u'Reason string')
            self.assertEquals(e._pyobjc_info_['userInfo'], {
                'key1': 'value1',
                'key2': 'value2',
            })

    def testUnicodeName(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeName()

        except objc.error, e:
            self.assertEquals(str(e), u'SimpleException\u1234\u2049 - hello world'.encode('utf-8'))
            self.assertEquals(e._pyobjc_info_['name'], u'SimpleException\u1234\u2049')
            self.assertEquals(e._pyobjc_info_['reason'], u'hello world')
            self.assertEquals(e._pyobjc_info_['userInfo'], None)

    def testUnicodeReason(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeReason()

        except objc.error, e:
            self.assertEquals(str(e), u'SimpleException - hello world\u1234\u2049'.encode('utf-8'))
            self.assertEquals(e._pyobjc_info_['name'], u'SimpleException')
            self.assertEquals(e._pyobjc_info_['reason'], u'hello world\u1234\u2049')
            self.assertEquals(e._pyobjc_info_['userInfo'], None)

    def testUnicodeWithInfo(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeWithInfo()

        except objc.error, e:
            self.assertEquals(str(e), u'InfoException\u1234\u2049 - Reason string\u1234\u2049'.encode('utf-8'))
            self.assertEquals(e._pyobjc_info_['name'], u'InfoException\u1234\u2049')
            self.assertEquals(e._pyobjc_info_['reason'], u'Reason string\u1234\u2049')
            self.assertEquals(e._pyobjc_info_['userInfo'], {
                u'key1\u1234\u2049': u'value1\u1234\u2049',
                u'key2\u1234\u2049': u'value2\u1234\u2049',
            })

    def testRaisingStringsInObjectiveC(self):
        # Bug #1741095, @throw anNSString

        o = PyObjCTestExceptions.alloc().init()
        try:
            o.raiseAString()

        except objc.error, e:
            self.assertEquals(e._pyobjc_exc_, u"thrown string")

if __name__ == "__main__":
    main()
