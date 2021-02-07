"""
Minimal tests for sequence proxies

NOTE: this file is very, very incomplete and just tests copying at the moment.
"""

import objc
from PyObjCTest.pythonset import OC_TestSet
from PyObjCTools.TestSupport import TestCase

OC_PythonDictionary = objc.lookUpClass("OC_PythonDictionary")
OC_BuiltinPythonDictionary = objc.lookUpClass("OC_BuiltinPythonDictionary")


class TestDictionary(TestCase):
    mapClass = dict

    def testCopy(self):
        s = self.mapClass()
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

        s = self.mapClass({1: 2, "a": "c"})
        o = OC_TestSet.set_copyWithZone_(s, None)
        self.assertEqual(s, o)
        self.assertIsNot(s, o)

    def testProxyClass(self):
        # Ensure that the right class is used to proxy sets
        self.assertIs(OC_TestSet.classOf_(self.mapClass()), OC_BuiltinPythonDictionary)

    def testMutableCopy(self):

        s = self.mapClass({1: 2, "a": "c"})
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)

        s = self.mapClass()
        o = OC_TestSet.set_mutableCopyWithZone_(s, None)
        self.assertEqual(dict(s), o)
        self.assertIsNot(s, o)
        self.assertIsInstance(o, dict)
