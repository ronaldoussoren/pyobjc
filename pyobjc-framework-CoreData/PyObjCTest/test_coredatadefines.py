import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCoreDataDefines(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreData.NSCoreDataVersionNumber, float)

        self.assertEqual(CoreData.NSCoreDataVersionNumber10_4, 46.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_4_3, 77.0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_5, 185.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_5_3, 186.0)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7, 358.4)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7_2, 358.12)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_7_3, 358.13)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_8, 407.5)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_8_2, 407.7)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9, 481.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9_2, 481.1)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_9_3, 481.3)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10, 526.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10_2, 526.1)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_10_3, 526.2)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_11, 640.0)
        self.assertEqual(CoreData.NSCoreDataVersionNumber10_11_3, 641.3)
