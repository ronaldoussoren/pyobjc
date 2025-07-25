"""
Python mapping for the CloudKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Accounts
    import CoreData
    import CoreLocation
    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CloudKit",
        frameworkIdentifier="com.apple.cloudkit.CloudKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CloudKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            CoreData,
            CoreLocation,
            Accounts,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CKDatabase", b"init"),
        ("CKDatabase", b"new"),
        ("CKNotification", b"init"),
        ("CKNotification", b"new"),
        ("CKServerChangeToken", b"init"),
        ("CKServerChangeToken", b"new"),
        ("CKQuery", b"init"),
        ("CKQuery", b"new"),
        ("CKReference", b"init"),
        ("CKReference", b"new"),
        ("CKShareParticipant", b"init"),
        ("CKShareParticipant", b"new"),
        ("CKRecordZoneID", b"init"),
        ("CKRecordZoneID", b"new"),
        ("CKSystemSharingUIObserver", b"init"),
        ("CKSystemSharingUIObserver", b"new"),
        ("CKSyncEngineState", b"init"),
        ("CKSyncEngineState", b"new"),
        ("CKSyncEngineStateSerialization", b"init"),
        ("CKSyncEngineStateSerialization", b"new"),
        ("CKSyncEnginePendingRecordZoneChange", b"init"),
        ("CKSyncEnginePendingRecordZoneChange", b"new"),
        ("CKSyncEnginePendingDatabaseChange", b"init"),
        ("CKSyncEnginePendingDatabaseChange", b"new"),
        ("CKSyncEngineConfiguration", b"init"),
        ("CKSyncEngineConfiguration", b"new"),
        ("CKSyncEngineEvent", b"init"),
        ("CKSyncEngineEvent", b"new"),
        ("CKSyncEngineFetchedRecordDeletion", b"init"),
        ("CKSyncEngineFetchedRecordDeletion", b"new"),
        ("CKSyncEngineFetchedZoneDeletion", b"init"),
        ("CKSyncEngineFetchedZoneDeletion", b"new"),
        ("CKSyncEngineFailedRecordSave", b"init"),
        ("CKSyncEngineFailedRecordSave", b"new"),
        ("CKSyncEngineFailedZoneSave", b"init"),
        ("CKSyncEngineFailedZoneSave", b"new"),
        ("CKRecordZone", b"init"),
        ("CKRecordZone", b"new"),
        ("CKRecordID", b"init"),
        ("CKRecordID", b"new"),
        ("CKShare", b"init"),
        ("CKShare", b"new"),
        ("CKShare", b"initWithRecordType:"),
        ("CKShare", b"initWithRecordType:recordID:"),
        ("CKShare", b"initWithRecordType:zoneID:"),
        ("CKLocationSortDescriptor", b"init"),
        ("CKLocationSortDescriptor", b"new"),
        ("CKQueryCursor", b"init"),
        ("CKQueryCursor", b"new"),
        ("CKSubscription", b"init"),
        ("CKSubscription", b"new"),
        ("CKRecord", b"init"),
        ("CKRecord", b"new"),
        ("CKContainer", b"init"),
        ("CKContainer", b"new"),
        ("CKAsset", b"init"),
        ("CKAsset", b"new"),
        ("CKUserIdentityLookupInfo", b"init"),
        ("CKUserIdentityLookupInfo", b"new"),
        ("CKSyncEngineRecordZoneChangeBatch", b"init"),
        ("CKSyncEngineRecordZoneChangeBatch", b"new"),
        ("CKUserIdentity", b"init"),
        ("CKUserIdentity", b"new"),
        ("CKSyncEngine", b"init"),
        ("CKSyncEngine", b"new"),
        ("CKSyncEngineFetchChangesContext", b"init"),
        ("CKSyncEngineFetchChangesContext", b"new"),
        ("CKSyncEngineSendChangesContext", b"init"),
        ("CKSyncEngineSendChangesContext", b"new"),
        ("CKShareAccessRequester", b"init"),
        ("CKShareAccessRequester", b"new"),
        ("CKShareBlockedIdentity", b"init"),
        ("CKShareBlockedIdentity", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CloudKit._metadata"]

    for clsname in (
        "CKAllowedSharingOptions",
        "CKAsset",
        "CKContainer",
        "CKDatabase",
        "CKDatabaseNotification",
        "CKDatabaseSubscription",
        "CKFetchRecordZoneChangesConfiguration",
        "CKNotification",
        "CKNotificationID",
        "CKNotificationInfo",
        "CKOperationConfiguration",
        "CKOperationGroup",
        "CKQuery",
        "CKQueryCursor",
        "CKQueryNotification",
        "CKQuerySubscription",
        "CKRecord",
        "CKRecordID",
        "CKRecordZone",
        "CKRecordZoneID",
        "CKRecordZoneNotification",
        "CKRecordZoneSubscription",
        "CKReference",
        "CKServerChangeToken",
        "CKShare",
        "CKShareMetadata",
        "CKShareParticipant",
        "CKSubscription",
        "CKSyncEngine",
        "CKSyncEngineAccountChangeEvent",
        "CKSyncEngineConfiguration",
        "CKSyncEngineDidFetchChangesEvent",
        "CKSyncEngineDidFetchRecordZoneChangesEvent",
        "CKSyncEngineDidSendChangesEvent",
        "CKSyncEngineEvent",
        "CKSyncEngineFailedRecordSave",
        "CKSyncEngineFailedZoneSave",
        "CKSyncEngineFetchChangesOptions",
        "CKSyncEngineFetchedDatabaseChangesEvent",
        "CKSyncEngineFetchedRecordDeletion",
        "CKSyncEngineFetchedRecordZoneChangesEvent",
        "CKSyncEngineFetchedZoneDeletion",
        "CKSyncEnginePendingDatabaseChange",
        "CKSyncEnginePendingRecordZoneChange",
        "CKSyncEnginePendingZoneDelete",
        "CKSyncEnginePendingZoneSave",
        "CKSyncEngineRecordZoneChangeBatch",
        "CKSyncEngineSendChangesContext",
        "CKSyncEngineSendChangesOptions",
        "CKSyncEngineSentDatabaseChangesEvent",
        "CKSyncEngineSentRecordZoneChangesEvent",
        "CKSyncEngineState",
        "CKSyncEngineStateSerialization",
        "CKSyncEngineStateUpdateEvent",
        "CKSyncEngineWillFetchChangesEvent",
        "CKSyncEngineWillFetchRecordZoneChangesEvent",
        "CKSyncEngineWillSendChangesEvent",
        "CKSystemSharingUIObserver",
        "CKUserIdentity",
        "CKUserIdentityLookupInfo",
        "CKShareAccessRequester",
        "CKShareBlockedIdentity",
    ):
        try:
            objc.lookUpClass(clsname).__final__ = True
        except objc.error:
            pass


globals().pop("_setup")()
