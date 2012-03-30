from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSAnimationContext (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBlock(NSAnimationContext.completionHandler, 'v')
        self.assertArgIsBlock(NSAnimationContext.setCompletionHandler_, 0, 'v')

if __name__ == "__main__":
    main()
