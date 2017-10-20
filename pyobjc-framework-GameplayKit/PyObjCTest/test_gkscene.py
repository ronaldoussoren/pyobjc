from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKAgent (TestCase):
        def testProtocols(self):
            objc.protocolNamed('GKSceneRootNodeType')


if __name__ == "__main__":
    main()
