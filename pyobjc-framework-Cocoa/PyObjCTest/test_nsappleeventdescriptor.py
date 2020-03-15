import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAED(TestCase):
    def testCreateWithBytes(self):
        self.assertArgSizeInArg(
            Foundation.NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_,
            1,
            2,
        )
        self.assertArgIsIn(
            Foundation.NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_,
            1,
        )

        self.assertArgSizeInArg(
            Foundation.NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1, 2
        )
        self.assertArgIsIn(
            Foundation.NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1
        )

        self.assertResultIsBOOL(Foundation.NSAppleEventDescriptor.booleanValue)

    #    def testInitWithAEDescNoCopy(self):
    #        # The object will call AEDisposeDesc, meaning MacPython shouldn't
    #        self.fail("Test for 'initWithAEDescNoCopy'")
    #
    #    def testAccess(self):
    #        # Ensure Python doesn't call AEDisposeDesc
    #        self.fail('-aeDesc')

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(Foundation.NSAppleEventDescriptor.isRecordDescriptor)

    def testConstants(self):
        self.assertEqual(Foundation.NSAppleEventSendNoReply, 1)
        self.assertEqual(Foundation.NSAppleEventSendQueueReply, 2)
        self.assertEqual(Foundation.NSAppleEventSendWaitForReply, 3)
        self.assertEqual(Foundation.NSAppleEventSendNeverInteract, 16)
        self.assertEqual(Foundation.NSAppleEventSendCanInteract, 32)
        self.assertEqual(Foundation.NSAppleEventSendAlwaysInteract, 48)
        self.assertEqual(Foundation.NSAppleEventSendCanSwitchLayer, 64)
        self.assertEqual(Foundation.NSAppleEventSendDontRecord, 4096)
        self.assertEqual(Foundation.NSAppleEventSendDontExecute, 8192)
        self.assertEqual(Foundation.NSAppleEventSendDontAnnotate, 65536)
        self.assertEqual(
            Foundation.NSAppleEventSendDefaultOptions,
            Foundation.NSAppleEventSendWaitForReply
            | Foundation.NSAppleEventSendCanInteract,
        )
