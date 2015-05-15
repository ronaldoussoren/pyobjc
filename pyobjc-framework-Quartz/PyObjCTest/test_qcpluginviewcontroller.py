from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class QCPlugInHelper (QCPlugIn):
    def createViewController(self):
        return 1

class TestQCPlugInViewController (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsRetained(QCPlugIn.createViewController)
        self.assertResultIsRetained(QCPlugInHelper.createViewController)

if __name__ == "__main__":
    main()
