# Generated file, don't edit
# Source: BridgeSupport/SyncServices.bridgesupport
# Last update: Tue Jul 19 15:14:08 2011

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
constants = '''$ISyncAvailabilityChangedNotification$ISyncChangePropertyActionKey$ISyncChangePropertyClear$ISyncChangePropertyNameKey$ISyncChangePropertySet$ISyncChangePropertyValueKey$ISyncClientTypeApplication$ISyncClientTypeDevice$ISyncClientTypePeer$ISyncClientTypeServer$ISyncErrorDomain$ISyncInvalidEntityException$ISyncInvalidRecordException$ISyncInvalidRecordIdentifiersKey$ISyncInvalidRecordReasonsKey$ISyncInvalidRecordsKey$ISyncRecordEntityNameKey$ISyncServerUnavailableException$ISyncSessionCancelledException$ISyncSessionUnavailableException$ISyncUnsupportedEntityException$ISyncChangePropertyValueIsDefaultKey$ISyncInvalidSchemaException$ISyncInvalidArgumentsException$'''
enums = '''$ISyncServerDisabledReasonNone@1000$ISyncServerDisabledReasonByPreference@1001$ISyncServerDisabledReasonSharedNetworkHome@1002$ISyncServerDisabledReasonUnresponsive@1003$ISyncServerDisabledReasonUnknown@1004$ISyncChangeTypeNone@0$ISyncChangeTypeAdd@1$ISyncChangeTypeDelete@3$ISyncChangeTypeModify@2$ISyncSessionClientAlreadySyncingError@100$ISyncSessionDriverChangeAccepted@1$ISyncSessionDriverChangeError@3$ISyncSessionDriverChangeIgnored@2$ISyncSessionDriverChangeRefused@0$ISyncSessionDriverFatalError@300$ISyncSessionDriverModeFast@1$ISyncSessionDriverModeRefresh@3$ISyncSessionDriverModeSlow@2$ISyncSessionDriverPullFailureError@201$ISyncSessionDriverRegistrationError@200$ISyncSessionUserCanceledSessionError@101$ISyncStatusCancelled@5$ISyncStatusErrors@4$ISyncStatusFailed@6$ISyncStatusNever@7$ISyncStatusRunning@1$ISyncStatusSuccess@2$ISyncStatusWarnings@3$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('ISyncClient', b'formatsRelationships', {'retval': {'type': b'Z'}})
    r('ISyncClient', b'setFormatsRelationships:', {'arguments': {2: {'type': b'Z'}}})
    r('ISyncClient', b'canPullChangesForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncClient', b'canPushChangesForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncClient', b'isEnabledForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncClient', b'setEnabled:forEntityNames:', {'arguments': {2: {'type': b'Z'}}})
    r('ISyncClient', b'setShouldReplaceClientRecords:forEntityNames:', {'arguments': {2: {'type': b'Z'}}})
    r('ISyncClient', b'setShouldSynchronize:withClientsOfType:', {'arguments': {2: {'type': b'Z'}}})
    r('ISyncClient', b'setSyncAlertHandler:selector:', {'arguments': {3: {'sel_of_type': b'v@:@@'}}})
    r('ISyncClient', b'shouldReplaceClientRecordsForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncClient', b'shouldSynchronizeWithClientsOfType:', {'retval': {'type': b'Z'}})
    r('ISyncManager', b'clientWithIdentifier:needsSyncing:', {'arguments': {3: {'type': b'Z'}}})
    r('ISyncManager', b'isEnabled', {'retval': {'type': b'Z'}})
    r('ISyncManager', b'registerSchemaWithBundlePath:', {'retval': {'type': b'Z'}})
    r('ISyncRecordSnapshot', b'recordIdentifierForReference:isModified:', {'arguments': {3: {'type': b'^Z', 'type_modifier': b'o'}}})
    r('ISyncSession', b'beginSessionInBackgroundWithClient:entityNames:target:selector:', {'arguments': {5: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'beginSessionInBackgroundWithClient:entityNames:target:selector:lastAnchors:', {'arguments': {5: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'clientLostRecordWithIdentifier:shouldReplaceOnNextSync:', {'arguments': {3: {'type': b'Z'}}})
    r('ISyncSession', b'isCancelled', {'retval': {'type': b'Z'}})
    r('ISyncSession', b'prepareToPullChangesForEntityNames:beforeDate:', {'retval': {'type': b'Z'}})
    r('ISyncSession', b'prepareToPullChangesInBackgroundForEntityNames:target:selector:', {'arguments': {4: {'sel_of_type': b'v@:@@'}}})
    r('ISyncSession', b'shouldPullChangesForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncSession', b'shouldPushAllRecordsForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncSession', b'shouldPushChangesForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncSession', b'shouldReplaceAllRecordsOnClientForEntityName:', {'retval': {'type': b'Z'}})
    r('ISyncSessionDriver', b'handlesSyncAlerts', {'retval': {'type': b'Z'}})
    r('ISyncSessionDriver', b'setHandlesSyncAlerts:', {'arguments': {2: {'type': b'Z'}}})
    r('ISyncSessionDriver', b'startAsynchronousSync:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('ISyncSessionDriver', b'sync', {'retval': {'type': b'Z'}})
    r('NSObject', b'applyChange:forEntityName:remappedRecordIdentifier:formattedRecord:error:', {'retval': {'type': b'i'}, 'arguments': {4: {'type': b'^@', 'type_modifier': b'o'}, 5: {'type': b'^@', 'type_modifier': b'o'}, 6: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changedRecordsForEntityName:moreComing:error:', {'arguments': {3: {'type': b'^Z', 'type_modifier': b'o'}, 4: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'changesForEntityName:moreComing:error:', {'arguments': {3: {'type': b'^Z', 'type_modifier': b'o'}, 4: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'deleteAllRecordsForEntityName:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'identifiersForRecordsToDeleteForEntityName:moreComing:error:', {'arguments': {3: {'type': b'^Z', 'type_modifier': b'o'}, 4: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'isEqual:', {'retval': {'type': b'Z'}})
    r('NSObject', b'persistentStoreCoordinator:willDeleteRecordWithIdentifier:inSyncSession:', {'retval': {'type': b'Z'}})
    r('NSObject', b'persistentStoreCoordinatorShouldStartSyncing:', {'retval': {'type': b'Z'}})
    r('NSObject', b'recordsForEntityName:moreComing:error:', {'arguments': {3: {'type': b'^Z', 'type_modifier': b'o'}, 4: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willNegotiateAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didReceiveSyncAlertAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didNegotiateAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPullAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didPushAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:didRegisterClientAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'^@', 'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willFinishSessionAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPullAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSObject', b'sessionDriver:willPushAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSObject', b'shouldApplyRecord:withRecordIdentifier:', {'retval': {'type': b'Z'}})
    r('NSPersistentStoreCoordinator', b'syncWithClient:inBackground:handler:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}, 5: {'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
protocols={'ISyncSessionDriverDelegate': objc.informal_protocol('ISyncSessionDriverDelegate', [objc.selector(None, 'sessionDriver:didPullAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didPushAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:didRegisterClientAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willFinishSessionAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willPullAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriver:willPushAndReturnError:', 'Z@:@^@', isRequired=False), objc.selector(None, 'sessionDriverDidCancelSession:', 'v@:@', isRequired=False), objc.selector(None, 'sessionDriverDidFinishSession:', 'v@:@', isRequired=False), objc.selector(None, 'sessionDriverWillCancelSession:', 'v@:@', isRequired=False)]), 'ISyncSessionDriverDataSourceOptionalMethods': objc.informal_protocol('ISyncSessionDriverDataSourceOptionalMethods', [objc.selector(None, 'changedRecordsForEntityName:moreComing:error:', '@@:@^Z^@', isRequired=False), objc.selector(None, 'changesForEntityName:moreComing:error:', '@@:@^Z^@', isRequired=False), objc.selector(None, 'entityNamesToPull', '@@:', isRequired=False), objc.selector(None, 'entityNamesToSync', '@@:', isRequired=False), objc.selector(None, 'identifiersForRecordsToDeleteForEntityName:moreComing:error:', '@@:@^Z^@', isRequired=False), objc.selector(None, 'lastAnchorForEntityName:', '@@:@', isRequired=False), objc.selector(None, 'nextAnchorForEntityName:', '@@:@', isRequired=False), objc.selector(None, 'sessionBeginTimeout', 'd@:', isRequired=False), objc.selector(None, 'sessionPullChangesTimeout', 'd@:', isRequired=False)]), 'SyncUIHelperInformalProtocol': objc.informal_protocol('SyncUIHelperInformalProtocol', [objc.selector(None, 'attributedStringForIdentityPropertiesWithNames:inRecord:comparisonRecords:firstLineAttributes:secondLineAttributes:', '@@:@@@@@', isRequired=False), objc.selector(None, 'attributedStringForPropertiesWithNames:inRecord:comparisonRecords:defaultAttributes:', '@@:@@@@', isRequired=False)])}
