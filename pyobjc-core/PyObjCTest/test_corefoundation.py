"""
Testcases for the CoreFoundation wrappers introduced in 1.5
"""
import objc
from PyObjCTools.TestSupport import *
import re
import sys

from PyObjCTest.corefoundation import *

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

if sys.version_info[0] == 3:
    unicode = str

class TestCoreFoundation (TestCase):
    def testTollFree(self):
        obj = OC_TestCoreFoundation.today()

        self.assertIs(CFDateRef, objc.lookUpClass("NSDate"))
        self.assertIsInstance(obj, CFDateRef)

        v = OC_TestCoreFoundation.formatDate_(obj)
        self.assertIsInstance(v, unicode)

        formatter = objc.lookUpClass("NSDateFormatter").new()
        formatter.setDateStyle_(OC_TestCoreFoundation.shortStyle())
        formatter.setTimeStyle_(OC_TestCoreFoundation.shortStyle())
        formatter.setLocale_(objc.lookUpClass("NSLocale").currentLocale())
        v2 = formatter.stringForObjectValue_(obj)

        # Arggh, I'm an idiot: the code above doesn't calculate the same
        # string as the C code in corefoundation.m.
        #print v , v2

    def testBridged(self):

        obj = OC_TestCoreFoundation.createUUID()

        self.assertIsInstance(obj, CFUUIDRef)

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assertIsInstance(formatted, unicode)
        self.assertTrue( re.match(
            r'[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}',
            formatted) )

        self.assertRaises(objc.error, objc.lookUpClass, "CFUUIDRef")


        # AnotherUUID claims to return an Object (objc._C_ID), check that
        # we correctly return an object of the right type in that case as well.
        obj = OC_TestCoreFoundation.anotherUUID()

        self.assertIsInstance(obj, CFUUIDRef)

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assertIsInstance(formatted, unicode)
        self.assertTrue( re.match(
            r'[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}',
            formatted) )

    # TODO: testcases that check that
    # 1) you cannot delete selectors
    # 2) or even add them
    # 3) but can add/update/delete new Python methods or other attributes
    #

    def testMutableTypes(self):
        cftype = objc.lookUpClass('NSCFType')

        def myMethod(self, arg):
            return '%s %s'%(self.__class__.__name__, arg)

        self.assertNotHasAttr(CFUUIDRef, 'myMethod')

        CFUUIDRef.myMethod = myMethod

        self.assertHasAttr(CFUUIDRef, 'myMethod')
        self.assertNotHasAttr(CFDateRef, 'myMethod')
        self.assertNotHasAttr(cftype, 'myMethod')

if __name__ == "__main__":
    main()
