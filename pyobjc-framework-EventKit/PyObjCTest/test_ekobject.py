from PyObjCTools.TestSupport import TestCase
import EventKit


class TestEKEvent(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKObject.hasChanges)
        self.assertResultIsBOOL(EventKit.EKObject.isNew)
        self.assertResultIsBOOL(EventKit.EKObject.refresh)
