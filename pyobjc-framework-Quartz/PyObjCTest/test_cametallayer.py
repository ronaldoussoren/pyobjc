from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCAMetalLayer(TestCase):
    @min_os_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("CAMetalDrawable")

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.CAMetalLayer.framebufferOnly)
        self.assertArgIsBOOL(Quartz.CAMetalLayer.setFramebufferOnly_, 0)

        self.assertResultIsBOOL(Quartz.CAMetalLayer.presentsWithTransaction)
        self.assertArgIsBOOL(Quartz.CAMetalLayer.setPresentsWithTransaction_, 0)

        self.assertResultIsBOOL(Quartz.CAMetalLayer.wantsExtendedDynamicRangeContent)
        self.assertArgIsBOOL(
            Quartz.CAMetalLayer.setWantsExtendedDynamicRangeContent_, 0
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Quartz.CAMetalLayer.displaySyncEnabled)
        self.assertArgIsBOOL(Quartz.CAMetalLayer.setDisplaySyncEnabled_, 0)

        self.assertResultIsBOOL(Quartz.CAMetalLayer.allowsNextDrawableTimeout)
        self.assertArgIsBOOL(Quartz.CAMetalLayer.setAllowsNextDrawableTimeout_, 0)
