import os
import time

import FSEvents
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestFSEvents(TestCase):
    def testValues(self):
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

    def testFunctions(self):
        def fsevents_callback(
            streamRef, clientInfo, numEvents, eventPaths, eventMarsks, eventIDs
        ):
            pass

        context = object()

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

    def testOpaque(self):
        self.assertHasAttr(FSEvents, "FSEventStreamRef")
        self.assertIsOpaquePointer(FSEvents.FSEventStreamRef)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        # Can't test beyond this because PyObjC doesn't support dispatch_queue_t yet
        self.assertHasAttr(FSEvents, "FSEventStreamSetDispatchQueue")

    @min_os_level("10.9")
    def testFunctions10_9(self):
        self.assertResultIsBOOL(FSEvents.FSEventStreamSetExclusionPaths)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(FSEvents)
