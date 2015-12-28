# Generated file, don't edit
# Source: BridgeSupport/InterfaceBuilderKit.bridgesupport
# Last update: Thu Jul 21 08:47:20 2011

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "IBDocumentStorage*": objc.createOpaquePointerType('IBDocumentStorage*', b'^{IBDocumentStorage=}'),
    "IBInset": objc.createStructType('IBInset', b'{IBInsetTag="left"f"top"f"right"f"bottom"f}', None),
}
constants = '''$IBAdditionalLocalizableKeyPaths$IBAttributeKeyPaths$IBLocalizableGeometryKeyPaths$IBLocalizableStringKeyPaths$IBToManyRelationshipKeyPaths$IBToOneRelationshipKeyPaths$'''
enums = '''$IBMaxXDirection@2$IBMaxXMaxYDirection@10$IBMaxXMinYDirection@6$IBMaxYDirection@8$IBMinXDirection@1$IBMinXMaxYDirection@9$IBMinXMinYDirection@5$IBMinYDirection@4$IBNoDirection@0$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r(b'IBDocument', b'addObject:toParent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'IBDocument', b'childrenOfObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBDocument', b'connectAction:ofSourceObject:toDestinationObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'IBDocument', b'connectBinding:ofSourceObject:toDestinationObject:keyPath:options:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}, 6: {'type': b'@'}}})
    r(b'IBDocument', b'connectOutlet:ofSourceObject:toDestinationObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'IBDocument', b'documentForObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBDocument', b'documentImageNamed:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBDocument', b'metadataForKey:ofObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'IBDocument', b'moveObject:toParent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'IBDocument', b'objects', {'retval': {'type': b'@'}})
    r(b'IBDocument', b'parentOfObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBDocument', b'removeObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBDocument', b'setMetadata:forKey:ofObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'IBDocument', b'topLevelObjects', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'document', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'inspectedObjects', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'inspectedObjectsController', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'label', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'refresh', {'retval': {'type': b'v'}})
    r(b'IBInspector', b'sharedInstance', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'supportsMultipleObjectInspection', {'retval': {'type': b'Z'}})
    r(b'IBInspector', b'view', {'retval': {'type': b'@'}})
    r(b'IBInspector', b'viewNibName', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'didLoad', {'retval': {'type': b'v'}})
    r(b'IBPlugin', b'document:didAddDraggedObjects:fromDraggedLibraryView:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'IBPlugin', b'label', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'libraryNibNames', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'pasteboardObjectsForDraggedLibraryView:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r(b'IBPlugin', b'preferencesView', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'requiredFrameworks', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'sharedInstance', {'retval': {'type': b'@'}})
    r(b'IBPlugin', b'willUnload', {'retval': {'type': b'v'}})
    r(b'NSObject', b'ibAwakeInDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibDefaultChildren', {'retval': {'type': b'@'}})
    r(b'NSObject', b'ibDefaultImage', {'retval': {'type': b'@'}})
    r(b'NSObject', b'ibDefaultLabel', {'retval': {'type': b'@'}})
    r(b'NSObject', b'ibDidAddToDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibDidRemoveFromDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibIsChildInitiallySelectable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibRemoveChildren:', {'retval': {'type': b'Z'}})
    r(b'NSObject', b'ibIsChildViewUserMovable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibIsChildViewUserSizable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibObjectAtLocation:inWindowController:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': sel32or64(b'{_NSPoint=ff}', b'{CGPoint=dd}')}, 3: {'type': b'@'}}})
    r(b'NSObject', b'ibPopulateAttributeInspectorClasses:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibPopulateKeyPaths:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'ibRectForChild:inWindowController:', {'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSView', b'ibBaselineAtIndex:', {'retval': {'type': b'f'}, 'arguments': {2: {'type': b'i'}}})
    r(b'NSView', b'ibBaselineCount', {'retval': {'type': b'i'}})
    r(b'NSView', b'ibDesignableContentView', {'retval': {'type': b'@'}})
    r(b'NSView', b'ibLayoutInset', {'retval': {'type': b'{IBInsetTag=ffff}'}})
    r(b'NSView', b'ibMaximumSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r(b'NSView', b'ibMinimumSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r(b'NSView', b'ibPreferredDesignSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r(b'NSView', b'ibPreferredResizeDirection', {'retval': {'type': b'i'}})
finally:
    objc._updatingMetadata(False)
protocols={'IBObjectIntegration': objc.informal_protocol('IBObjectIntegration', [objc.selector(None, b'ibAwakeInDesignableDocument:', b'v@:@', isRequired=False), objc.selector(None, b'ibDefaultChildren', b'@@:', isRequired=False), objc.selector(None, b'ibDefaultImage', b'@@:', isRequired=False), objc.selector(None, b'ibDefaultLabel', b'@@:', isRequired=False), objc.selector(None, b'ibRemoveChildren:', b'Z@:@', isRequired=False), objc.selector(None, b'ibDidAddToDesignableDocument:', b'v@:@', isRequired=False), objc.selector(None, b'ibDidRemoveFromDesignableDocument:', b'v@:@', isRequired=False), objc.selector(None, b'ibIsChildInitiallySelectable:', b'Z@:@', isRequired=False), objc.selector(None, b'ibIsChildViewUserMovable:', b'Z@:@', isRequired=False), objc.selector(None, b'ibIsChildViewUserSizable:', b'Z@:@', isRequired=False), objc.selector(None, b'ibObjectAtLocation:inWindowController:', sel32or64(b'@@:{_NSPoint=ff}@', b'@@:{CGPoint=dd}@'), isRequired=False), objc.selector(None, b'ibPopulateAttributeInspectorClasses:', b'v@:@', isRequired=False), objc.selector(None, b'ibPopulateKeyPaths:', b'v@:@', isRequired=False), objc.selector(None, b'ibRectForChild:inWindowController:', sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@@', b'{CGRect={CGPoint=dd}{CGSize=dd}}@:@@'), isRequired=False)])}
