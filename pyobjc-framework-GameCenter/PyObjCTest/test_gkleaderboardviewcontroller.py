from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKLeaderboardViewController (TestCase):
        @min_os_level('10.8')
        def testProtocols(self):
            objc.protocolNamed('GKLeaderboardViewControllerDelegate')

if __name__ == "__main__":
    main()
