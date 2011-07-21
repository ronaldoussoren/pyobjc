# Generated file, don't edit
# Source: BridgeSupport/Message.bridgesupport
# Last update: Thu Jul 21 08:50:01 2011

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
constants = '''$NSASCIIMailFormat$NSMIMEMailFormat$NSSMTPDeliveryProtocol$NSSendmailDeliveryProtocol$'''
enums = '''$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSMailDelivery', b'hasDeliveryClassBeenConfigured', {'retval': {'type': b'Z'}})
    r('NSMailDelivery', b'deliverMessage:headers:format:protocol:', {'retval': {'type': b'Z'}})
    r('NSMailDelivery', b'deliverMessage:subject:to:', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
