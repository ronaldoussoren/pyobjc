# Generated file, don't edit
# Source: BridgeSupport/QuickLookUI.bridgesupport
# Last update: Thu Jul 21 17:06:28 2011

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
    r('NSObject', b'acceptsPreviewPanelControl:', {'retval': {'type': b'Z'}})
    r('NSObject', b'previewPanel:handleEvent:', {'retval': {'type': b'Z'}})
    r('NSObject', b'previewPanel:sourceFrameOnScreenForPreviewItem:', {'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{_NSRect={_NSPoint=dd}{_NSSize=dd}}')}})
    r('NSObject', b'previewPanel:transitionImageForPreviewItem:contentRect:', {'arguments': {4: {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{_NSRect={_NSPoint=dd}{_NSSize=dd}}')}}})
    r('QLPreviewPanel', b'enterFullScreenMode:withOptions:', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'sharedPreviewPanelExists', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'sharedPreviewPanelExists', {'retval': {'type': b'Z'}})
    r('QLPreviewPanel', b'isInFullScreenMode', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
protocols={'QLPreviewPanelController': objc.informal_protocol('QLPreviewPanelController', [objc.selector(None, 'acceptsPreviewPanelControl:', 'Z@:@', isRequired=False), objc.selector(None, 'beginPreviewPanelControl:', 'v@:@', isRequired=False), objc.selector(None, 'endPreviewPanelControl:', 'v@:@', isRequired=False)])}
