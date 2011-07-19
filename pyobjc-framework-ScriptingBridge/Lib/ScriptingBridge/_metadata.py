# Generated file, don't edit
# Source: BridgeSupport/ScriptingBridge.bridgesupport
# Last update: Tue Jul 19 15:18:58 2011

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
enums = '''$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSObject', b'eventDidFail:withError:', {'arguments': {2: {'type': b'r^{AEDesc=I^^{OpaqueAEDataStorageType}}'}}})
    r('SBApplication', b'isRunning', {'retval': {'type': b'Z'}})
    r('SBElementArray', b'arrayByApplyingSelector:', {'arguments': {2: {'sel_of_type': b'@@:'}}})
    r('SBElementArray', b'arrayByApplyingSelector:withObject:', {'arguments': {2: {'sel_of_type': b'@@:@'}}})
    r('SBObject', b'sendEvent:id:parameters:', {'variadic': 'true'})
finally:
    objc._updatingMetadata(False)
protocols={'SBApplicationDelegate': objc.informal_protocol('SBApplicationDelegate', [objc.selector(None, 'eventDidFail:withError:', '@@:^{AEDesc=I^^{OpaqueAEDataStorageType}}@', isRequired=False)])}
