from Foundation import *
from PyObjCTools.TestSupport import *

class TestAED (TestCase):
    def testCreateWithBytes(self):
        self.assertArgSizeInArg(NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_, 1, 2)
        self.assertArgIsIn(NSAppleEventDescriptor.descriptorWithDescriptorType_bytes_length_, 1)

        self.assertArgSizeInArg(NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1, 2)
        self.assertArgIsIn(NSAppleEventDescriptor.initWithDescriptorType_bytes_length_, 1)

#    def testInitWithAEDescNoCopy(self):
#        # The object will call AEDisposeDesc, meaning MacPython shouldn't
#        self.fail("Test for 'initWithAEDescNoCopy'")
#
#    def testAccess(self):
#        # Ensure Python doesn't call AEDisposeDesc
#        self.fail('-aeDesc')


if __name__ == "__main__":
    main()
