from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKAgent (TestCase):
        def testProtocols(self):
            objc.protocolNamed('GKAgentDelegate')

        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKAgent3D.rightHanded)
            self.assertArgIsBOOL(GameplayKit.GKAgent3D.setRightHanded_, 0)


if __name__ == "__main__":
    main()
