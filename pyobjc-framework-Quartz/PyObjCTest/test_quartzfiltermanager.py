
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestQuartzFilterManager (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(QuartzFilterManager.selectFilter_)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kQuartzFilterManagerDidAddFilterNotification, unicode)
        self.assertIsInstance(kQuartzFilterManagerDidRemoveFilterNotification, unicode)
        self.assertIsInstance(kQuartzFilterManagerDidModifyFilterNotification, unicode)
        self.assertIsInstance(kQuartzFilterManagerDidSelectFilterNotification, unicode)


    @min_os_level('10.6')
    @expectedFailure
    def testConstants10_6(self):
        # The following definitions are documented for 10.5, but aren't actually
        # exported from the framework:
        self.assertIsInstance(kQuartzFilterApplicationDomain, unicode)
        self.assertIsInstance(kQuartzFilterPDFWorkflowDomain, unicode)
        self.assertIsInstance(kQuartzFilterPrintingDomain, unicode)


if __name__ == "__main__":
    main()
