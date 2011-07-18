# Generated file, don't edit
# Source: BridgeSupport/Collaboration.bridgesupport
# Last update: Mon Jul 18 19:19:08 2011

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
    r('CBIdentity', b'CSIdentity', {'retval': {'type': b'^{__CSIdentity=}'}})
    r('CBIdentity', b'identityWithCSIdentity:', {'arguments': {2: {'type': b'^{__CSIdentity=}'}}})
    r('CBIdentity', b'isHidden', {'retval': {'type': b'Z'}})
    r('CBIdentity', b'isMemberOfGroup:', {'retval': {'type': b'Z'}})
    r('CBIdentityAuthority', b'CSIdentityAuthority', {'retval': {'type': b'^{__CSIdentityAuthority=}'}})
    r('CBIdentityAuthority', b'identityAuthorityWithCSIdentityAuthority:', {'arguments': {2: {'type': b'^{__CSIdentityAuthority=}'}}})
    r('CBIdentityPicker', b'allowsMultipleSelection', {'retval': {'type': b'Z'}})
    r('CBIdentityPicker', b'runModalForWindow:modalDelegate:didEndSelector:contextInfo:', {'arguments': {4: {'sel_of_type': sel32or64(b'v@:@i^v', b'v@:@q^v')}, 5: {'type': b'^v'}}})
    r('CBIdentityPicker', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': b'Z'}}})
    r('CBUserIdentity', b'authenticateWithPassword:', {'retval': {'type': b'Z'}})
    r('CBUserIdentity', b'certificate', {'retval': {'type': b'^{OpaqueSecCertificateRef=}'}})
    r('CBUserIdentity', b'isEnabled', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
