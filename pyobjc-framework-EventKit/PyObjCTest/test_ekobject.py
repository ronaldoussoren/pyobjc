from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKEvent(TestCase):
    @min_os_level("10.8")
    def testBasic(self):
        self.assertTrue(hasattr(EventKit, "EKObject"))

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(EventKit.EKObject.hasChanges)
        self.assertResultIsBOOL(EventKit.EKObject.isNew)
        self.assertResultIsBOOL(EventKit.EKObject.refresh)
