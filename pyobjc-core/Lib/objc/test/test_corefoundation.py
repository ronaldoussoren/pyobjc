"""
Testcases for the CoreFoundation wrappers introduced in 1.5
"""
import objc
import objc.test
import re

from objc.test.corefoundation import *

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

class TestCoreFoundation (objc.test.TestCase):
    def testTollFree(self):
        obj = OC_TestCoreFoundation.today()

        self.assert_( CFDateRef, objc.lookUpClass("NSDate") ) 
        self.assert_( isinstance(obj, CFDateRef) )

        v = OC_TestCoreFoundation.formatDate_(obj)
        self.assert_( isinstance(v, unicode) )

        formatter = objc.lookUpClass("NSDateFormatter").new()
        formatter.setDateStyle_(OC_TestCoreFoundation.shortStyle())
        formatter.setTimeStyle_(OC_TestCoreFoundation.shortStyle())
        formatter.setLocale_(objc.lookUpClass("NSLocale").currentLocale())
        v2 = formatter.stringForObjectValue_(obj)
        
        # Arggh, I'm an idiot: the code above doesn't calculate the same
        # string as the C code in corefoundation.m.
        #print v , v2

    def testBridged(self):

        obj = OC_TestCoreFoundation.newUUID()

        self.assert_( isinstance(obj, CFUUIDRef) )
        self.assert_( isinstance(obj, objc.lookUpClass("NSCFType")) )

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assert_( isinstance(formatted, unicode) )
        self.assert_( re.match(
            r'[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}', 
            formatted) )


        # AnotherUUID claims to return an Object (objc._C_ID), check that
        # we correctly return an object of the right type in that case as well.
        obj = OC_TestCoreFoundation.anotherUUID()

        self.assert_( isinstance(obj, CFUUIDRef) )
        self.assert_( isinstance(obj, objc.lookUpClass("NSCFType")) )

        formatted = OC_TestCoreFoundation.formatUUID_(obj)

        self.assert_( isinstance(formatted, unicode) )
        self.assert_( re.match(
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

        self.assert_( not hasattr( CFUUIDRef, 'myMethod') )

        CFUUIDRef.myMethod = myMethod

        self.assert_( hasattr( CFUUIDRef, 'myMethod') )
        self.assert_( not hasattr( CFDateRef, 'myMethod'))
        self.assert_( not hasattr( cftype, 'myMethod'))

if __name__ == "__main__":
    objc.test.main()
    

