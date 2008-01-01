'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import FSEvents

class TestFSEvents (unittest.TestCase):

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
            ('kFSEventStreamEventFlagRootChanged', 0x00000020)
            ):

            self.assert_( hasattr(FSEvents, k) , k)
            self.assert_( isinstance(getattr(FSEvents, k), (int, long)) )
            self.assertEquals( getattr(FSEvents, k), v )

        self.assert_(hasattr(FSEvents, 'kFSEventStreamEventIdSinceNow'))
        self.assert_(isinstance(FSEvents.kFSEventStreamEventIdSinceNow, (int, long)))
        self.assertEquals(FSEvents.kFSEventStreamEventIdSinceNow, -1)



    def testFunctions(self):
        self.assert_( hasattr(FSEvents, 'FSEventStreamCreateRelativeToDevice') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamCreateRelativeToDevice') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamGetLatestEventId') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamGetDeviceBeingWatched') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamCopyPathsBeingWatched') )
        self.assert_( hasattr(FSEvents, 'FSEventsGetCurrentEventId') )
        self.assert_( hasattr(FSEvents, 'FSEventsCopyUUIDForDevice') )
        self.assert_( hasattr(FSEvents, 'FSEventsGetLastEventIdForDeviceBeforeTime') )
        self.assert_( hasattr(FSEvents, 'FSEventsPurgeEventsForDeviceUpToEventId') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamRetain') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamRelease') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamScheduleWithRunLoop') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamUnscheduleFromRunLoop') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamInvalidate') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamStart') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamFlushAsync') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamFlushSync') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamStop') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamShow') )
        self.assert_( hasattr(FSEvents, 'FSEventStreamCopyDescription') )

    def testOpaque(self):
        self.assert_( hasattr(FSEvents, 'FSEventStreamRef') )



if __name__ == "__main__":
    unittest.main()

