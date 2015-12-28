from Foundation import *
from PyObjCTools.TestSupport import *

class TestAED (TestCase):
    def testCreateWithBytes(self):
        self.assertArgSizeInArg(NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_, 1, 2)
        self.assertArgIsIn(NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_, 1)

        self.assertArgSizeInArg(NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1, 2)
        self.assertArgIsIn(NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1)

        self.assertResultIsBOOL(NSAppleEventDescriptor.booleanValue)

#    def testInitWithAEDescNoCopy(self):
#        # The object will call AEDisposeDesc, meaning MacPython shouldn't
#        self.fail("Test for 'initWithAEDescNoCopy'")
#
#    def testAccess(self):
#        # Ensure Python doesn't call AEDisposeDesc
#        self.fail('-aeDesc')

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSAppleEventDescriptor.isRecordDescriptor)

    def testConstants(self):
        self.assertEqual(NSAppleEventSendNoReply, 1)
        self.assertEqual(NSAppleEventSendQueueReply, 2)
        self.assertEqual(NSAppleEventSendWaitForReply, 3)
        self.assertEqual(NSAppleEventSendNeverInteract, 16)
        self.assertEqual(NSAppleEventSendCanInteract, 32)
        self.assertEqual(NSAppleEventSendAlwaysInteract, 48)
        self.assertEqual(NSAppleEventSendCanSwitchLayer, 64)
        self.assertEqual(NSAppleEventSendDontRecord, 4096)
        self.assertEqual(NSAppleEventSendDontExecute, 8192)
        self.assertEqual(NSAppleEventSendDontAnnotate, 65536)
        self.assertEqual(NSAppleEventSendDefaultOptions, NSAppleEventSendWaitForReply | NSAppleEventSendCanInteract)




if __name__ == "__main__":
    main()
