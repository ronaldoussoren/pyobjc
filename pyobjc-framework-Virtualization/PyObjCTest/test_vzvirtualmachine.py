from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZVirtualMachine(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Virtualization.VZVirtualMachineState)

    def test_constants(self):
        self.assertEqual(Virtualization.VZVirtualMachineStateStopped, 0)
        self.assertEqual(Virtualization.VZVirtualMachineStateRunning, 1)
        self.assertEqual(Virtualization.VZVirtualMachineStatePaused, 2)
        self.assertEqual(Virtualization.VZVirtualMachineStateError, 3)
        self.assertEqual(Virtualization.VZVirtualMachineStateStarting, 4)
        self.assertEqual(Virtualization.VZVirtualMachineStatePausing, 5)
        self.assertEqual(Virtualization.VZVirtualMachineStateResuming, 6)
        self.assertEqual(Virtualization.VZVirtualMachineStateStopping, 7)
        self.assertEqual(Virtualization.VZVirtualMachineStateSaving, 8)
        self.assertEqual(Virtualization.VZVirtualMachineStateRestoring, 9)

    def test_methods(self):
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.isSupported)
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.canStart)
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.canPause)
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.canResume)
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.canRequestStop)

        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.startWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.pauseWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.resumeWithCompletionHandler_, 0, b"v@"
        )

        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.requestStopWithError_)
        self.assertArgIsOut(Virtualization.VZVirtualMachine.requestStopWithError_, 0)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(Virtualization.VZVirtualMachine.canStop)

        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.stopWithCompletionHandler_, 0, b"v@"
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.startWithOptions_completionHandler_,
            1,
            b"v@",
        )

    @arch_only("arm64")
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.restoreMachineStateFromURL_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            Virtualization.VZVirtualMachine.saveMachineStateToURL_completionHandler_,
            1,
            b"v@",
        )
