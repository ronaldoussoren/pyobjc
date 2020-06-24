import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit

SCNBindingBlock = b"v" + objc._C_UINT + objc._C_UINT + b"@@"


class TestSCNTechnique(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            SceneKit.SCNTechnique.handleBindingOfSymbol_usingBlock_, 1, SCNBindingBlock
        )

    @min_os_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("SCNTechniqueSupport")
