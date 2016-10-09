import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINCallCapabilityOptionsResolutionResult (TestCase):
        @min_os_level('10.12')
        def testClasses(self):
            self.assertIsInstance(Intents.INCallCapabilityOptionsResolutionResult, objc.objc_class)

if __name__ == "__main__":
    main()
