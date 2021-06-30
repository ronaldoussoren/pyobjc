from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKVirtualConferenceProvider(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            EventKit.EKVirtualConferenceProvider.fetchAvailableRoomTypesWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            EventKit.EKVirtualConferenceProvider.fetchVirtualConferenceForIdentifier_completionHandler_,
            1,
            b"v@@",
        )
