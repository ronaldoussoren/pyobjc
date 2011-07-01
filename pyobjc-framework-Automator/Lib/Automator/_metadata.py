# Generated file, don't edit
# Source: BridgeSupport/Automator.bridgesupport
# Last update: Fri Jul  1 13:58:53 2011

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
constants = '''$'''
enums = '''$AMLogLevelDebug@0$AMLogLevelInfo@1$AMLogLevelWarn@2$AMLogLevelError@3$AMActionApplicationResourceError@-206$AMActionApplicationVersionResourceError@-207$AMActionArchitectureMismatchError@-202$AMActionExceptionError@-213$AMActionExecutionError@-212$AMActionFileResourceError@-208$AMActionInitializationError@-211$AMActionInsufficientDataError@-215$AMActionIsDeprecatedError@-216$AMActionLicenseResourceError@-209$AMActionLinkError@-205$AMActionLoadError@-204$AMActionNotLoadableError@-201$AMActionPropertyListInvalidError@-214$AMActionRequiredActionResourceError@-210$AMActionRuntimeMismatchError@-203$AMConversionFailedError@-302$AMConversionNoDataError@-301$AMConversionNotPossibleError@-300$AMNoSuchActionError@-200$AMUserCanceledError@-128$AMWorkflowNewerActionVersionError@-111$AMWorkflowNewerVersionError@-100$AMWorkflowOlderActionVersionError@-112$AMWorkflowPropertyListInvalidError@-101$'''
misc.update({'AMAutomatorErrorDomain': 'com.apple.Automator', 'AMActionErrorKey': 'AMActionErrorKey'})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('AMAction', b'ignoresInput', {'retval': {'type': b'Z'}})
    r('AMAction', b'isStopped', {'retval': {'type': b'Z'}})
    r('AMAction', b'initWithContentsOfURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('AMAction', b'initWithDefinition:fromArchive:', {'arguments': {3: {'type': b'Z'}}})
    r('AMAction', b'runWithInput:fromAction:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('AMAction', b'runWithInput:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('AMAction', b'logMessageWithLevel:format:', {'arguments': {3: {'printf_format': True}}, 'variadic': 'true'})
    r('AMBundleAction', b'hasView', {'retval': {'type': b'Z'}})
    r('AMBundleAction', b'initWithDefinition:fromArchive:', {'arguments': {3: {'type': b'Z'}}})
    r('AMShellScriptAction', b'remapLineEndings', {'retval': {'type': b'Z'}})
    r('AMWorkflow', b'initWithContentsOfURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('AMWorkflow', b'runWorkflowAtURL:withInput:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('AMWorkflow', b'setValue:forVariableWithName:', {'retval': {'type': b'Z'}})
    r('AMWorkflow', b'writeToURL:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('AMWorkflowController', b'canRun', {'retval': {'type': b'Z'}})
    r('AMWorkflowController', b'isRunning', {'retval': {'type': b'Z'}})
    r('AMWorkflowController', b'isPaused', {'retval': {'type': b'Z'}})
    r('AMWorkflowView', b'isEditable', {'retval': {'type': b'Z'}})
    r('AMWorkflowView', b'setEditable:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
protocols={'AMWorkflowControllerDelegate': objc.informal_protocol('AMWorkflowControllerDelegate', [objc.selector(None, 'workflowController:didError:', 'v@:@@', isRequired=False), objc.selector(None, 'workflowController:didRunAction:', 'v@:@@', isRequired=False), objc.selector(None, 'workflowController:willRunAction:', 'v@:@@', isRequired=False), objc.selector(None, 'workflowControllerDidRun:', 'v@:@', isRequired=False), objc.selector(None, 'workflowControllerDidStop:', 'v@:@', isRequired=False), objc.selector(None, 'workflowControllerWillRun:', 'v@:@', isRequired=False), objc.selector(None, 'workflowControllerWillStop:', 'v@:@', isRequired=False)])}
