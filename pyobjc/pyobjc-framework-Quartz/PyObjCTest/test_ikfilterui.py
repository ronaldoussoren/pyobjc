
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKFilterUI (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKUISizeFlavor, unicode)
        self.assertIsInstance(IKUISizeMini, unicode)
        self.assertIsInstance(IKUISizeSmall, unicode)
        self.assertIsInstance(IKUISizeRegular, unicode)
        self.assertIsInstance(IKUImaxSize, unicode)
        self.assertIsInstance(IKUIFlavorAllowFallback, unicode)

    @min_os_level('10.5')
    def no_testProtocol(self):
        self.assertIsInstance(objc.protocolNamed("IKFilterCustomUIProvider"), objc.formal_protocol)

if __name__ == "__main__":
    main()
