from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZVirtualMachine(TestCase):
    def test_constants(self):
        self.assertEqual(Virtualization.VZVirtualMachineStateStopped, 0)
        self.assertEqual(Virtualization.VZVirtualMachineStateRunning, 1)
        self.assertEqual(Virtualization.VZVirtualMachineStatePaused, 2)
        self.assertEqual(Virtualization.VZVirtualMachineStateError, 3)
        self.assertEqual(Virtualization.VZVirtualMachineStateStarting, 4)
        self.assertEqual(Virtualization.VZVirtualMachineStatePausing, 5)
        self.assertEqual(Virtualization.VZVirtualMachineStateResuming, 6)

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
