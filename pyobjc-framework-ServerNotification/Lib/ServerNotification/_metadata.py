# Generated file, don't edit
# Source: BridgeSupport/ServerNotification.bridgesupport
# Last update: Tue Jul 19 15:18:10 2011

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
    r('NSServerNotificationCenter', b'addObserver:selector:name:object:', {'arguments': {3: {'sel_of_type': b'v@:@', 'type': b':'}}})
finally:
    objc._updatingMetadata(False)
