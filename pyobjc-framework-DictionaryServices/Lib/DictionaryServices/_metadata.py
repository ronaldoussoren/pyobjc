# Generated file, don't edit
# Source: BridgeSupport/DictionaryServices.bridgesupport
# Last update: Thu Jul 21 08:42:41 2011

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
functions = {'DCSDictionaryGetTypeID': (sel32or64('i', 'q'),), 'DCSGetTermRangeInString': ('{_CFRange=ll}^{__DCSDictionary=}^{__CFString=}l',), 'DCSCopyTextDefinition': ('^{__CFString=}^{__DCSDictionary=}^{__CFString=}{_CFRange=ll}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}})}
cftypes = []
cftypes.append(('DCSDictionaryRef', '^{__DCSDictionary=}', 'DCSDictionaryGetTypeID', None))
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
finally:
    objc._updatingMetadata(False)
