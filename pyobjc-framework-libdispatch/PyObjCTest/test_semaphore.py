import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSemaphoreAPI(TestCase):
    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_semaphore_create, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_semaphore_create, 0, objc._C_LNG)

        self.assertResultHasType(libdispatch.dispatch_semaphore_wait, objc._C_LNG)
        self.assertArgHasType(libdispatch.dispatch_semaphore_wait, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_semaphore_wait, 1, objc._C_ULNGLNG)

        self.assertResultHasType(libdispatch.dispatch_semaphore_signal, objc._C_LNG)
        self.assertArgHasType(libdispatch.dispatch_semaphore_signal, 0, objc._C_ID)
