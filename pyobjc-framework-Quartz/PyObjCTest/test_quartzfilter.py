
from PyObjCTools.TestSupport import *
from Quartz import *

class TestQuartzFilter (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(QuartzFilter.applyToContext_)

if __name__ == "__main__":
    main()
