import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINCallRecordTypeOptions (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INCallRecordTypeOptionOutgoing, 1 << 0)
            self.assertEqual(Intents.INCallRecordTypeOptionMissed, 1 << 1)
            self.assertEqual(Intents.INCallRecordTypeOptionReceived, 1 << 2)
            self.assertEqual(Intents.INCallRecordTypeOptionLatest, 1 << 3)
            self.assertEqual(Intents.INCallRecordTypeOptionVoicemail, 1 << 4)



if __name__ == "__main__":
    main()
