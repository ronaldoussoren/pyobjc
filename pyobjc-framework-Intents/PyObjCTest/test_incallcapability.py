import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINCallCapability (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INCallCapabilityUnknown, 0)
            self.assertEqual(Intents.INCallCapabilityAudioCall, 1)
            self.assertEqual(Intents.INCallCapabilityVideoCall, 2)


if __name__ == "__main__":
    main()
