import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestMultiProcessingInfo(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("MPGetNextCpuID")
        self.assert_not_wrapped("MPGetNextTaskID")
        self.assert_not_wrapped("kMPQueueInfoVersion")
        self.assert_not_wrapped("kMPSemaphoreInfoVersion")
        self.assert_not_wrapped("kMPEventInfoVersion")
        self.assert_not_wrapped("kMPCriticalRegionInfoVersion")
        self.assert_not_wrapped("kMPNotificationInfoVersion")
        self.assert_not_wrapped("kMPAddressSpaceInfoVersion")
        self.assert_not_wrapped("MPQueueInfo")
        self.assert_not_wrapped("MPSemaphoreInfo")
        self.assert_not_wrapped("MPEventInfo")
        self.assert_not_wrapped("MPCriticalRegionInfo")
        self.assert_not_wrapped("MPNotificationInfo")
        self.assert_not_wrapped("MPAddressSpaceInfo")
        self.assert_not_wrapped("")
