from PyObjCTools.TestSupport import TestCase
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
    def test_protocols(self):
        self.assertProtocolExists("IKImageEditPanelDataSource", Quartz)

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIKImageEditPanelHelper.thumbnailWithMaximumSize_,
            0,
            Quartz.NSSize.__typestr__,
        )

        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasAdjustMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasEffectsMode)
        self.assertResultIsBOOL(TestIKImageEditPanelHelper.hasDetailsMode)
