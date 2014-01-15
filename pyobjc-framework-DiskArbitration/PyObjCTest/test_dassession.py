from PyObjCTools.TestSupport import *

import DiskArbitration

try:
    long
except NameError:
    long = int

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
        DiskArbitration.DASessionScheduleWithRunLoop(obj, rl, DiskArbitration.CFCommonRunLoopModes)

        DiskArbitration.DASessionUnscheduleFromRunLoop(obj, rl, DiskArbitration.CFCommonRunLoopModes)

        DiskArbitration.DASessionSetDispatchQueue

        self.assertIsInstance(DiskArbitration.DAApprovalSessionGetTypeID(), (int, long))

        self.assertResultIsCFRetained(DiskArbitration.DAApprovalSessionCreate)
        ses = DiskArbitration.DAApprovalSessionCreate(None)
        self.assertIsInstance(ses, DiskArbitration.DAApprovalSessionRef)

        DAApprovalSessionScheduleWithRunLoop(ses, rl, DiskArbitration.CFCommonRunLoopModes)
        DAApprovalSessionUnscheduleFromRunLoop(ses, rl, DiskArbitration.CFCommonRunLoopModes)

if __name__ == "__main__":
    main()
