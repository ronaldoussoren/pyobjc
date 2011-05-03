'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import CoreData

class TestCoreData (TestCase):
    def testClasses(self):
        self.assert_( hasattr(CoreData, 'NSAttributeDescription') )
        self.assert_( isinstance(CoreData.NSAttributeDescription, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(CoreData, 'NSCoreDataVersionNumber10_4_3') )
        self.assert_( isinstance(CoreData.NSCoreDataVersionNumber10_4_3, float) )
        self.assertEquals(CoreData.NSCoreDataVersionNumber10_4_3, 77.0)

        self.assert_( hasattr(CoreData, 'NSValidationMultipleErrorsError') )
        self.assert_( isinstance(CoreData.NSValidationMultipleErrorsError, (int, long)) )
        self.assertEquals(CoreData.NSValidationMultipleErrorsError, 1560)

    def testVariables(self):
        self.assert_( hasattr(CoreData, 'NSCoreDataVersionNumber') )
        self.assert_( isinstance(CoreData.NSCoreDataVersionNumber, float) )

        self.assert_( hasattr(CoreData, 'NSDetailedErrorsKey') )
        self.assert_( isinstance(CoreData.NSDetailedErrorsKey, unicode) )

        self.assert_( hasattr(CoreData, 'NSErrorMergePolicy') )
        self.assert_( isinstance(CoreData.NSErrorMergePolicy, objc.objc_object) )

if __name__ == "__main__":
    main()
