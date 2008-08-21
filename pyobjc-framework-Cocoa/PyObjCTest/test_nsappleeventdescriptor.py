from Foundation import *
import unittest

class TestAED (unittest.TestCase):
    def testCreateWithBytes(self):
        self.fail("+ (NSAppleEventDescriptor *)descriptorWithDescriptorType:(DescType)descriptorType bytes:(const void *)bytes length:(NSUInteger)byteCount;")
        self.fail("- (id)initWithDescriptorType:(DescType)descriptorType bytes:(const void *)bytes length:(NSUInteger)byteCount;")

    def testInitWithAEDescNoCopy(self):
        # The object will call AEDisposeDesc, meaning MacPython shouldn't
        self.fail("Test for 'initWithAEDescNoCopy'")

    def testAccess(self):
        # Ensure Python doesn't call AEDisposeDesc
        self.fail('-aeDesc')


if __name__ == "__main__":
    unittest.main()
