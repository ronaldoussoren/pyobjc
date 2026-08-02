import os
import tempfile

from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz
import contextlib


@contextlib.contextmanager
def saved_system_stderr():
    result = []
    saved_stderr = os.dup(2)

    try:
        with tempfile.TemporaryFile() as fp:
            os.dup2(fp.fileno(), 2)
            yield result

            fp.seek(0)
            result.append(fp.read().decode())

    finally:
        os.dup2(saved_stderr, 2)


class TestCGDataProvider(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CGDataProviderRef)

    def test_functions(self):
        self.assertIsInstance(Quartz.CGDataProviderGetTypeID(), int)

        provider = Quartz.CGDataProviderCreateWithCFData(b"data")
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        fn = "/Library/Documentation/Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation/Airport Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"

        if not os.path.exists(fn):
            self.fail("Cannot find test file")

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, fn, Quartz.kCFURLPOSIXPathStyle, False
        )

        provider = Quartz.CGDataProviderCreateWithURL(url)
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        provider = Quartz.CGDataProviderCreateWithFilename(fn.encode("ascii"))
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        v = Quartz.CGDataProviderRetain(provider)
        self.assertTrue(v is provider)
        Quartz.CGDataProviderRelease(provider)

        data = Quartz.CGDataProviderCopyData(provider)
        self.assertIsInstance(data, Quartz.CFDataRef)

        info = [b"hello world", False]

        def release(info):
            info[-1] = True

        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            Quartz.CGDataProviderCreateWithData()

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGDataProviderCreateWithData(info, info[0], "count", release)

        with self.assertRaisesRegex(TypeError, "release not callable"):
            Quartz.CGDataProviderCreateWithData(info, info[0], len(info[0]), 42)

        provider = Quartz.CGDataProviderCreateWithData(
            info, info[0], len(info[0]), release
        )
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)
        del provider

        self.assertTrue(info[-1])

        provider = Quartz.CGDataProviderCreateWithData(
            info,
            info[0],
            len(info[0]),
            None,
        )
        self.assertIsNot(provider, None)
        del provider

        def release_raises(info):
            raise RuntimeError("release failed")

        with saved_system_stderr() as stderr:
            provider = Quartz.CGDataProviderCreateWithData(
                info, info[0], len(info[0]), release_raises
            )
            self.assertIsNot(provider, None)
            del provider

        self.assertIn(
            "PyObjC: Exception during dealloc of proxy: <class 'RuntimeError'>: release failed",
            stderr[0],
        )

    @expectedFailure
    def test_missing(self):
        self.fail("CGDataProviderCreateSequential")  # + callbacks
        self.fail("CGDataProviderCreateDirect")  # + callbacks
        self.fail("CGDataProviderCreate")  # + callbacks
        self.fail("CGDataProviderCreateDirectAccess")  # + callbacks

    @min_os_level("10.13")
    def test_functions10_13(self):
        Quartz.CGDataProviderGetInfo
