
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKImageEditPanelHelper (NSObject):
    def thumbnailWithMaximumSize_(self, sz): return None
    def hasAdjustMode(self): return 1
    def hasEffectsMode(self): return 1
    def hasDetailsMode(self): return 1

class TestIKImageEditPanel (TestCase):
    @min_os_level('10.5')
    def no_testProtocols(self):
        self.assertIsInstance(objc.protocolNamed('IKImageEditPanel'), objc.formal_protocol)

    @min_os_level('10.5')
    def testProtocolMethods(self):
        self.assertArgHasType(TestIKImageEditPanelHelper.thumbnailWithMaximumSize_, 0, NSSize.__typestr__)

    @min_os_level('10.6')
    def testProtocolMethods10_6(self):
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasAdjustMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasEffectsMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasDetailsMode)

if __name__ == "__main__":
    main()
