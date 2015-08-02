from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class TestGKAchievementViewController (TestCase):
        @min_os_level('10.8')
        def testClasses10_8(self):
            self.assertIsInstance(GameCenter.GKAchievementViewController, objc.objc_class)

        @min_os_level('10.8')
        def testProtocols10_8(self):
            objc.protocolNamed('GKAchievementViewControllerDelegate')

if __name__ == "__main__":
    main()
