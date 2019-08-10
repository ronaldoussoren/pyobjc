"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import CoreData


class TestCoreData(TestCase):
    def testClasses(self):
        self.assertHasAttr(CoreData, "NSAttributeDescription")
        self.assertIsInstance(CoreData.NSAttributeDescription, objc.objc_class)

    def testValues(self):
        self.assertHasAttr(CoreData, "NSCoreDataVersionNumber10_4_3")
        self.assertIsInstance(CoreData.NSCoreDataVersionNumber10_4_3, float)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_4_3, 77.0)

        self.assertHasAttr(CoreData, "NSValidationMultipleErrorsError")
        self.assertIsInstance(CoreData.NSValidationMultipleErrorsError, (int, long))
        self.assertEqual(CoreData.NSValidationMultipleErrorsError, 1560)

    def testVariables(self):
        self.assertHasAttr(CoreData, "NSCoreDataVersionNumber")
        self.assertIsInstance(CoreData.NSCoreDataVersionNumber, float)

        self.assertHasAttr(CoreData, "NSDetailedErrorsKey")
        self.assertIsInstance(CoreData.NSDetailedErrorsKey, unicode)


if __name__ == "__main__":
    main()
