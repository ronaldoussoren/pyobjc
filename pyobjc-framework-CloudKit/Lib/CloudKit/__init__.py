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
    ):
        try:
            objc.lookUpClass(clsname).__final__ = True
        except objc.error:
            pass


globals().pop("_setup")()
