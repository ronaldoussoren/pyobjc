import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSpeakable (TestCase):
        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('INSpeakable')

if __name__ == "__main__":
    main()
