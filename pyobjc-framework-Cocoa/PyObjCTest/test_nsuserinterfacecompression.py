from PyObjCTools.TestSupport import *

from AppKit import *
import objc


class TestNSUserInterfaceCompression (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(NSUserInterfaceCompressionOptions.containsOptions_)
        self.assertResultIsBOOL(NSUserInterfaceCompressionOptions.intersectsOptions_)
        self.assertResultIsBOOL(NSUserInterfaceCompressionOptions.isEmpty)
        #self.assertArgIsBOOL(NSUserInterfaceCompressionOptions.setEmpty_)

    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('NSUserInterfaceCompression')


if __name__ == "__main__":
    main()
