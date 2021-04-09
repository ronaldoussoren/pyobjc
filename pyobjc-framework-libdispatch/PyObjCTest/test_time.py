import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestTime(TestCase):
    def test_constants(self):
        self.assertEqual(libdispatch.NSEC_PER_SEC, 1_000_000_000)
        self.assertEqual(libdispatch.NSEC_PER_MSEC, 1_000_000)
        self.assertEqual(libdispatch.USEC_PER_SEC, 1_000_000)
        self.assertEqual(libdispatch.NSEC_PER_USEC, 1000)

        self.assertEqual(libdispatch.DISPATCH_TIME_FOREVER, 18446744073709551615)

        self.assertEqual(libdispatch.DISPATCH_TIME_NOW, 0)
        self.assertEqual(libdispatch.DISPATCH_TIME_FOREVER, 0xFFFFFFFFFFFFFFFF)

    def test_structs(self):

        tv = libdispatch.timespec(50, 100)
        self.assertEqual(tv.tv_sec, 50)
        self.assertEqual(tv.tv_nsec, 100)

        tv = libdispatch.timespec()
        self.assertEqual(tv.tv_sec, 0)
        self.assertEqual(tv.tv_nsec, 0)

    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_time, objc._C_ULNGLNG)
        self.assertArgHasType(libdispatch.dispatch_time, 0, objc._C_ULNGLNG)
        self.assertArgHasType(libdispatch.dispatch_time, 1, objc._C_LNGLNG)

        self.assertResultHasType(libdispatch.dispatch_walltime, objc._C_ULNGLNG)
        self.assertArgHasType(libdispatch.dispatch_walltime, 0, b"n^{timespec=ll}")
        self.assertArgHasType(libdispatch.dispatch_walltime, 1, objc._C_LNGLNG)
