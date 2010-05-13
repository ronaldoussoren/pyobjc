"""
Minimal tests for sequence proxies

NOTE: this file is very, very incomplete and just tests copying at the moment.
"""
import sys
from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSDictionary, NSMutableDictionary, NSPredicate, NSObject, NSNull
from PyObjCTest.pythonset import OC_TestSet
import objc

OC_PythonDictionary = objc.lookUpClass("OC_PythonDictionary")





class TestMutableSequence (TestCase):
    mapClass = dict

    def testCopy(self):
        s = self.mapClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)

        s = self.mapClass({1:2, 'a':'c'})
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEquals(s, o)
        self.assertIsNot(s, o)

    def testProxyClass(self):
        # Ensure that the right class is used to proxy sets
        self.assertIs(OC_TestSet.classOf_(self.mapClass()), OC_PythonDictionary)

    def testMutableCopy(self):

        s = self.mapClass({1:2, 'a':'c'})
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)

        s = self.mapClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEquals(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)




if __name__ == "__main__":
    main()
