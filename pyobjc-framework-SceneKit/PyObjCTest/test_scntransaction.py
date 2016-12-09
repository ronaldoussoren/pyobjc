from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    SCNBindingBlock = b'v' + objc._C_UINT + objc._C_UINT + b'@@'

    class TestSCNTransaction (TestCase):
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(SceneKit.SCNTransaction.disableActions)
            self.assertArgIsBOOL(SceneKit.SCNTransaction.setDisableActions_, 0)

            self.assertResultIsBlock(SceneKit.SCNTransaction.completionBlock, b'v')
            self.assertArgIsBlock(SceneKit.SCNTransaction.setCompletionBlock_, 0, b'v')


if __name__ == "__main__":
    main()
