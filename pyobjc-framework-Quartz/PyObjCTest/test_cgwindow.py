from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGWindow(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.kCGWindowIDCFNumberType, Quartz.kCFNumberSInt32Type)
        self.assertEqual(
            Quartz.kCGWindowSharingCFNumberType, Quartz.kCFNumberSInt32Type
        )
        self.assertEqual(
            Quartz.kCGWindowBackingCFNumberType, Quartz.kCFNumberSInt32Type
        )
        self.assertEqual(Quartz.kCGNullWindowID, 0)
        self.assertEqual(Quartz.kCGWindowSharingNone, 0)
        self.assertEqual(Quartz.kCGWindowSharingReadOnly, 1)
        self.assertEqual(Quartz.kCGWindowSharingReadWrite, 2)
        self.assertEqual(Quartz.kCGBackingStoreRetained, 0)
        self.assertEqual(Quartz.kCGBackingStoreNonretained, 1)
        self.assertEqual(Quartz.kCGBackingStoreBuffered, 2)

        self.assertIsInstance(Quartz.kCGWindowNumber, str)
        self.assertIsInstance(Quartz.kCGWindowStoreType, str)
        self.assertIsInstance(Quartz.kCGWindowLayer, str)
        self.assertIsInstance(Quartz.kCGWindowBounds, str)
        self.assertIsInstance(Quartz.kCGWindowSharingState, str)
        self.assertIsInstance(Quartz.kCGWindowAlpha, str)
        self.assertIsInstance(Quartz.kCGWindowOwnerPID, str)
        self.assertIsInstance(Quartz.kCGWindowMemoryUsage, str)
        self.assertIsInstance(Quartz.kCGWindowWorkspace, str)
        self.assertIsInstance(Quartz.kCGWindowOwnerName, str)
        self.assertIsInstance(Quartz.kCGWindowName, str)
        self.assertIsInstance(Quartz.kCGWindowIsOnscreen, str)
        self.assertIsInstance(Quartz.kCGWindowBackingLocationVideoMemory, str)

        self.assertEqual(Quartz.kCGWindowListOptionAll, 0)
        self.assertEqual(Quartz.kCGWindowListOptionOnScreenOnly, (1 << 0))
        self.assertEqual(Quartz.kCGWindowListOptionOnScreenAboveWindow, (1 << 1))
        self.assertEqual(Quartz.kCGWindowListOptionOnScreenBelowWindow, (1 << 2))
        self.assertEqual(Quartz.kCGWindowListOptionIncludingWindow, (1 << 3))
        self.assertEqual(Quartz.kCGWindowListExcludeDesktopElements, (1 << 4))

        self.assertEqual(Quartz.kCGWindowImageDefault, 0)
        self.assertEqual(Quartz.kCGWindowImageBoundsIgnoreFraming, (1 << 0))
        self.assertEqual(Quartz.kCGWindowImageShouldBeOpaque, (1 << 1))
        self.assertEqual(Quartz.kCGWindowImageOnlyShadows, (1 << 2))

        self.assertEqual(Quartz.kCGWindowImageDefault, 0)
        self.assertEqual(Quartz.kCGWindowImageBoundsIgnoreFraming, (1 << 0))
        self.assertEqual(Quartz.kCGWindowImageShouldBeOpaque, (1 << 1))
        self.assertEqual(Quartz.kCGWindowImageOnlyShadows, (1 << 2))
        self.assertEqual(Quartz.kCGWindowImageBestResolution, (1 << 3))
        self.assertEqual(Quartz.kCGWindowImageNominalResolution, (1 << 4))

    def test_functions(self):
        self.assertResultIsCFRetained(Quartz.CGWindowListCopyWindowInfo)
        v = Quartz.CGWindowListCopyWindowInfo(0, 0)
        self.assertIsInstance(v, Quartz.CFArrayRef)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], Quartz.CFDictionaryRef)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            Quartz.CGWindowListCreate()

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGWindowListCreate("one", 0)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGWindowListCreate(0, "one")

        v = Quartz.CGWindowListCreate(0, 0)
        self.assertIsInstance(v, tuple)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], int)

        aWindowID = v[0]
        windowArray = v

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            Quartz.CGWindowListCreateDescriptionFromArray()

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Quartz.CGWindowListCreateDescriptionFromArray(42)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGWindowListCreateDescriptionFromArray(list(v) + ["root"])

        self.assertEqual(Quartz.CGWindowListCreateDescriptionFromArray(()), ())
        self.assertEqual(
            Quartz.CGWindowListCreateDescriptionFromArray((min(v) - 1,)), ()
        )

        v = Quartz.CGWindowListCreateDescriptionFromArray(v)
        self.assertIsInstance(v, Quartz.CFArrayRef)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], Quartz.CFDictionaryRef)

        self.assertResultIsCFRetained(Quartz.CGWindowListCreateImage)
        v = Quartz.CGWindowListCreateImage(((0, 0), (100, 100)), aWindowID, 0, 0)
        if v is not None:
            # function requires specific permissions on macOS 15
            self.assertIsInstance(v, Quartz.CGImageRef)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Quartz.CGWindowListCreateImageFromArray()

        with self.assertRaisesRegex(TypeError, "epythonifying struct, got no sequence"):
            Quartz.CGWindowListCreateImageFromArray(42, windowArray, 0)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            Quartz.CGWindowListCreateImageFromArray(((0, 0), (100, 100)), 42, 0)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Quartz.CGWindowListCreateImageFromArray(((0, 0), (100, 100)), (), "none")

        v = Quartz.CGWindowListCreateImageFromArray(
            ((0, 0), (100, 100)), windowArray, 0
        )
        self.assertIsInstance(v, (Quartz.CGImageRef, type(None)))

    @min_os_level("11.0")
    def test_functions10_15(self):
        Quartz.CGPreflightScreenCaptureAccess
        Quartz.CGRequestScreenCaptureAccess
