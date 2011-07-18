# Generated file, don't edit
# Source: BridgeSupport/CoreData.bridgesupport
# Last update: Mon Jul 18 19:22:14 2011

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
constants = '''$NSPersistentStoreCoordinatorWillRemoveStoreNotification$NSManagedObjectContextWillSaveNotification$NSSQLiteAnalyzeOption$NSSQLiteManualVacuumOption$NSInferMappingModelAutomaticallyOption$NSXMLExternalRecordType$NSBinaryExternalRecordType$NSExternalRecordsFileFormatOption$NSExternalRecordsDirectoryOption$NSExternalRecordExtensionOption$NSEntityNameInPathKey$NSStoreUUIDInPathKey$NSStorePathKey$NSModelPathKey$NSObjectURIKey$NSAddedPersistentStoresKey$NSAffectedObjectsErrorKey$NSAffectedStoresErrorKey$NSBinaryStoreType$NSCoreDataVersionNumber@d$NSDeletedObjectsKey$NSDetailedErrorsKey$NSErrorMergePolicy$NSIgnorePersistentStoreVersioningOption$NSInMemoryStoreType$NSInsertedObjectsKey$NSInvalidatedAllObjectsKey$NSInvalidatedObjectsKey$NSManagedObjectContextDidSaveNotification$NSManagedObjectContextObjectsDidChangeNotification$NSMergeByPropertyObjectTrumpMergePolicy$NSMergeByPropertyStoreTrumpMergePolicy$NSMigratePersistentStoresAutomaticallyOption$NSMigrationDestinationObjectKey$NSMigrationEntityMappingKey$NSMigrationManagerKey$NSMigrationPropertyMappingKey$NSMigrationSourceObjectKey$NSOverwriteMergePolicy$NSPersistentStoreCoordinatorStoresDidChangeNotification$NSPersistentStoreOSCompatibility$NSPersistentStoreTimeoutOption$NSReadOnlyPersistentStoreOption$NSRefreshedObjectsKey$NSRemovedPersistentStoresKey$NSRollbackMergePolicy$NSSQLiteErrorDomain$NSSQLitePragmasOption$NSSQLiteStoreType$NSStoreModelVersionHashesKey$NSStoreModelVersionIdentifiersKey$NSStoreTypeKey$NSStoreUUIDKey$NSUUIDChangedPersistentStoresKey$NSUpdatedObjectsKey$NSValidateXMLStoreOption$NSValidationKeyErrorKey$NSValidationObjectErrorKey$NSValidationPredicateErrorKey$NSValidationValueErrorKey$NSXMLStoreType$'''
enums = '''$NSDictionaryResultType@2$NSAddEntityMappingType@2$NSBinaryDataAttributeType@1000$NSBooleanAttributeType@800$NSCascadeDeleteRule@2$NSCopyEntityMappingType@4$NSCoreDataError@134060$NSCoreDataVersionNumber10_4@46.0$NSCoreDataVersionNumber10_4_3@77.0$NSCoreDataVersionNumber10_5@185.0$NSCoreDataVersionNumber10_5_3@186.0$NSInferredMappingModelError@134190$NSExternalRecordImportError@134200$NSCustomEntityMappingType@1$NSDateAttributeType@900$NSDecimalAttributeType@400$NSDenyDeleteRule@3$NSDoubleAttributeType@500$NSEntityMigrationPolicyError@134170$NSFetchRequestExpressionType@50$NSFloatAttributeType@600$NSInteger16AttributeType@100$NSInteger32AttributeType@200$NSInteger64AttributeType@300$NSManagedObjectContextLockingError@132000$NSManagedObjectExternalRelationshipError@133010$NSManagedObjectIDResultType@1$NSManagedObjectMergeError@133020$NSManagedObjectReferentialIntegrityError@133000$NSManagedObjectResultType@0$NSManagedObjectValidationError@1550$NSMigrationCancelledError@134120$NSMigrationError@134110$NSMigrationManagerDestinationStoreError@134160$NSMigrationManagerSourceStoreError@134150$NSMigrationMissingMappingModelError@134140$NSMigrationMissingSourceModelError@134130$NSNoActionDeleteRule@0$NSNullifyDeleteRule@1$NSPersistentStoreCoordinatorLockingError@132010$NSPersistentStoreIncompatibleSchemaError@134020$NSPersistentStoreIncompatibleVersionHashError@134100$NSPersistentStoreIncompleteSaveError@134040$NSPersistentStoreInvalidTypeError@134000$NSPersistentStoreOpenError@134080$NSPersistentStoreOperationError@134070$NSPersistentStoreSaveError@134030$NSPersistentStoreTimeoutError@134090$NSPersistentStoreTypeMismatchError@134010$NSRemoveEntityMappingType@3$NSSQLiteError@134180$NSStringAttributeType@700$NSTransformEntityMappingType@5$NSTransformableAttributeType@1800$NSObjectIDAttributeType@2000$NSUndefinedAttributeType@0$NSUndefinedEntityMappingType@0$NSValidationDateTooLateError@1630$NSValidationDateTooSoonError@1640$NSValidationInvalidDateError@1650$NSValidationMissingMandatoryPropertyError@1570$NSValidationMultipleErrorsError@1560$NSValidationNumberTooLargeError@1610$NSValidationNumberTooSmallError@1620$NSValidationRelationshipDeniedDeleteError@1600$NSValidationRelationshipExceedsMaximumCountError@1590$NSValidationRelationshipLacksMinimumCountError@1580$NSValidationStringPatternMatchingError@1680$NSValidationStringTooLongError@1660$NSValidationStringTooShortError@1670$NSSnapshotEventUndoInsertion@2$NSSnapshotEventUndoDeletion@4$NSSnapshotEventUndoUpdate@8$NSSnapshotEventRollback@16$NSSnapshotEventRefresh@32$NSSnapshotEventMergePolicy@64$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSAtomicStore', b'load:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSAtomicStore', b'save:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSEntityDescription', b'isAbstract', {'retval': {'type': b'Z'}})
    r('NSEntityDescription', b'isKindOfEntity:', {'retval': {'type': b'Z'}})
    r('NSEntityDescription', b'setAbstract:', {'arguments': {2: {'type': b'Z'}}})
    r('NSEntityMigrationPolicy', b'beginEntityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'createDestinationInstancesForSourceInstance:entityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'createRelationshipsForDestinationInstance:entityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endEntityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endInstanceCreationForEntityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endRelationshipCreationForEntityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'performCustomValidationForEntityMapping:manager:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSFetchRequest', b'includesPendingChanges', {'retval': {'type': b'Z'}})
    r('NSFetchRequest', b'setIncludesPendingChanges:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequest', b'returnsDistinctResults', {'retval': {'type': b'Z'}})
    r('NSFetchRequest', b'setReturnsDistinctResults:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequest', b'includesPropertyValues', {'retval': {'type': b'Z'}})
    r('NSFetchRequest', b'includesSubentities', {'retval': {'type': b'Z'}})
    r('NSFetchRequest', b'returnsObjectsAsFaults', {'retval': {'type': b'Z'}})
    r('NSFetchRequest', b'setIncludesPropertyValues:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequest', b'setIncludesSubentities:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequest', b'setReturnsObjectsAsFaults:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequestExpression', b'expressionForFetch:context:countOnly:', {'arguments': {4: {'type': b'Z'}}})
    r('NSFetchRequestExpression', b'isCountOnlyRequest', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'contextShouldIgnoreUnmodeledPropertyChanges', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'hasFaultForRelationshipNamed:', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'isDeleted', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'isFault', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'isInserted', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'isUpdated', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'observationInfo', {'retval': {'type': b'^v'}})
    r('NSManagedObject', b'setObservationInfo:', {'arguments': {2: {'type': b'^v'}}})
    r('NSManagedObject', b'validateForDelete:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateForInsert:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateForUpdate:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateValue:forKey:error:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'N'}, 4: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'existingObjectWithID:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'countForFetchRequest:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'executeFetchRequest:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'hasChanges', {'retval': {'type': b'Z'}})
    r('NSManagedObjectContext', b'observeValueForKeyPath:ofObject:change:context:', {'arguments': {5: {'type': b'^v'}}})
    r('NSManagedObjectContext', b'obtainPermanentIDsForObjects:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'propagatesDeletesAtEndOfEvent', {'retval': {'type': b'Z'}})
    r('NSManagedObjectContext', b'refreshObject:mergeChanges:', {'arguments': {3: {'type': b'Z'}}})
    r('NSManagedObjectContext', b'retainsRegisteredObjects', {'retval': {'type': b'Z'}})
    r('NSManagedObjectContext', b'save:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'setPropagatesDeletesAtEndOfEvent:', {'arguments': {2: {'type': b'Z'}}})
    r('NSManagedObjectContext', b'setRetainsRegisteredObjects:', {'arguments': {2: {'type': b'Z'}}})
    r('NSManagedObjectContext', b'tryLock', {'retval': {'type': b'Z'}})
    r('NSManagedObjectID', b'isTemporaryID', {'retval': {'type': b'Z'}})
    r('NSManagedObjectModel', b'isConfiguration:compatibleWithStoreMetadata:', {'retval': {'type': b'Z'}})
    r('NSMigrationManager', b'migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:', {'retval': {'type': b'Z'}, 'arguments': {9: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'loadMetadata', {'retval': {'type': b'Z'}})
    r('NSPersistentStore', b'loadMetadata:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'isReadOnly', {'retval': {'type': b'Z'}})
    r('NSPersistentStore', b'metadataForPersistentStoreWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'setMetadata:forPersistentStoreWithURL:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'setReadOnly:', {'arguments': {2: {'type': b'Z'}}})
    r('NSPersistentStoreCoordinator', b'addPersistentStoreWithType:configuration:URL:options:error:', {'arguments': {6: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'metadataForPersistentStoreOfType:URL:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'metadataForPersistentStoreWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'migratePersistentStore:toURL:options:withType:error:', {'arguments': {6: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'removePersistentStore:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'setMetadata:forPersistentStoreOfType:URL:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'setURL:forPersistentStore:', {'retval': {'type': b'Z'}})
    r('NSPersistentStoreCoordinator', b'tryLock', {'retval': {'type': b'Z'}})
    r('NSPersistentStoreCoordinator', b'importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:', {'arguments': {7: {'type_modifier': b'o'}}})
    r('NSPropertyDescription', b'isIndexed', {'retval': {'type': b'Z'}})
    r('NSPropertyDescription', b'isOptional', {'retval': {'type': b'Z'}})
    r('NSPropertyDescription', b'isTransient', {'retval': {'type': b'Z'}})
    r('NSPropertyDescription', b'setIndexed:', {'arguments': {2: {'type': b'Z'}}})
    r('NSPropertyDescription', b'setOptional:', {'arguments': {2: {'type': b'Z'}}})
    r('NSPropertyDescription', b'setTransient:', {'arguments': {2: {'type': b'Z'}}})
    r('NSPropertyDescription', b'isIndexedBySpotlight', {'retval': {'type': b'Z'}})
    r('NSPropertyDescription', b'setIndexedBySpotlight:', {'arguments': {2: {'type': b'Z'}}})
    r('NSPropertyDescription', b'isStoredInExternalRecord', {'retval': {'type': b'Z'}})
    r('NSPropertyDescription', b'setStoredInExternalRecord:', {'arguments': {2: {'type': b'Z'}}})
    r('NSRelationshipDescription', b'isToMany', {'retval': {'type': b'Z'}})
    r('NSMappingModel', b'inferredMappingModelForSourceModel:destinationModel:error:', {'arguments': {4: {'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
