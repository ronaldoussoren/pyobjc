from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAMetalLayer (TestCase):
    @min_os_level('10.11')
    def testProtocols(self):
        objc.protocolNamed('CAMetalDrawable')

    @min_os_level('10.11')
    def testMethods(self):
        self.assertResultIsBOOL(CAMetalLayer.framebufferOnly)
        self.assertArgIsBOOL(CAMetalLayer.setFramebufferOnly_, 0)

        self.assertResultIsBOOL(CAMetalLayer.presentsWithTransaction)
        self.assertArgIsBOOL(CAMetalLayer.setPresentsWithTransaction_, 0)

        self.assertResultIsBOOL(CAMetalLayer.wantsExtendedDynamicRangeContent)
        self.assertArgIsBOOL(CAMetalLayer.setWantsExtendedDynamicRangeContent_, 0)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(CAMetalLayer.displaySyncEnabled)
        self.assertArgIsBOOL(CAMetalLayer.setDisplaySyncEnabled_, 0)

        self.assertResultIsBOOL(CAMetalLayer.allowsNextDrawableTimeout)
        self.assertArgIsBOOL(CAMetalLayer.setAllowsNextDrawableTimeout_, 0)

if __name__ == "__main__":
    main()
