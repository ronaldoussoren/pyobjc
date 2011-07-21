# Generated file, don't edit
# Source: BridgeSupport/PubSub.bridgesupport
# Last update: Thu Jul 21 08:55:25 2011

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
}
constants = '''$PSEnclosureDownloadStateDidChangeNotification$PSErrorDomain$PSFeedAddedEntriesKey$PSFeedDidChangeEntryFlagsKey$PSFeedEntriesChangedNotification$PSFeedRefreshingNotification$PSFeedRemovedEntriesKey$PSFeedUpdatedEntriesKey$'''
enums = '''$PSAtomFormat@2$PSEnclosureDownloadDidFail@4$PSEnclosureDownloadDidFinish@3$PSEnclosureDownloadIsActive@2$PSEnclosureDownloadIsIdle@0$PSEnclosureDownloadIsQueued@1$PSEnclosureDownloadWasDeleted@5$PSFeedSettingsIntervalDefault@0.0$PSFeedSettingsIntervalNever@-1$PSFeedSettingsUnlimitedSize@0$PSInternalError@1$PSLinkToAlternate@7$PSLinkToAtom@2$PSLinkToAtomService@3$PSLinkToFOAF@4$PSLinkToOther@0$PSLinkToRSD@5$PSLinkToRSS@1$PSLinkToSelf@6$PSNotAFeedError@2$PSRSSFormat@1$PSUnknownFormat@0$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('PSClient', b'addFeed:', {'retval': {'type': b'Z'}})
    r('PSClient', b'removeFeed:', {'retval': {'type': b'Z'}})
    r('PSClient', b'isPrivate', {'retval': {'type': b'Z'}})
    r('PSClient', b'setPrivate:', {'arguments': {2: {'type': b'Z'}}})
    r('PSEntry', b'isRead', {'retval': {'type': b'Z'}})
    r('PSEntry', b'isFlagged', {'retval': {'type': b'Z'}})
    r('PSEntry', b'isCurrent', {'retval': {'type': b'Z'}})
    r('PSEntry', b'setCurrent:', {'arguments': {2: {'type': b'Z'}}})
    r('PSEntry', b'setFlagged:', {'arguments': {2: {'type': b'Z'}}})
    r('PSEntry', b'setRead:', {'arguments': {2: {'type': b'Z'}}})
    r('PSEnclosure', b'download:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('PSFeed', b'XMLRepresentationWithEntries:', {'arguments': {2: {'type': b'Z'}}})
    r('PSFeed', b'refresh:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('PSFeed', b'isRefreshing', {'retval': {'type': b'Z'}})
    r('PSFeedSettings', b'downloadsEnclosures', {'retval': {'type': b'Z'}})
    r('PSFeedSettings', b'refreshesInBackground', {'retval': {'type': b'Z'}})
    r('PSFeedSettings', b'setDownloadsEnclosures:', {'arguments': {2: {'type': b'Z'}}})
    r('PSFeedSettings', b'setRefreshesInBackground:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
protocols={'PSClientDelegate': objc.informal_protocol('PSClientDelegate', [objc.selector(None, 'enclosure:downloadStateDidChange:', 'v@:@i', isRequired=False), objc.selector(None, 'feed:didAddEntries:', 'v@:@@', isRequired=False), objc.selector(None, 'feed:didChangeFlagsInEntries:', 'v@:@@', isRequired=False), objc.selector(None, 'feed:didRemoveEntriesWithIdentifiers:', 'v@:@@', isRequired=False), objc.selector(None, 'feed:didUpdateEntries:', 'v@:@@', isRequired=False), objc.selector(None, 'feedDidBeginRefresh:', 'v@:@', isRequired=False), objc.selector(None, 'feedDidEndRefresh:', 'v@:@', isRequired=False)])}
misc.update({'PSFeedSettingsAllTypes': None})