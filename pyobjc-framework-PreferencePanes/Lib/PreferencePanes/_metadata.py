# Generated file, don't edit
# Source: BridgeSupport/PreferencePanes.bridgesupport
# Last update: Thu Jul 21 08:51:28 2011

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
constants = '''$NSPreferencePaneCancelUnselectNotification$NSPreferencePaneDoUnselectNotification$'''
enums = '''$NSUnselectCancel@0$NSUnselectLater@2$NSUnselectNow@1$'''
misc.update({'kNSPrefPaneHelpMenuAnchorKey': 'anchor', 'kNSPrefPaneHelpMenuTitleKey': 'title', 'kNSPrefPaneHelpMenuInfoPListKey': 'NSPrefPaneHelpAnchors'})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSPreferencePane', b'autoSaveTextFields', {'retval': {'type': b'Z'}})
    r('NSPreferencePane', b'isSelected', {'retval': {'type': b'Z'}})
    r('NSPreferencePane', b'replyToShouldUnselect:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
