
from PyObjCTools.TestSupport import *
from Quartz import *

class TestQuartzFilterManager (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(QuartzFilterManager.selectFilter_)

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kQuartzFilterManagerDidAddFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidRemoveFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidModifyFilterNotification, unicode)
        self.failUnlessIsInstance(kQuartzFilterManagerDidSelectFilterNotification, unicode)


    @min_os_level('10.6')
    @expectedFailure
    def testConstants10_6(self):
        # The following definitions are documented for 10.5, but aren't actually
        # exported from the framework:
        self.failUnlessIsInstance(kQuartzFilterApplicationDomain, unicode)
        self.failUnlessIsInstance(kQuartzFilterPDFWorkflowDomain, unicode)
        self.failUnlessIsInstance(kQuartzFilterPrintingDomain, unicode)
                                                                                                         

if __name__ == "__main__":
    main()
