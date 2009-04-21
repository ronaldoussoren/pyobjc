
from PyObjCTools.TestSupport import *
from Quartz.QuartzFilters import *

class TestQuartzFilterManager (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(QuartzFilterManager.selectFilter_)

    def testConstants(self):
        self.failUnlessIsInstance(kQuartzFilterManagerDidAddFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidRemoveFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidModifyFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidSelectFilterNotification, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        # The following definitions are documented for 10.5, but aren't actually
        # exported from the framework:
        self.failUnlessIsInstance(kQuartzFilterApplicationDomain, unicode)
        self.failUnlessIsInstance(kQuartzFilterPDFWorkflowDomain, unicode)
        self.failUnlessIsInstance(kQuartzFilterPrintingDomain, unicode)
                                                                                                         

if __name__ == "__main__":
    main()
