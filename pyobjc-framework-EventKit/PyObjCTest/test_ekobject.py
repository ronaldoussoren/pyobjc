from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKEvent(TestCase):
    @min_os_level("10.8")
    def test_basic(self):
        self.assertTrue(hasattr(EventKit, "EKObject"))

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(EventKit.EKObject.hasChanges)
        self.assertResultIsBOOL(EventKit.EKObject.isNew)
        self.assertResultIsBOOL(EventKit.EKObject.refresh)
