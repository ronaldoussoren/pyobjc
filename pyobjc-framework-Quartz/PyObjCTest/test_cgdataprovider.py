import os
import tempfile
import sys
import io
import objc

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


@contextlib.contextmanager
def saved_python_stderr():
    result = []
    saved_stderr = sys.stderr

    try:
        sys.stderr = io.StringIO()

        yield result

    finally:
        result.append(sys.stderr.getvalue())
        sys.stderr = saved_stderr


class TestCGDataProvider(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CGDataProviderRef)

    def test_functions(self):
        self.assertIsInstance(Quartz.CGDataProviderGetTypeID(), int)

        provider = Quartz.CGDataProviderCreateWithCFData(b"data")
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)

        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdoc.pdf")
        # fn = "/Library/Documentation/Acknowledgements.rtf"
        # if not os.path.exists(fn):
        # fn = "/Library/Documentation/Airport Acknowledgements.rtf"
        # if not os.path.exists(fn):
        # fn = "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"
        #
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

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Quartz.CGDataProviderCreateWithData(
                info, "hello world", len(info[0]), release
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGDataProviderCreateWithData(info, info[0], "count", release)

        with self.assertRaisesRegex(TypeError, "release not callable"):
            Quartz.CGDataProviderCreateWithData(info, info[0], len(info[0]), 42)

        provider = Quartz.CGDataProviderCreateWithData(
            info, tuple(info[0]), len(info[0]), release
        )
        self.assertIsInstance(provider, Quartz.CGDataProviderRef)
        del provider

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

    def test_manual_dataprovider_sequential(self):
        record = []

        def getBytes(info, buf, count):
            record.append(("getBytes", buf, count))
            if len(record) % 2 == 0:
                b = info.readinto(buf[:count])
                return b, buf

            else:
                buf = info.read(count)
                return len(buf), buf

        def skipForward(info, count):
            record.append(("skipForward", count))
            c = info.seek(0, os.SEEK_CUR)
            r = info.seek(count, os.SEEK_CUR)
            return r - c

        def rewind(info):
            record.append(("rewind",))
            info.seek(0)

        def release(info):
            record.append(("release",))

        with open(
            "/Library/Documentation/License.lpdf/Contents/Resources/English.lproj/License.pdf",
            "rb",
        ) as context:

            with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
                Quartz.CGDataProviderCreateSequential()

            with self.assertRaisesRegex(
                TypeError, "Callbacks should be tuple of 4 callables"
            ):
                Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, skipForward, rewind)
                )

            with self.assertRaisesRegex(TypeError, "getBytes is not callable"):
                Quartz.CGDataProviderCreateSequential(
                    context, (None, skipForward, rewind, release)
                )

            with self.assertRaisesRegex(TypeError, "skipForward is not callable"):
                Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, None, rewind, release)
                )

            with self.assertRaisesRegex(TypeError, "rewind is not callable"):
                Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, skipForward, None, release)
                )

            with self.assertRaisesRegex(TypeError, "release is not callable"):
                Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, skipForward, rewind, 42)
                )

            p = Quartz.CGDataProviderCreateSequential(
                context, (getBytes, skipForward, rewind, None)
            )
            self.assertIsInstance(p, Quartz.CGDataProviderRef)

            p = Quartz.CGDataProviderCreateSequential(
                context, (getBytes, skipForward, rewind, release)
            )
            self.assertIsInstance(p, Quartz.CGDataProviderRef)

            pdf = Quartz.CGPDFDocumentCreateWithProvider(p)
            self.assertIsNot(pdf, None)

            del p

            context.seek(0)

            def rewind_raises(info):
                rewind(info)
                raise RuntimeError("cannot rewind")

            p = Quartz.CGDataProviderCreateSequential(
                context, (getBytes, skipForward, rewind_raises, None)
            )

            with saved_python_stderr() as stderr:
                Quartz.CGPDFDocumentCreateWithProvider(p)

            if sys.version_info[:2] >= (3, 13):
                self.assertIn(
                    "Exception ignored in CGDataProvider rewind callback", stderr[0]
                )
            else:
                self.assertIn("Exception ignored in:", stderr[0])
            self.assertIn("RuntimeError: cannot rewind", stderr[0])

            context.seek(0)

            # XXX: The tests below are testing error paths that cause crashes
            #      in Quartz on macOS 27 when using Rosetta 2. That's why
            #      tests are disabled there.
            if objc.arch != "x86_64" or not objc.macos_available(27, 0):

                def skipForward_raises(info, count):
                    skipForward(info, count)
                    raise RuntimeError("cannot skip")

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, skipForward_raises, rewind, None)
                )

                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider skipForward callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                    self.assertIn("RuntimeError: cannot skip", stderr[0])

                context.seek(0)

                def skipForward_raises(info, count):
                    return "20"

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes, skipForward_raises, rewind, None)
                )
                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider skipForward callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                self.assertIn(
                    "ValueError: depythonifying 'long long', got 'str'", stderr[0]
                )

                def getBytes_raises(info, buf, count):
                    getBytes(info, buf, count)
                    raise RuntimeError("cannot read")

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes_raises, skipForward, rewind, None)
                )
                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider getBytes callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                self.assertIn("RuntimeError: cannot read", stderr[0])

                return  # XXX

                context.seek(0)

                def getBytes_raises(info, buf, count):
                    getBytes(info, buf, count)
                    return None

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes_raises, skipForward, rewind, None)
                )
                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider getBytes callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                self.assertIn(
                    "TypeError: Expecting result of type tuple of 2, got NoneType",
                    stderr[0],
                )

                context.seek(0)

                def getBytes_raises(info, buf, count):
                    getBytes(info, buf, count)
                    buf = info.read(count)
                    return str(len(buf)), buf

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes_raises, skipForward, rewind, None)
                )
                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider getBytes callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                self.assertIn(
                    "ValueError: depythonifying 'unsigned long long', got 'str'",
                    stderr[0],
                )

                context.seek(0)

                def getBytes_raises(info, buf, count):
                    buf = info.read(count)
                    return len(buf), 42

                p = Quartz.CGDataProviderCreateSequential(
                    context, (getBytes_raises, skipForward, rewind, None)
                )
                with saved_python_stderr() as stderr:
                    Quartz.CGPDFDocumentCreateWithProvider(p)

                if sys.version_info[:2] >= (3, 13):
                    self.assertIn(
                        "Exception ignored in CGDataProvider getBytes callback",
                        stderr[0],
                    )
                else:
                    self.assertIn("Exception ignored in:", stderr[0])
                    self.assertIn(
                        "TypeError: a bytes-like object is required, not 'int'",
                        stderr[0],
                    )

                    context.seek(0)

                    def getBytes_raises(info, buf, count):
                        buf = info.read(count)
                        return len(buf) * 10, buf

                    p = Quartz.CGDataProviderCreateSequential(
                        context, (getBytes_raises, skipForward, rewind, None)
                    )
                    with saved_python_stderr() as stderr:
                        Quartz.CGPDFDocumentCreateWithProvider(p)
                    if sys.version_info[:2] >= (3, 13):
                        self.assertIn(
                            "Exception ignored in CGDataProvider getBytes callback",
                            stderr[0],
                        )
                    else:
                        self.assertIn("Exception ignored in:", stderr[0])
                    self.assertIn("ValueError: Inconsistent size", stderr[0])

                    def release_raises(info):
                        raise RuntimeError("release fails")

                    p = Quartz.CGDataProviderCreateSequential(
                        context, (getBytes, skipForward, rewind, release_raises)
                    )

                    with saved_python_stderr() as stderr:
                        del p

                    if sys.version_info[:2] >= (3, 13):
                        self.assertIn(
                            "Exception ignored in CGDataProvider release callback",
                            stderr[0],
                        )
                    else:
                        self.assertIn("Exception ignored in:", stderr[0])
                    self.assertIn("RuntimeError: release fails", stderr[0])

    @expectedFailure
    def test_missing(self):
        self.fail("CGDataProviderCreateDirect")  # + callbacks

    @min_os_level("10.13")
    def test_functions10_13(self):
        Quartz.CGDataProviderGetInfo
