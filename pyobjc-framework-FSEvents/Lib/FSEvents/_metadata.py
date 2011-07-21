# Generated file, don't edit
# Source: BridgeSupport/FSEvents.bridgesupport
# Last update: Thu Jul 21 08:44:47 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "FSEventStreamRef": objc.createOpaquePointerType('FSEventStreamRef', b'^{__FSEventStream=}'),
    "FSEventStreamContext": objc.createStructType('FSEventStreamContext', b'{FSEventStreamContext="version"i"info"^v"retain"^?"release"^?"copyDescription"^?}', None),
}
constants = '''$'''
enums = '''$kFSEventStreamCreateFlagNoDefer@2$kFSEventStreamCreateFlagNone@0$kFSEventStreamCreateFlagUseCFTypes@1$kFSEventStreamEventFlagEventIdsWrapped@8$kFSEventStreamEventFlagHistoryDone@16$kFSEventStreamEventFlagKernelDropped@4$kFSEventStreamCreateFlagWatchRoot@4$kFSEventStreamEventFlagMustScanSubDirs@1$kFSEventStreamEventFlagNone@0$kFSEventStreamEventFlagUserDropped@2$kFSEventStreamEventIdSinceNow@-1$kFSEventStreamEventFlagRootChanged@32$kFSEventStreamEventFlagMount@64$kFSEventStreamEventFlagUnmount@128$'''
misc.update({})
functions = {'FSEventStreamGetDeviceBeingWatched': ('i^{__FSEventStream=}',), 'FSEventStreamGetLatestEventId': ('Q^{__FSEventStream=}',), 'FSEventStreamRetain': ('v^{__FSEventStream=}',), 'FSEventStreamCreateRelativeToDevice': (sel32or64('^{__FSEventStream=}^{__CFAllocator=}^?^{FSEventStreamContext=i^v^?^?^?}i^{__CFArray=}QdL', '^{__FSEventStream=}^{__CFAllocator=}^?^{FSEventStreamContext=q^v^?^?^?}i^{__CFArray=}QdL'), '', {'retval': {'already_retained': True, 'type': b'^{__FSEventStream=}'}}), 'FSEventsCopyUUIDForDevice': ('^{__CFUUID=}i', '', {'retval': {'already_retained': True, 'type': b'^{__CFUUID=}'}}), 'FSEventStreamShow': ('v^{__FSEventStream=}',), 'FSEventStreamScheduleWithRunLoop': ('v^{__FSEventStream=}^{__CFRunLoop=}^{__CFString=}',), 'FSEventStreamInvalidate': ('v^{__FSEventStream=}',), 'FSEventStreamStop': ('v^{__FSEventStream=}',), 'FSEventsPurgeEventsForDeviceUpToEventId': ('ZiQ',), 'FSEventStreamCreate': (sel32or64('^{__FSEventStream=}^{__CFAllocator=}^?^{FSEventStreamContext=i^v^?^?^?}^{__CFArray=}QdL', '^{__FSEventStream=}^{__CFAllocator=}^?^{FSEventStreamContext=q^v^?^?^?}^{__CFArray=}QdL'), '', {'retval': {'already_retained': True, 'type': b'^{__FSEventStream=}'}}), 'FSEventStreamCopyDescription': ('^{__CFString=}^{__FSEventStream=}', '', {'retval': {'already_retained': True, 'type': b'^{__CFString=}'}}), 'FSEventStreamCopyPathsBeingWatched': ('^{__CFArray=}^{__FSEventStream=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'FSEventStreamUnscheduleFromRunLoop': ('v^{__FSEventStream=}^{__CFRunLoop=}^{__CFString=}',), 'FSEventStreamRelease': ('v^{__FSEventStream=}',), 'FSEventStreamStart': ('Z^{__FSEventStream=}',), 'FSEventStreamFlushSync': ('v^{__FSEventStream=}',), 'FSEventsGetLastEventIdForDeviceBeforeTime': ('Qid',), 'FSEventStreamFlushAsync': ('q^{__FSEventStream=}',), 'FSEventsGetCurrentEventId': ('Q',)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
finally:
    objc._updatingMetadata(False)
