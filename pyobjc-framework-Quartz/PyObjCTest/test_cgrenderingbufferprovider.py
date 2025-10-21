from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGRenderingBufferProvider(TestCase):
    @min_os_level("26.0")
    def test_functions(self):
        self.assertResultIsCFRetained(Quartz.CGRenderingBufferProviderCreate)
        self.assertArgIsIn(Quartz.CGRenderingBufferProviderCreate, 0)
        self.assertArgSizeInArg(Quartz.CGRenderingBufferProviderCreate, 0, 1)

        self.assertResultIsCFRetained(Quartz.CGRenderingBufferProviderCreateWithCFData)
        Quartz.CGRenderingBufferProviderGetSize
        self.assertResultIsVariableSize(Quartz.CGRenderingBufferLockBytePtr)
        Quartz.CGRenderingBufferUnlockBytePtr
        Quartz.CGRenderingBufferProviderGetTypeID
