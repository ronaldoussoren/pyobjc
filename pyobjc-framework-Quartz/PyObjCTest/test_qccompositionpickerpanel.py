from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCCompositionPickerPanel(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            Quartz.QCCompositionPickerPanelDidSelectCompositionNotification, str
        )
