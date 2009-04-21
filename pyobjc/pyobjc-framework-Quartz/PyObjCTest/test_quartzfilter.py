
from PyObjCTools.TestSupport import *
from Quartz.QuartzFilters import *

class TestQuartzFilter (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(QuartzFilter.applyToContext_)

if __name__ == "__main__":
    main()
