import DiskArbitration
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)


class TestDASession(TestCase):
    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.10")
    @min_os_level("10.10")
    def test_types(self):
        self.assertIsCFType(DiskArbitration.DASessionRef)
        self.assertIsCFType(DiskArbitration.DAApprovalSessionRef)

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertIsInstance(DiskArbitration.DASessionGetTypeID(), int)

        self.assertResultIsCFRetained(DiskArbitration.DASessionCreate)

        obj = DiskArbitration.DASessionCreate(None)
        self.assertIsInstance(obj, DiskArbitration.DASessionRef)

        rl = DiskArbitration.CFRunLoopGetCurrent()
        DiskArbitration.DASessionScheduleWithRunLoop(
            obj, rl, DiskArbitration.kCFRunLoopCommonModes
        )

        DiskArbitration.DASessionUnscheduleFromRunLoop(
            obj, rl, DiskArbitration.kCFRunLoopCommonModes
        )

        self.assertIsInstance(DiskArbitration.DAApprovalSessionGetTypeID(), int)

        self.assertResultIsCFRetained(DiskArbitration.DAApprovalSessionCreate)
        ses = DiskArbitration.DAApprovalSessionCreate(None)
        self.assertIsInstance(ses, DiskArbitration.DAApprovalSessionRef)

        DiskArbitration.DAApprovalSessionScheduleWithRunLoop(
            ses, rl, DiskArbitration.kCFRunLoopCommonModes
        )
        DiskArbitration.DAApprovalSessionUnscheduleFromRunLoop(
            ses, rl, DiskArbitration.kCFRunLoopCommonModes
        )

        DiskArbitration.DASessionSetDispatchQueue
