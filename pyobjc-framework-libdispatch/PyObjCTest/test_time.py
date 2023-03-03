import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, cast_ulonglong


class TestTime(TestCase):
    def test_constants(self):
        self.assertEqual(dispatch.NSEC_PER_SEC, 1_000_000_000)
        self.assertEqual(dispatch.NSEC_PER_MSEC, 1_000_000)
        self.assertEqual(dispatch.USEC_PER_SEC, 1_000_000)
        self.assertEqual(dispatch.NSEC_PER_USEC, 1000)

        self.assertEqual(dispatch.DISPATCH_TIME_FOREVER, 18446744073709551615)

        self.assertEqual(dispatch.DISPATCH_TIME_NOW, 0)
        self.assertEqual(dispatch.DISPATCH_TIME_FOREVER, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(dispatch.DISPATCH_WALLTIME_NOW, cast_ulonglong(-1))

    def test_structs(self):
        tv = dispatch.timespec(50, 100)
        self.assertEqual(tv.tv_sec, 50)
        self.assertEqual(tv.tv_nsec, 100)
        self.assertPickleRoundTrips(tv)

        tv = dispatch.timespec()
        self.assertEqual(tv.tv_sec, 0)
        self.assertEqual(tv.tv_nsec, 0)
        self.assertPickleRoundTrips(tv)

    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultHasType(dispatch.dispatch_time, objc._C_ULNGLNG)
        self.assertArgHasType(dispatch.dispatch_time, 0, objc._C_ULNGLNG)
        self.assertArgHasType(dispatch.dispatch_time, 1, objc._C_LNGLNG)

        self.assertResultHasType(dispatch.dispatch_walltime, objc._C_ULNGLNG)
        self.assertArgHasType(dispatch.dispatch_walltime, 0, b"n^{timespec=ll}")
        self.assertArgHasType(dispatch.dispatch_walltime, 1, objc._C_LNGLNG)
