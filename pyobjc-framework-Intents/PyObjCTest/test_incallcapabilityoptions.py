import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINCallCapabilityOptions (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INCallCapabilityOptionAudioCall, 1 << 0)
            self.assertEqual(Intents.INCallCapabilityOptionVideoCall, 1 << 1)

if __name__ == "__main__":
    main()
