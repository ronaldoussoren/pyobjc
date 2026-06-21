from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestIKImageEditPanelHelper(Quartz.NSObject):
    def thumbnailWithMaximumSize_(self, sz):
        return None

    def hasAdjustMode(self):
        return 1

    def hasEffectsMode(self):
        return 1

    def hasDetailsMode(self):
        return 1


class TestIKImageEditPanel(TestCase):
    @min_os_level("10.5")
    def no_test_protocols(self):
        self.assertProtocolExists("IKImageEditPanel", Quartz)
        self.assertProtocolExists("IKImageEditPanelDataSource", Quartz)

    @min_os_level("10.5")
    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIKImageEditPanelHelper.thumbnailWithMaximumSize_,
            0,
            Quartz.NSSize.__typestr__,
        )

    @min_os_level("10.6")
    def test_protocol_methods10_6(self):
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasAdjustMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasEffectsMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasDetailsMode)
