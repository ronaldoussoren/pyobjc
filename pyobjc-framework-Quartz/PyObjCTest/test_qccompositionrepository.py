
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCCompositionRepository (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(QCCompositionRepositoryDidUpdateNotification, unicode)

if __name__ == "__main__":
    main()
