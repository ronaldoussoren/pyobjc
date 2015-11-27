from PyObjCTools.TestSupport import *

import DiskArbitration

class TestDASession (TestCase):
    def test_types(self):
        self.assertIsCFType(DiskArbitration.DASessionRef)
        self.assertIsCFType(DiskArbitration.DAApprovalSessionRef)

    def test_functions(self):
        self.assertIsInstance(DiskArbitration.DASessionGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiskArbitration.DASessionCreate)

        obj = DiskArbitration.DASessionCreate(None)
        self.assertIsInstance(obj, DiskArbitration.DASessionRef)

        rl = DiskArbitration.CFRunLoopGetCurrent()
        DiskArbitration.DASessionScheduleWithRunLoop(obj, rl, DiskArbitration.kCFRunLoopCommonModes)

        DiskArbitration.DASessionUnscheduleFromRunLoop(obj, rl, DiskArbitration.kCFRunLoopCommonModes)

        DiskArbitration.DASessionSetDispatchQueue

        self.assertIsInstance(DiskArbitration.DAApprovalSessionGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiskArbitration.DAApprovalSessionCreate)
        ses = DiskArbitration.DAApprovalSessionCreate(None)
        self.assertIsInstance(ses, DiskArbitration.DAApprovalSessionRef)

        DiskArbitration.DAApprovalSessionScheduleWithRunLoop(ses, rl, DiskArbitration.kCFRunLoopCommonModes)
        DiskArbitration.DAApprovalSessionUnscheduleFromRunLoop(ses, rl, DiskArbitration.kCFRunLoopCommonModes)

if __name__ == "__main__":
    main()
