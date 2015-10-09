
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIPlugIn (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(CIPlugIn.loadPlugIn_allowNonExecutable_, 1)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(CIPlugIn.loadPlugIn_allowExecutableCode_, 1)

if __name__ == "__main__":
    main()
