
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKImageEditPanelHelper (NSObject):
    def thumbnailWithMaximumSize_(self, sz):
        return None

class TestIKImageEditPanel (TestCase):
    def no_testProtocols(self):
        self.failUnlessIsInstance(objc.protocolNamed('IKImageEditPanel'), objc.formal_protocol)

    def testProtocolMethods(self):
        self.failUnlessArgHasType(TestIKImageEditPanelHelper.thumbnailWithMaximumSize_, 0, NSSize.__typestr__)

if __name__ == "__main__":
    main()
