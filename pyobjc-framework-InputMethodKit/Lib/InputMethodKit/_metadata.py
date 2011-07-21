# Generated file, don't edit
# Source: BridgeSupport/InputMethodKit.bridgesupport
# Last update: Thu Jul 21 08:45:27 2011

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
constants = '''$IMKCandidatesOpacityAttributeName$IMKControllerClass$IMKDelegateClass$IMKModeDictionary$kIMKCommandClientName$kIMKCommandMenuItemName$IMKCandidatesSendServerKeyEventFirst$'''
enums = '''$kIMKLocateCandidatesAboveHint@1$kIMKLocateCandidatesBelowHint@2$kIMKLocateCandidatesLeftHint@3$kIMKLocateCandidatesRightHint@4$kIMKScrollingGridCandidatePanel@2$kIMKSingleColumnScrollingCandidatePanel@1$kIMKSingleRowSteppingCandidatePanel@3$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('IMKCandidates', b'dismissesAutomatically', {'retval': {'type': b'Z'}})
    r('IMKCandidates', b'isVisible', {'retval': {'type': b'Z'}})
    r('IMKCandidates', b'selectionKeysKeylayout', {'retval': {'type': b'^{__TISInputSource=}'}})
    r('IMKCandidates', b'setDismissesAutomatically:', {'arguments': {2: {'type': b'Z'}}})
    r('IMKCandidates', b'setSelectionKeysKeylayout:', {'arguments': {2: {'type': b'^{__TISInputSource=}'}}})
    r('IMKInputController', b'doCommandBySelector:commandDictionary:', {'arguments': {2: {'type': b':'}}})
    r('NSObject', b'didCommandBySelector:client:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b':'}}})
    r('NSObject', b'handleEvent:client:', {'retval': {'type': b'Z'}})
    r('NSObject', b'inputText:client:', {'retval': {'type': b'Z'}})
    r('NSObject', b'inputText:key:modifiers:client:', {'retval': {'type': b'Z'}})
    r('NSObject', b'mouseDownOnCharacterIndex:coordinate:withModifier:continueTracking:client:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}, 3: {'type': sel32or64(b'{_NSPoint=ff}', b'{CGPoint=dd}')}, 4: {'type': sel32or64(b'I', b'Q')}, 5: {'type': b'^Z', 'type_modifier': b'o'}}})
    r('NSObject', b'mouseMovedOnCharacterIndex:coordinate:withModifier:client:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}, 3: {'type': sel32or64(b'{_NSPoint=ff}', b'{CGPoint=dd}')}, 4: {'type': sel32or64(b'I', b'Q')}}})
    r('NSObject', b'mouseUpOnCharacterIndex:coordinate:withModifier:client:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': sel32or64(b'I', b'Q')}, 3: {'type': sel32or64(b'{_NSPoint=ff}', b'{CGPoint=dd}')}, 4: {'type': sel32or64(b'I', b'Q')}}})
finally:
    objc._updatingMetadata(False)
protocols={'IMKServerInput': objc.informal_protocol('IMKServerInput', [objc.selector(None, 'candidates:', '@@:@', isRequired=False), objc.selector(None, 'commitComposition:', 'v@:@', isRequired=False), objc.selector(None, 'composedString:', '@@:@', isRequired=False), objc.selector(None, 'didCommandBySelector:client:', 'Z@::@', isRequired=False), objc.selector(None, 'handleEvent:client:', 'Z@:@@', isRequired=False), objc.selector(None, 'inputText:client:', 'Z@:@@', isRequired=False), objc.selector(None, 'inputText:key:modifiers:client:', sel32or64('Z@:@iI@', 'Z@:@qQ@'), isRequired=False), objc.selector(None, 'originalString:', '@@:@', isRequired=False)])}
