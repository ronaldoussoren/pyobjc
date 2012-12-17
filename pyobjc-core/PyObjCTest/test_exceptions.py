#
# Some more tests for exception handling.
# XXX: we should centralize all exception handling tests into this file, this
#      is now mostly used to check general unicode support in exceptions.
#
from __future__ import unicode_literals
from PyObjCTest.exceptions import *

from PyObjCTools.TestSupport import *
import objc, sys

class TestExceptionsFromObjC (TestCase):
    def testSimple(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseSimple()

        except objc.error as e:
            self.assertEqual(str(e), 'SimpleException - hello world')
            self.assertEqual(e._pyobjc_info_['name'], 'SimpleException')
            self.assertEqual(e._pyobjc_info_['reason'], 'hello world')
            self.assertEqual(e._pyobjc_info_['userInfo'], None)

    def testSimpleWithInfo(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseSimpleWithInfo()

        except objc.error as e:
            self.assertEqual(str(e), 'InfoException - Reason string')
            self.assertEqual(e._pyobjc_info_['name'], 'InfoException')
            self.assertEqual(e._pyobjc_info_['reason'], 'Reason string')
            self.assertEqual(e._pyobjc_info_['userInfo'], {
                'key1': 'value1',
                'key2': 'value2',
            })

    def testUnicodeName(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeName()

        except objc.error as e:
            if sys.version_info[0] == 2:
                self.assertEqual(str(e), 'SimpleException\u1234\u2049 - hello world'.encode('utf-8'))
            else:
                self.assertEqual(str(e), 'SimpleException\u1234\u2049 - hello world')
            self.assertEqual(e._pyobjc_info_['name'], 'SimpleException\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['reason'], 'hello world')
            self.assertEqual(e._pyobjc_info_['userInfo'], None)

    def testUnicodeReason(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeReason()

        except objc.error as e:
            if sys.version_info[0] == 2:
                self.assertEqual(str(e), 'SimpleException - hello world\u1234\u2049'.encode('utf-8'))
            else:
                self.assertEqual(str(e), 'SimpleException - hello world\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['name'], 'SimpleException')
            self.assertEqual(e._pyobjc_info_['reason'], 'hello world\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['userInfo'], None)

    def testUnicodeWithInfo(self):
        o = PyObjCTestExceptions.alloc().init()

        try:
            o.raiseUnicodeWithInfo()

        except objc.error as e:
            if sys.version_info[0] == 2:
                self.assertEqual(str(e), 'InfoException\u1234\u2049 - Reason string\u1234\u2049'.encode('utf-8'))
            else:
                self.assertEqual(str(e), 'InfoException\u1234\u2049 - Reason string\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['name'], 'InfoException\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['reason'], 'Reason string\u1234\u2049')
            self.assertEqual(e._pyobjc_info_['userInfo'], {
                'key1\u1234\u2049': 'value1\u1234\u2049',
                'key2\u1234\u2049': 'value2\u1234\u2049',
            })

    def testRaisingStringsInObjectiveC(self):
        # Bug #1741095, @throw anNSString

        o = PyObjCTestExceptions.alloc().init()
        try:
            o.raiseAString()

        except objc.error as e:
            self.assertEqual(e._pyobjc_exc_, "thrown string")

if __name__ == "__main__":
    main()
