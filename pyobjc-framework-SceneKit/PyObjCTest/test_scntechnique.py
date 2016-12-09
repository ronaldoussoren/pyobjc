from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    SCNBindingBlock = b'v' + objc._C_UINT + objc._C_UINT + b'@@'

    class TestSCNTechnique (TestCase):
        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertArgIsBlock(SceneKit.SCNTechnique.handleBindingOfSymbol_usingBlock_, 1, SCNBindingBlock)


        @min_os_level('10.11')
        def testProtocols(self):
            objc.protocolNamed('SCNTechniqueSupport')

if __name__ == "__main__":
    main()
