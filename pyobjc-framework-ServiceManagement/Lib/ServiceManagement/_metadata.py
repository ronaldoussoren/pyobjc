# Generated file, don't edit
# Source: BridgeSupport/ServiceManagement.bridgesupport
# Last update: Tue Jul 19 15:17:28 2011

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
constants = '''$kSMDomainSystemLaunchd@^{__CFString=}$kSMDomainUserLaunchd@^{__CFString=}$kSMErrorDomainFramework@^{__CFString=}$kSMErrorDomainIPC@^{__CFString=}$kSMErrorDomainLaunchd@^{__CFString=}$kSMInfoKeyAuthorizedClients@^{__CFString=}$kSMInfoKeyPrivilegedExecutables@^{__CFString=}$'''
enums = '''$kSMErrorAuthorizationFailure@4$kSMErrorInternalFailure@2$kSMErrorInvalidSignature@3$kSMErrorJobMustBeEnabled@9$kSMErrorJobNotFound@6$kSMErrorJobPlistNotFound@8$kSMErrorServiceUnavailable@7$kSMErrorToolNotValid@5$'''
misc.update({'kSMRightModifySystemDaemons': 'com.apple.ServiceManagement.daemons.modify', 'kSMRightBlessPrivilegedHelper': 'com.apple.ServiceManagement.blesshelper'})
functions = {'SMCopyAllJobDictionaries': ('^{__CFArray=}^{__CFString=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'SMJobRemove': ('Z^{__CFString=}^{__CFString=}^{AuthorizationOpaqueRef=}Z^^{__CFError}', '', {'arguments': {0: {'type': b'^{__CFString=}'}, 1: {'type': b'^{__CFString=}'}, 2: {'type': b'^{AuthorizationOpaqueRef=}'}, 3: {'type': b'Z'}, 4: {'type': b'^^{__CFError}', 'type_modifier': b'o'}}}), 'SMJobBless': ('Z^{__CFString=}^{__CFString=}^{AuthorizationOpaqueRef=}^^{__CFError}', '', {'arguments': {0: {'type': b'^{__CFString=}'}, 1: {'type': b'^{__CFString=}'}, 2: {'type': b'^{AuthorizationOpaqueRef=}'}, 3: {'type': b'^^{__CFError}', 'type_modifier': b'o'}}}), 'SMJobCopyDictionary': ('^{__CFDictionary=}^{__CFString=}^{__CFString=}', '', {'retval': {'type': b'^{__CFDictionary=}', 'already_cfretained': True}}), 'SMJobSubmit': ('Z^{__CFString=}^{__CFDictionary=}^{AuthorizationOpaqueRef=}^^{__CFError}', '', {'arguments': {0: {'type': b'^{__CFString=}'}, 1: {'type': b'^{__CFDictionary=}'}, 2: {'type': b'^{AuthorizationOpaqueRef=}'}, 3: {'type': b'^^{__CFError}', 'type_modifier': b'o'}}})}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
finally:
    objc._updatingMetadata(False)
