'''
Some simple tests to check that the framework is properly wrapped.
'''
import FSEvents
from FSEvents import *
from PyObjCTools.TestSupport import *
import os, time

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestFSEvents (TestCase):

    def testValues(self):
        for k, v in (('kFSEventStreamCreateFlagNone', 0x00000000),
            ('kFSEventStreamCreateFlagUseCFTypes', 0x00000001),
            ('kFSEventStreamCreateFlagNoDefer', 0x00000002),
            ('kFSEventStreamCreateFlagWatchRoot', 0x00000004),
            ('kFSEventStreamEventFlagNone', 0x00000000),
            ('kFSEventStreamEventFlagMustScanSubDirs', 0x00000001),
            ('kFSEventStreamEventFlagUserDropped', 0x00000002),
            ('kFSEventStreamEventFlagKernelDropped', 0x00000004),
            ('kFSEventStreamEventFlagEventIdsWrapped', 0x00000008),
            ('kFSEventStreamEventFlagHistoryDone', 0x00000010),
            ('kFSEventStreamEventFlagRootChanged', 0x00000020),
            ('kFSEventStreamEventFlagMount', 0x00000040),
            ('kFSEventStreamEventFlagUnmount', 0x00000080),
            ):

            self.assertHasAttr(FSEvents, k)
            self.assertIsInstance(getattr(FSEvents, k), (int, long))
            self.assertEquals( getattr(FSEvents, k), v )

        self.assertHasAttr(FSEvents, 'kFSEventStreamEventIdSinceNow')
        self.assertIsInstance(FSEvents.kFSEventStreamEventIdSinceNow, (int, long))
        self.assertEquals(FSEvents.kFSEventStreamEventIdSinceNow, 18446744073709551615)



    def testFunctions(self):
        def fsevents_callback(streamRef, clientInfo, numEvents, eventPaths, eventMarsks, eventIDs):
            pass
        context = object()

        ref = FSEventStreamCreate(None, fsevents_callback, context,
                ["/etc", "/tmp"], kFSEventStreamEventIdSinceNow, 2.0,  kFSEventStreamCreateFlagUseCFTypes|kFSEventStreamCreateFlagNoDefer)

        self.assertIsInstance(ref, FSEventStreamRef)
        FSEventStreamRelease(ref); ref = None

        ref = FSEventStreamCreateRelativeToDevice(
                None, fsevents_callback, context,
                os.stat('/').st_dev, [os.path.realpath("/etc"), os.path.realpath("/tmp")], kFSEventStreamEventIdSinceNow, 2.0,  kFSEventStreamCreateFlagUseCFTypes|kFSEventStreamCreateFlagNoDefer)
        self.assertIsInstance(ref, FSEventStreamRef)
        try:
            v = FSEventStreamGetLatestEventId(ref)
            self.assertIsInstance(v, (int, long))

            v = FSEventStreamGetDeviceBeingWatched(ref)
            self.assertIsInstance(v, (int, long))

            self.assertResultIsCFRetained(FSEventStreamCopyPathsBeingWatched)
            v = FSEventStreamCopyPathsBeingWatched(ref)
            self.assertIsInstance(v, CFArrayRef)
            self.assertEqual(len(v), 2)

            self.assertIn(v, [
                    [os.path.realpath("/etc")[1:], os.path.realpath("/tmp")[1:]],
                    [os.path.realpath("/etc"), os.path.realpath("/tmp")],
                ])

            v = FSEventsGetCurrentEventId()
            self.assertIsInstance(v, (int, long))

            v = FSEventsCopyUUIDForDevice(os.stat('/').st_dev)
            self.assertIsInstance(v, CFUUIDRef)

            v = FSEventsGetLastEventIdForDeviceBeforeTime(os.stat('/').st_dev, time.time()-(3600*25))
            self.assertIsInstance(v, (int, long))

            # Calling this function can affect the actual device (when running
            # the tests as root), therefore test against /dev which is a virtual
            # filesystem on OSX
            self.assertResultIsBOOL(FSEventsPurgeEventsForDeviceUpToEventId)
            v = FSEventsPurgeEventsForDeviceUpToEventId(os.stat('/dev').st_dev,
                    FSEventsGetLastEventIdForDeviceBeforeTime(os.stat('/dev').st_dev, 0))
            self.assertIsInstance(v, bool)

            FSEventStreamRetain(ref)
            FSEventStreamRelease(ref)

            rl = CFRunLoopGetCurrent()
            FSEventStreamScheduleWithRunLoop(ref, rl, kCFRunLoopDefaultMode)


            self.assertResultIsBOOL(FSEventStreamStart)
            FSEventStreamStart(ref)

            v = FSEventStreamFlushAsync(ref)
            self.assertIsInstance(v, (int, long))

            FSEventStreamFlushSync(ref)
            FSEventStreamStop(ref)

            FSEventStreamUnscheduleFromRunLoop(ref, rl, FSEventStreamUnscheduleFromRunLoop)

            fd = os.dup(2)
            fd2 = os.open('/dev/null', os.O_WRONLY)
            os.dup2(fd2, 2)
            os.close(fd2)
            try:
                FSEventStreamShow(ref)

            finally:
                os.dup2(fd, 2)

            v = FSEventStreamCopyDescription(ref)
            self.assertIsInstance(v, unicode)

            FSEventStreamInvalidate(ref)

        finally:
            FSEventStreamRelease(ref); ref = None


    def testOpaque(self):
        self.assertHasAttr(FSEvents, 'FSEventStreamRef')
        self.assertIsOpaquePointer(FSEventStreamRef)


if __name__ == "__main__":
    main()
