from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKVoiceChatService (TestCase):
        # NOTE: Class GKVoiceChatService is not available on OSX

        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertIsInstance(GameCenter.GKVoiceChatServiceErrorDomain, unicode)

if __name__ == "__main__":
    main()
