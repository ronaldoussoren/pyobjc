# Generated file, don't edit
# Source: BridgeSupport/AppleScriptObjC.bridgesupport
# Last update: Sun Jul 17 21:18:38 2011

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
finally:
    objc._updatingMetadata(False)
