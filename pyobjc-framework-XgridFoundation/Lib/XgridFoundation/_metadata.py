# Generated file, don't edit
# Source: BridgeSupport/XgridFoundation.bridgesupport
# Last update: Tue Jul 19 15:04:50 2011

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
constants = '''$XGActionMonitorResultsOutputFilesKey$XGActionMonitorResultsOutputStreamsKey$XGConnectionKeyIsClosed$XGConnectionKeyIsOpened$XGConnectionKeyState$XGControllerWillDeallocNotification$XGFileStandardErrorPath$XGFileStandardOutputPath$XGJobSpecificationARTConditionsKey$XGJobSpecificationARTDataKey$XGJobSpecificationARTEqualKey$XGJobSpecificationARTMaximumKey$XGJobSpecificationARTMinimumKey$XGJobSpecificationARTSpecificationsKey$XGJobSpecificationApplicationIdentifierKey$XGJobSpecificationArgumentTypeKey$XGJobSpecificationArgumentsKey$XGJobSpecificationCommandKey$XGJobSpecificationDependsOnJobsKey$XGJobSpecificationDependsOnTasksKey$XGJobSpecificationEnvironmentKey$XGJobSpecificationFileDataKey$XGJobSpecificationGridIdentifierKey$XGJobSpecificationInputFileMapKey$XGJobSpecificationInputFilesKey$XGJobSpecificationInputStreamKey$XGJobSpecificationIsExecutableKey$XGJobSpecificationNameKey$XGJobSpecificationNotificationEmailKey$XGJobSpecificationPathIdentifierKey$XGJobSpecificationSchedulerHintsKey$XGJobSpecificationSchedulerParametersKey$XGJobSpecificationSubmissionIdentifierKey$XGJobSpecificationTaskPrototypeIdentifierKey$XGJobSpecificationTaskPrototypesKey$XGJobSpecificationTaskSpecificationsKey$XGJobSpecificationTypeKey$XGJobSpecificationTypeTaskListValue$'''
enums = '''$XGActionMonitorOutcomeFailure@2$XGActionMonitorOutcomeNone@0$XGActionMonitorOutcomeSuccess@1$XGAuthenticatorStateAuthenticated@2$XGAuthenticatorStateAuthenticating@1$XGAuthenticatorStateFailed@3$XGAuthenticatorStateUnauthenticated@0$XGConnectionStateClosed@0$XGConnectionStateClosing@3$XGConnectionStateOpen@2$XGConnectionStateOpening@1$XGFileTypeNone@0$XGFileTypeRegular@1$XGFileTypeStream@2$XGResourceActionDelete@5$XGResourceActionGetOutputFiles@10$XGResourceActionGetOutputStreams@9$XGResourceActionGetSpecification@11$XGResourceActionMakeDefault@7$XGResourceActionNone@0$XGResourceActionRename@6$XGResourceActionRestart@2$XGResourceActionResume@4$XGResourceActionStop@1$XGResourceActionSubmitJob@8$XGResourceActionSuspend@3$XGResourceStateAvailable@4$XGResourceStateCanceled@12$XGResourceStateConnecting@2$XGResourceStateFailed@13$XGResourceStateFinished@14$XGResourceStateOffline@1$XGResourceStatePending@6$XGResourceStateRunning@9$XGResourceStateStagingIn@8$XGResourceStateStagingOut@11$XGResourceStateStarting@7$XGResourceStateSuspended@10$XGResourceStateUnavailable@3$XGResourceStateUninitialized@0$XGResourceStateWorking@5$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('XGActionMonitor', b'actionDidFail', {'retval': {'type': b'Z'}})
    r('XGActionMonitor', b'actionDidSucceed', {'retval': {'type': b'Z'}})
    r('XGConnection', b'isClosed', {'retval': {'type': b'Z'}})
    r('XGConnection', b'isOpened', {'retval': {'type': b'Z'}})
    r('XGFileDownload', b'setDestination:allowOverwrite:', {'arguments': {3: {'type': b'Z'}}})
    r('XGGrid', b'isDefault', {'retval': {'type': b'Z'}})
    r('XGResource', b'isUpdated', {'retval': {'type': b'Z'}})
    r('XGResource', b'isUpdating', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
protocols={'XGAuthenticatorDelegate': objc.informal_protocol('XGAuthenticatorDelegate', [objc.selector(None, 'authenticatorDidAuthenticate:', 'v@:@', isRequired=False), objc.selector(None, 'authenticatorDidNotAuthenticate:', 'v@:@', isRequired=False)]), 'XGFileDownloadDelegate': objc.informal_protocol('XGFileDownloadDelegate', [objc.selector(None, 'fileDownload:decideDestinationWithSuggestedPath:', 'v@:@@', isRequired=False), objc.selector(None, 'fileDownload:didCreateDestination:', 'v@:@@', isRequired=False), objc.selector(None, 'fileDownload:didFailWithError:', 'v@:@@', isRequired=False), objc.selector(None, 'fileDownload:didReceiveAttributes:', 'v@:@@', isRequired=False), objc.selector(None, 'fileDownload:didReceiveData:', 'v@:@@', isRequired=False), objc.selector(None, 'fileDownloadDidBegin:', 'v@:@', isRequired=False), objc.selector(None, 'fileDownloadDidFinish:', 'v@:@', isRequired=False)]), 'XGConnectionDelegate': objc.informal_protocol('XGConnectionDelegate', [objc.selector(None, 'connectionDidClose:', 'v@:@', isRequired=False), objc.selector(None, 'connectionDidNotOpen:withError:', 'v@:@@', isRequired=False), objc.selector(None, 'connectionDidOpen:', 'v@:@', isRequired=False)])}
