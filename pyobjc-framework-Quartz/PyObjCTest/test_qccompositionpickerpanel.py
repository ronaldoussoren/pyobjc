
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

try:
    unicode
except NameError:
    unicode = str

class TestQCCompositionPickerPanel (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QCCompositionPickerPanelDidSelectCompositionNotification, unicode)

if __name__ == "__main__":
    main()
