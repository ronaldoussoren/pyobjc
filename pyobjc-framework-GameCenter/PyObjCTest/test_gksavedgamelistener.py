from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKSavedGameListener (TestCase):
        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('GKSavedGameListener')

if __name__ == "__main__":
    main()
