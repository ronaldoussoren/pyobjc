import os
import tempfile
import time

import FSEvents
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, NoObjCClass


class TestFSEvents(TestCase):
    def test_values(self):
        for k, v in (
            ("kFSEventStreamCreateFlagNone", 0x00000000),
            ("kFSEventStreamCreateFlagUseCFTypes", 0x00000001),
            ("kFSEventStreamCreateFlagNoDefer", 0x00000002),
            ("kFSEventStreamCreateFlagWatchRoot", 0x00000004),
            ("kFSEventStreamEventFlagNone", 0x00000000),
            ("kFSEventStreamEventFlagMustScanSubDirs", 0x00000001),
            ("kFSEventStreamEventFlagUserDropped", 0x00000002),
            ("kFSEventStreamEventFlagKernelDropped", 0x00000004),
            ("kFSEventStreamEventFlagEventIdsWrapped", 0x00000008),
            ("kFSEventStreamEventFlagHistoryDone", 0x00000010),
            ("kFSEventStreamEventFlagRootChanged", 0x00000020),
            ("kFSEventStreamEventFlagMount", 0x00000040),
            ("kFSEventStreamEventFlagUnmount", 0x00000080),
            ("kFSEventStreamCreateFlagIgnoreSelf", 0x00000008),
            ("kFSEventStreamCreateFlagFileEvents", 0x00000010),
            ("kFSEventStreamCreateFlagMarkSelf", 0x00000020),
            ("kFSEventStreamCreateFlagUseExtendedData", 0x00000040),
            ("kFSEventStreamEventFlagItemCreated", 0x00000100),
            ("kFSEventStreamEventFlagItemRemoved", 0x00000200),
            ("kFSEventStreamEventFlagItemInodeMetaMod", 0x00000400),
            ("kFSEventStreamEventFlagItemRenamed", 0x00000800),
            ("kFSEventStreamEventFlagItemModified", 0x00001000),
            ("kFSEventStreamEventFlagItemFinderInfoMod", 0x00002000),
            ("kFSEventStreamEventFlagItemChangeOwner", 0x00004000),
            ("kFSEventStreamEventFlagItemXattrMod", 0x00008000),
            ("kFSEventStreamEventFlagItemIsFile", 0x00010000),
            ("kFSEventStreamEventFlagItemIsDir", 0x00020000),
            ("kFSEventStreamEventFlagItemIsSymlink", 0x00040000),
            ("kFSEventStreamEventFlagOwnEvent", 0x00080000),
            ("kFSEventStreamEventFlagItemIsHardlink", 0x00100000),
            ("kFSEventStreamEventFlagItemIsLastHardlink", 0x00200000),
            ("kFSEventStreamEventFlagItemCloned", 0x00400000),
            ("kFSEventStreamCreateFlagFullHistory", 0x00000080),
            ("kFSEventStreamCreateWithDocID", 0x00000100),
            ("kFSEventStreamCreateDeviceState", 0x00000200),
        ):
            with self.subTest(k):
                self.assertHasAttr(FSEvents, k)
                self.assertIsInstance(getattr(FSEvents, k), int)
                self.assertEqual(getattr(FSEvents, k), v)

        self.assertHasAttr(FSEvents, "kFSEventStreamEventIdSinceNow")
        self.assertIsInstance(FSEvents.kFSEventStreamEventIdSinceNow, int)
        self.assertEqual(
            FSEvents.kFSEventStreamEventIdSinceNow, 18_446_744_073_709_551_615
        )

        self.assertEqual(FSEvents.kFSEventStreamEventExtendedDataPathKey, "path")
        self.assertIsInstance(FSEvents.kFSEventStreamEventExtendedDataPathKey, str)

        self.assertEqual(FSEvents.kFSEventStreamEventExtendedFileIDKey, "fileID")
        self.assertIsInstance(FSEvents.kFSEventStreamEventExtendedFileIDKey, str)

        self.assertEqual(FSEvents.kFSEventStreamEventExtendedDocIDKey, "docID")
        self.assertIsInstance(FSEvents.kFSEventStreamEventExtendedDocIDKey, str)

    def test_functions(self):
        def fsevents_callback(
            streamRef, clientInfo, numEvents, eventPaths, eventMarsks, eventIDs
        ):
            pass

        context = object()

        with self.assertRaisesRegex(TypeError, "expected 7 arguments, got 0"):
            FSEvents.FSEventStreamCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            FSEvents.FSEventStreamCreate(
                NoObjCClass(),
                fsevents_callback,
                context,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            FSEvents.FSEventStreamCreate(
                None,
                fsevents_callback,
                context,
                NoObjCClass(),
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            FSEvents.FSEventStreamCreate(
                None,
                fsevents_callback,
                context,
                ["/etc", "/tmp"],
                "FSEvents.kFSEventStreamEventIdSinceNow",
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            FSEvents.FSEventStreamCreate(
                None,
                fsevents_callback,
                context,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                "2.0",
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            FSEvents.FSEventStreamCreate(
                None,
                fsevents_callback,
                context,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                "FSEvents.kFSEventStreamCreateFlagUseCFTypes",
            )

        self.assertIs(
            FSEvents.FSEventStreamCreate(
                None,
                fsevents_callback,
                context,
                [],
                FSEvents.kFSEventStreamEventIdSinceNow,
                1.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            ),
            None,
        )

        ref = FSEvents.FSEventStreamCreate(
            None,
            fsevents_callback,
            context,
            ["/etc", "/tmp"],
            FSEvents.kFSEventStreamEventIdSinceNow,
            2.0,
            FSEvents.kFSEventStreamCreateFlagUseCFTypes
            | FSEvents.kFSEventStreamCreateFlagNoDefer,
        )

        self.assertIsInstance(ref, FSEvents.FSEventStreamRef)
        FSEvents.FSEventStreamRelease(ref)
        ref = None

        with self.assertRaisesRegex(TypeError, "expected 8 arguments, got 0"):
            FSEvents.FSEventStreamCreateRelativeToDevice()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                NoObjCClass(),
                fsevents_callback,
                context,
                os.stat("/").st_dev,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                "dev",
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                os.stat("/").st_dev,
                NoObjCClass(),
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                os.stat("/").st_dev,
                ["/etc", "/tmp"],
                "FSEvents.kFSEventStreamEventIdSinceNow",
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                os.stat("/").st_dev,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                "2.0",
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                os.stat("/").st_dev,
                ["/etc", "/tmp"],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                "FSEvents.kFSEventStreamCreateFlagUseCFTypes",
            )

        self.assertIs(
            FSEvents.FSEventStreamCreateRelativeToDevice(
                None,
                fsevents_callback,
                context,
                -1,
                [os.path.realpath("/etc"), os.path.realpath("/tmp")],
                FSEvents.kFSEventStreamEventIdSinceNow,
                2.0,
                FSEvents.kFSEventStreamCreateFlagUseCFTypes
                | FSEvents.kFSEventStreamCreateFlagNoDefer,
            ),
            None,
        )

        ref = FSEvents.FSEventStreamCreateRelativeToDevice(
            None,
            fsevents_callback,
            context,
            os.stat("/").st_dev,
            [os.path.realpath("/etc"), os.path.realpath("/tmp")],
            FSEvents.kFSEventStreamEventIdSinceNow,
            2.0,
            FSEvents.kFSEventStreamCreateFlagUseCFTypes
            | FSEvents.kFSEventStreamCreateFlagNoDefer,
        )
        self.assertIsInstance(ref, FSEvents.FSEventStreamRef)
        try:
            v = FSEvents.FSEventStreamGetLatestEventId(ref)
            self.assertIsInstance(v, int)

            v = FSEvents.FSEventStreamGetDeviceBeingWatched(ref)
            self.assertIsInstance(v, int)

            self.assertResultIsCFRetained(FSEvents.FSEventStreamCopyPathsBeingWatched)
            v = FSEvents.FSEventStreamCopyPathsBeingWatched(ref)
            self.assertIsInstance(v, FSEvents.CFArrayRef)
            self.assertEqual(len(v), 2)

            self.assertIn(
                v,
                [
                    [os.path.realpath("/etc")[1:], os.path.realpath("/tmp")[1:]],
                    [os.path.realpath("/etc"), os.path.realpath("/tmp")],
                ],
            )

            v = FSEvents.FSEventsGetCurrentEventId()
            self.assertIsInstance(v, int)

            v = FSEvents.FSEventsCopyUUIDForDevice(os.stat("/").st_dev)
            self.assertIsInstance(v, FSEvents.CFUUIDRef)

            v = FSEvents.FSEventsGetLastEventIdForDeviceBeforeTime(
                os.stat("/").st_dev, time.time() - (3600 * 25)
            )
            self.assertIsInstance(v, int)

            # Calling this function can affect the actual device (when running
            # the tests as root), therefore test against /dev which is a virtual
            # filesystem on OSX
            self.assertResultIsBOOL(FSEvents.FSEventsPurgeEventsForDeviceUpToEventId)

            if 0:
                # Stop calling this API as this can affect system state and
                # /dev is not always a virtual file system.
                v = FSEvents.FSEventsPurgeEventsForDeviceUpToEventId(
                    os.stat("/dev").st_dev,
                    FSEvents.FSEventsGetLastEventIdForDeviceBeforeTime(
                        os.stat("/dev").st_dev, 0
                    ),
                )
                self.assertIsInstance(v, bool)

            FSEvents.FSEventStreamRetain(ref)
            FSEvents.FSEventStreamRelease(ref)

            rl = FSEvents.CFRunLoopGetCurrent()
            FSEvents.FSEventStreamScheduleWithRunLoop(
                ref, rl, FSEvents.kCFRunLoopDefaultMode
            )

            self.assertResultIsBOOL(FSEvents.FSEventStreamStart)
            FSEvents.FSEventStreamStart(ref)

            v = FSEvents.FSEventStreamFlushAsync(ref)
            self.assertIsInstance(v, int)

            FSEvents.FSEventStreamFlushSync(ref)
            FSEvents.FSEventStreamStop(ref)

            FSEvents.FSEventStreamUnscheduleFromRunLoop(
                ref, rl, FSEvents.FSEventStreamUnscheduleFromRunLoop
            )

            fd = os.dup(2)
            fd2 = os.open("/dev/null", os.O_WRONLY)
            os.dup2(fd2, 2)
            os.close(fd2)
            try:
                FSEvents.FSEventStreamShow(ref)

            finally:
                os.dup2(fd, 2)

            v = FSEvents.FSEventStreamCopyDescription(ref)
            self.assertIsInstance(v, str)

            FSEvents.FSEventStreamInvalidate(ref)

        finally:
            FSEvents.FSEventStreamRelease(ref)
            ref = None

        # Can't test beyond this because PyObjC doesn't support dispatch_queue_t yet
        self.assertHasAttr(FSEvents, "FSEventStreamSetDispatchQueue")

        self.assertResultIsBOOL(FSEvents.FSEventStreamSetExclusionPaths)

    def test_loop_integration(self):
        lst = []
        for base_flags in (0, FSEvents.kFSEventStreamCreateFlagUseCFTypes):
            with self.subTest(base_flags=base_flags):
                context = object()
                lst[:] = []
                rl = CoreFoundation.CFRunLoopGetCurrent()

                def fsevents_callback(
                    ref, info, numEvents, eventPaths, eventFlags, eventIds
                ):
                    lst.append(  # noqa: B023
                        (ref, info, numEvents, eventPaths, eventFlags, eventIds)
                    )

                ref = FSEvents.FSEventStreamCreate(
                    None,
                    fsevents_callback,
                    context,
                    [os.getcwd()],
                    FSEvents.kFSEventStreamEventIdSinceNow,
                    0.5,
                    base_flags | FSEvents.kFSEventStreamCreateFlagNoDefer,
                )
                self.assertIsNot(ref, None)

                FSEvents.FSEventStreamScheduleWithRunLoop(
                    ref, rl, CoreFoundation.kCFRunLoopDefaultMode
                )
                self.assertIs(FSEvents.FSEventStreamStart(ref), True)
                with tempfile.NamedTemporaryFile(dir=os.getcwd()):
                    with tempfile.NamedTemporaryFile(dir=os.getcwd()):
                        try:
                            CoreFoundation.CFRunLoopRunInMode(
                                CoreFoundation.kCFRunLoopDefaultMode, 0.5, False
                            )

                            saved_lst = lst
                            del lst
                            with tempfile.NamedTemporaryFile(dir=os.getcwd()):
                                with self.assertRaisesRegex(
                                    NameError, "cannot access free variable 'lst'"
                                ):
                                    CoreFoundation.CFRunLoopRunInMode(
                                        CoreFoundation.kCFRunLoopDefaultMode, 1.0, False
                                    )
                            lst = saved_lst

                        finally:
                            FSEvents.FSEventStreamStop(ref)
                            FSEvents.FSEventStreamUnscheduleFromRunLoop(
                                ref, rl, CoreFoundation.kCFRunLoopDefaultMode
                            )

                self.assertEqual(len(lst), 1)
                for item in lst:
                    # Note:  FSEventStreamRef is not a CF type
                    # self.assertIs(item[0], ref)
                    self.assertEqual(item[0].__pointer__, ref.__pointer__)
                    self.assertEqual(item[1], context)
                    self.assertIsInstance(item[2], int)
                    self.assertEqual(len(item[3]), item[2])
                    self.assertTrue(
                        all(
                            isinstance(n, str if base_flags else bytes) for n in item[3]
                        )
                    )
                    self.assertEqual(len(item[4]), item[2])
                    self.assertTrue(all(isinstance(n, int) for n in item[4]))
                    self.assertEqual(len(item[5]), item[2])
                    self.assertTrue(all(isinstance(n, int) for n in item[5]))

    def test_opaque(self):
        self.assertHasAttr(FSEvents, "FSEventStreamRef")
        self.assertIsOpaquePointer(FSEvents.FSEventStreamRef)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(FSEvents)
