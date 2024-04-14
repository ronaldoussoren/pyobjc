"""
Testcases for the CoreFoundation wrappers introduced in 1.5
"""

import re
import datetime
import sys

import objc
from PyObjCTest.corefoundation import OC_TestCoreFoundation
from PyObjCTools.TestSupport import TestCase

# registerCFSignature(name, encoding, typeId [, tollfreeName]) -> type

CFUUIDRef = objc.registerCFSignature(
    "CFUUIDRef",
    OC_TestCoreFoundation.signatureForCFUUIDRef(),
    OC_TestCoreFoundation.typeidForCFUUIDRef(),
)

CFDateRef = objc.registerCFSignature(
    "CFDateRef",
    OC_TestCoreFoundation.signatureForCFDateRef(),
    OC_TestCoreFoundation.typeidForCFDateRef(),
    "NSDate",
)

objc.registerMetaDataForSelector(
    b"OC_TestCoreFoundation",
    b"formatUUID2:",
    {
        "arguments": {
            2
            + 0: {
                "type_modifier": objc._C_OUT,
            }
        }
    },
)


class TestCoreFoundation(TestCase):
    def testTollFree(self):
        obj = OC_TestCoreFoundation.today()

        self.assertIs(CFDateRef, objc.lookUpClass("NSDate"))
        self.assertIsInstance(obj, CFDateRef)

        v = OC_TestCoreFoundation.formatDate_(obj)
        self.assertIsInstance(v, str)

        formatter = objc.lookUpClass("NSDateFormatter").new()
        formatter.setDateStyle_(OC_TestCoreFoundation.shortStyle())
        formatter.setTimeStyle_(OC_TestCoreFoundation.noStyle())
        formatter.setLocale_(objc.lookUpClass("NSLocale").currentLocale())
        v2 = formatter.stringForObjectValue_(obj)
        self.assertEqual(v2, v)

        self.assertIsInstance(repr(obj), str)
        self.assertIn(str(datetime.date.today()), repr(obj))

    def testBridged(self):
        obj = OC_TestCoreFoundation.createUUID()

        self.assertIsInstance(obj, CFUUIDRef)

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assertIsInstance(formatted, str)
        self.assertTrue(
            re.match(
                r"[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}",
                formatted,
            )
        )

        with self.assertRaisesRegex(objc.error, "^CFUUIDRef$"):
            objc.lookUpClass("CFUUIDRef")

        # AnotherUUID claims to return an Object (objc._C_ID), check that
        # we correctly return an object of the right type in that case as well.
        obj = OC_TestCoreFoundation.anotherUUID()

        self.assertIsInstance(obj, CFUUIDRef)

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assertIsInstance(formatted, str)
        self.assertTrue(
            re.match(
                r"[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}",
                formatted,
            )
        )

        self.assertIsInstance(repr(obj), str)
        self.assertIn("<CFUUID", repr(obj))
        self.assertIsInstance(str(obj), str)
        self.assertIn("<CFUUID", str(obj))

    def test_invalid_metata_for_cf_argument(self):
        obj = OC_TestCoreFoundation.createUUID()

        self.assertIsInstance(obj, CFUUIDRef)

        formatted = OC_TestCoreFoundation.formatUUID2_(obj)
        self.assertIsInstance(formatted, tuple)
        self.assertIsInstance(formatted[0], str)
        self.assertIsInstance(formatted[1], type(None))

    def test_default_bridged(self):
        value = OC_TestCoreFoundation.runloop()
        self.assertIsInstance(value, objc.lookUpClass("NSObject"))

        # XXX: A full test run currently loads CoreFoundation through
        # using Quartz...
        if "CoreFoundation" in sys.modules:
            self.assertIn("<core-foundation class CFRunLoop", str(type(value)))
        else:
            self.assertIn("CFType", str(type(value)))
        self.assertIn("<CFRunLoop ", str(value))

    # TODO: testcases that check that
    # 1) you cannot delete selectors
    # 2) or even add them
    # 3) but can add/update/delete new Python methods or other attributes
    #

    def testMutableTypes(self):
        cftype = objc.lookUpClass("NSCFType")

        @objc.python_method
        def myMethod(self, arg):
            return f"{self.__class__.__name__} {arg}"

        self.assertNotHasAttr(CFUUIDRef, "myMethod")

        CFUUIDRef.myMethod = myMethod

        self.assertHasAttr(CFUUIDRef, "myMethod")
        self.assertNotHasAttr(CFDateRef, "myMethod")
        self.assertNotHasAttr(cftype, "myMethod")
