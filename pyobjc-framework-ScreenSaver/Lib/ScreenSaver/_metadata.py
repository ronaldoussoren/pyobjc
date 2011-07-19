# Generated file, don't edit
# Source: BridgeSupport/ScreenSaver.bridgesupport
# Last update: Tue Jul 19 15:21:23 2011

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
functions = {'SSRandomPointForSizeWithinRect': (sel32or64('{_NSPoint=ff}{_NSSize=ff}{_NSRect={_NSPoint=ff}{_NSSize=ff}}', '{CGPoint=dd}{CGSize=ff}{CGRect={CGPoint=dd}{CGSize=dd}}'),), 'SSRandomIntBetween': ('iii',), 'SSRandomFloatBetween': ('fff',), 'SSCenteredRectInRect': (sel32or64('{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSRect={_NSPoint=ff}{_NSSize=ff}}', '{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}'),)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('ScreenSaverView', b'hasConfigureSheet', {'retval': {'type': b'Z'}})
    r('ScreenSaverView', b'initWithFrame:isPreview:', {'arguments': {3: {'type': b'Z'}}})
    r('ScreenSaverView', b'isAnimating', {'retval': {'type': b'Z'}})
    r('ScreenSaverView', b'isPreview', {'retval': {'type': b'Z'}})
    r('ScreenSaverView', b'performGammaFade', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
