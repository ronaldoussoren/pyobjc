import CoreData
from PyObjCTools.TestSupport import TestCase


class TestCoreDataDefines(TestCase):
    def test_constants(self):
        self.assertIsInstance(CoreData.NSCoreDataVersionNumber, float)

        self.assertEqual(CoreData.NSCoreDataVersionNumber10_4, 46.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_4_3, 77.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_5, 185.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_5_3, 186.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7, 358.4)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7_2, 358.12)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7_3, 358.13)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_8, 407.5)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_8_2, 407.7)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9, 481.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9_2, 481.1)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9_3, 481.3)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10, 526.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10_2, 526.1)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10_3, 526.2)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_11, 640.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_11_3, 641.3)
