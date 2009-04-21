
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKFilterUI (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(IKUISizeFlavor, unicode)
        self.failUnlessIsInstance(IKUISizeMini, unicode)
        self.failUnlessIsInstance(IKUISizeSmall, unicode)
        self.failUnlessIsInstance(IKUISizeRegular, unicode)
        self.failUnlessIsInstance(IKUImaxSize, unicode)
        self.failUnlessIsInstance(IKUIFlavorAllowFallback, unicode)

    def no_testProtocol(self):
        self.failUnlessIsInstance(objc.protocolNamed("IKFilterCustomUIProvider"), objc.formal_protocol)

if __name__ == "__main__":
    main()
